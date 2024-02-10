from dataclasses import dataclass
from datetime import datetime


@dataclass
class FoodData:
    name: str
    pantry: int = -1
    fridge: int = -1
    fridge_after_opening: int = -1
    freezer: int = -1

@dataclass
class StoredFood:
    name: str
    date_stored: datetime
    max_time: int

