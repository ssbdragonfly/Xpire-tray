import requests
from gui_utils import select_file
from typing import Any
from CTkMessagebox import CTkMessagebox

__all__ = [
    "get_image_info"
]

def get_image_info() -> dict[str, Any] | None:
    img = select_file()
    api_user_token = '5ad57c61cb39d998df48a783417e336d23f02fe8'
    headers = {'Authorization': 'Bearer ' + api_user_token}

    with img.open("rb") as f:
        url = 'https://api.logmeal.es/v2/image/segmentation/complete'
        resp = requests.post(url, files={'image': f}, headers=headers)
        if not resp:
            CTkMessagebox(message="No food name found.").mainloop()     
        else:
            url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
            resp = requests.post(url, json={'imageId': resp.json()['imageId']}, headers=headers)
            
            food_name = resp.json().get('foodName')
            if not food_name:
                CTkMessagebox(message="No food name found.").mainloop()
            else:
                return food_name

