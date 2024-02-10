from backend.constants import FOOD_DATA_PATH
from backend.data import FoodData 
import csv


def get_food_info() -> dict[str, FoodData]:
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
            data = FoodData(
                name = name,
                pantry = _get_timelength(row, 6),
                fridge = _get_timelength(row, 17),
                fridge_after_opening = _get_timelength(row, 25, compare_against_dop=False),
                freezer = _get_timelength(row, 31)
            )
            foods[name] = data
    return foods

def _get_timelength(row: list[str], index: int, buffer: int = 3, compare_against_dop: bool = True) -> int:
    return max(
        _parse_timelength(row[index], row[index+1]),
        _parse_timelength(row[index+buffer+1], row[index+buffer+2])
    ) if compare_against_dop else _parse_timelength(row[index], row[index+1])

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

