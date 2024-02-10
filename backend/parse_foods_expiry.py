from backend.constants import FOOD_DATA_PATH
from backend.data import FoodData 
import csv


def get_food_info():
    """Returns a dictionary mapping a food name to a `FoodData`
    instance. This dataclass contains the pantry, fridge, fridge_after_open, and freezer attributes.
    If the item should not be in a {pantry, fridge, freezer} the attribute will be -1
    """
    foods = {}
    with FOOD_DATA_PATH.open(newline="", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == "ID":
                continue # skip headers
            name = row[2]
            print("hi!", row[21], row)
            data = FoodData(
                name = name,
                pantry = _get_timelength(row, 6, 3),
                fridge = _get_timelength(row, 17, 3),
                fridge_after_opening = _get_timelength(row, 25, buffer=0),
                freezer = _get_timelength(row, 31)
            )
            foods[name] = data
            print(data)

def _get_timelength(row: list[str], index: int, buffer: int = 3) -> int:
    return max(
        _parse_timelength(row[index], row[index+1]),
        _parse_timelength(row[index+buffer+1], row[index+buffer+2])
    )

def _parse_timelength(length: str, unit: str) -> int:
    """Converts a length to days"""
    factors = {
        "Days": 1,
        "Weeks": 7,
        "Months": 30,
        "Years": 365
    }
    try:
        return int(length)*factors[unit] if length else -1
    except (KeyError, ValueError):
        return -1 # empty values

