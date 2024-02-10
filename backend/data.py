from dataclasses import dataclass


@dataclass
class FoodData:
    name: str
    pantry: int = -1
    fridge: int = -1
    fridge_after_opening: int = -1
    freezer: int = -1

