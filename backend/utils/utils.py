import psutil
import difflib
from enum import Enum
from typing import Callable



__all__ = [
    "kill_notifs",
    "search_for",
    "pcall",
    "ExitCode"
]

class ExitCode(Enum):
    FAILURE = 1
    SUCCESS = 0

def pcall(f: Callable, *args, **kwargs) -> int:
    try:
        f()
        return ExitCode.SUCCESS
    except Exception:
        return ExitCode.FAILURE

def kill_notifs() -> None:
    for proc in psutil.process_iter():
        if proc.name() == "main.py":
            proc.kill()

def search_for(item: str, foods: dict) -> str | list[str]:
    if item in foods:
        return foods[item]
    return difflib.get_close_matches(item, foods.keys())


