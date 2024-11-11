import requests
from gui_utils import select_file
from typing import Any
from backend.utils import ExitCode
from CTkMessagebox import CTkMessagebox

__all__ = [
    "get_image_info"
]

def get_image_info() -> dict[str, Any] | None | int:
    img = select_file()
    api_user_token = '6b444efc95ca6e691dbc76393edca1d30c0637af'
    headers = {'Authorization': 'Bearer ' + api_user_token}

    if img.is_dir():
        return ExitCode.FAILURE # user exited it
    with img.open("rb") as f:
        url = 'https://api.logmeal.es/v2/image/segmentation/complete'
        resp = requests.post(url, files={'image': f}, headers=headers)
        if not resp:
            CTkMessagebox(message="No food name found.").mainloop()           
        else:
            url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
            resp = requests.post(url, json={'imageId': resp.json()['imageId']}, headers=headers)
            
            food_data = resp.json()
            food_name = food_data.get('foodName')
            if not food_name:
                CTkMessagebox(message="No food name found.").mainloop()
            else:
                return food_data

