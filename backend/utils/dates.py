from datetime import datetime
import time
from backend.utils.data import StoredFood
from backend.utils.utils import ExitCode
from backend.utils.food import get_foods_in_database

__all__ = [
    "schedule_reminders"
]

def schedule_reminders(tol: int) -> None:
    while True:
        # recalculate every day
        _reminder(get_foods_in_database(), tol)
        time.sleep(24 * 60 * 60)


def _reminder(foods: list[StoredFood], tol: int) -> None:
    for food in foods:
        name = food.name
        diff = (datetime.now() - food.date_stored).days
        if diff > food.max_time - tol:
            _send_notif(
                title='Food Expiring!',
                message=f"{name} is expiring in {food.max_time-diff} days, use it soon!",
                timeout = 60
            )

def _send_notif(*args, **kwargs) -> int:
    from plyer import notification
    try:
        notification.notify(
            *args,
            **kwargs
        )
    except RuntimeError:
        return ExitCode.FAILURE
    else:
        return ExitCode.SUCCESS


