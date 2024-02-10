import psutil
import difflib
import pickle
from pathlib import Path
from backend.parse_foods_expiry import get_food_info

def kill_notifs() -> None:
    for proc in psutil.process_iter():
        if proc.name() == "main.py":
            proc.kill()

def search_for(item: str, foods: dict) -> str | list[str]:
    if item in foods:
        return foods[item]
    return difflib.get_close_matches(item, foods.keys())

def get_foods_cached():
    path = Path("storage/foods.pickle")
    if path.exists():
        with path.open("r") as f:
            return pickle.load(f)
    foods = get_food_info()
    with path.open("w") as f:
        pickle.dump(foods, f)
    return foods

