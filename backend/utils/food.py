import pickle
from pathlib import Path
from backend.utils import StoredFood, FoodData
from backend.parse_foods_expiry import get_food_info

__all__ = [
    "get_foods_cached",
    "get_foods_in_database",
    "write_database",
    "append_to_database",
    "food_to_stored_food",
]

FOODS = Path("storage/foods.pickle")
DATABASE = Path("storage/database.pickle")

def get_foods_cached():
    """Returns dict of foods we have info for"""
    if FOODS.exists():
        with FOODS.open("rb") as f:
            return pickle.load(f)
    foods = get_food_info()
    with FOODS.open("wb") as f:
        pickle.dump(foods, f)
    return foods

def get_foods_in_database() -> list[StoredFood]:
    """Get foods in fridge"""
    if DATABASE.exists():
        with DATABASE.open("rb") as f:
            return pickle.load(f)
    write_database([])
    return []

def write_database(foods: list[StoredFood]) -> None:
    with DATABASE.open("wb") as f:
        pickle.dump(foods, f)

def append_to_database(*foods: StoredFood) -> None:
    write_database(
        get_foods_in_database() + list(foods)
    )

def food_to_stored_food(food_data: FoodData, storage_location: str) -> StoredFood:
    from datetime import datetime
    return StoredFood(
        name = food_data.name,
        date_stored=datetime.now(),
        max_time = getattr(food_data, storage_location.lower())
    )