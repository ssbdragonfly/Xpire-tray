from datetime import datetime
from notify import notification
import schedule
from backend.data import StoredFood

def schedule_reminders(foods: dict[str, StoredFood], tol: int) -> None:
    schedule.every().day().at("10:30").do(lambda foods=foods: _reminder(foods, tol))


def _reminder(foods: dict[str, StoredFood], tol: int) -> None:
    for name, food in foods.items():
        diff = (datetime.now() - food.date_stored).days
        if diff > food.max_time - tol:
            _send_notif(
                'Food Expiring!',
                message=f"{name} is expiring in {food.max_time-diff} days, use it soon!"
            )

def _send_notif(*args, **kwargs) -> None:
    try:
        notification(
            *args,
            **kwargs
        )
    except RuntimeError:
        pass


