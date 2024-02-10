from backend.constants import FOOD_DATA_PATH
from backend.data import FoodData 
import csv


def get_food_info():
    """Returns a dictionary mapping a food name to a `FoodData`
    instance. This dataclass contains the pantry, fridge, and freezer attributes.
    If the item should not be in a {pantry, fridge, freezer} the attribute will be -1
    """
    with FOOD_DATA_PATH.open(newline="", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
    foods = {}
    for row in reader:
        name = row[2]
        data = FoodData(
            name = name,
            pantry = _get_timelength(row, 6),
            fridge = _get_timelength(row, 16)
        )

def _get_timelength(row: list[str], index: int) -> int:
    return max(_parse_timelength(row[index], row[index+1]), _parse_timelength(row[index+3], row[index+4]))

def _parse_timelength(length: str, unit: str) -> int:
    """Converts a length to days"""
    factors = {
        "Days": 1,
        "Weeks": 7,
    }
    return int(length)*factors[unit] if length else -1

