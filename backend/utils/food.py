import pickle
from pathlib import Path
from backend.utils import StoredFood, FoodData
from backend.parse_foods_expiry import get_food_info

__all__ = [
    "get_foods_cached",
    "get_foods_in_database",
    "write_database",
    "food_to_stored_food",
]

def get_foods_cached():
    """Returns dict of foods we have info for"""
    path = Path("storage/foods.pickle")
    if path.exists():
        with path.open("rb") as f:
            return pickle.load(f)
    foods = get_food_info()
    write_database(foods)
    return foods

def get_foods_in_database() -> list[StoredFood]:
    """Get foods in fridge"""
    existing = Path("storage/database.pickle")
    if existing.exists():
        with existing.open("rb") as f:
            return pickle.load(f)
    write_database([])
    return []

def write_database(foods: list[StoredFood]) -> None:
    with open("storage/database.pickle", "wb") as f:
        pickle.dump(foods, f)

def food_to_stored_food(food_data: FoodData, storage_location: str) -> StoredFood:
    from datetime import datetime
    return StoredFood(
        name = food_data.name,
        date_stored=datetime.now(),
        max_time = getattr(food_data, storage_location.lower())
    )