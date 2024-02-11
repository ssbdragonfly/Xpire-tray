import requests
from gui_utils import select_file
from typing import Any
from CTkMessagebox import CTkMessagebox

__all__ = [
    "get_image_info"
]

def get_image_info() -> dict[str, Any] | None:
    img = select_file()
    api_user_token = '87eb9de2098804745eefda4af0421b4a2b03f47c'
    headers = {'Authorization': 'Bearer ' + api_user_token}

    with img.open("rb") as f:
        url = 'https://api.logmeal.es/v2/image/segmentation/complete'
        resp = requests.post(url, files={'image': f}, headers=headers)
        if not resp:
            print('not working')           
        else:
            url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
            resp = requests.post(url, json={'imageId': resp.json()['imageId']}, headers=headers)
            
            food_name = resp.json().get('foodName')
            if not food_name:
                CTkMessagebox(message="No food name found.")
            else:
                return resp.json()

