from dataclasses import dataclass


@dataclass
class FoodData:
    name: str
    pantry: int
    fridge: int
    freezer: int

