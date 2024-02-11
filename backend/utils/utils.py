from __future__ import annotations

import difflib
from enum import Enum
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from backend.utils.data import FoodData



__all__ = [
    "search_for",
    "pcall",
    "ExitCode"
]

class ExitCode(Enum):
    FAILURE = 1
    SUCCESS = 0

def pcall(f: Callable, *args, **kwargs) -> int:
    """Make a function not raise an exception by catching it and returning an exit code."""
    try:
        f(*args, **kwargs)
        return ExitCode.SUCCESS
    except Exception:
        return ExitCode.FAILURE

def search_for(item: str, foods: dict[str, FoodData]) -> FoodData | list[str]:
    if item in foods:
        return foods[item]
    return difflib.get_close_matches(item, foods.keys())


