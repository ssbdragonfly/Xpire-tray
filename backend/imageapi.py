import requests
from gui_utils import select_file
from typing import Any
from CTkMessagebox import CTkMessagebox
import customtkinter

def get_image_info() -> dict[str, Any]:
    img = select_file()
    api_user_token = 'fc2d833b315c0fbfe7b9fafc3ca65a5fc6652d2b'
    headers = {'Authorization': 'Bearer ' + api_user_token}

    with img.open("rb") as f:
        url = 'https://api.logmeal.es/v2/image/segmentation/complete'
        resp = requests.post(url, files={'image': f}, headers=headers)
        if not resp:
            print('not working')
            
        else:
            url = 'https://api.logmeal.es/v2/recipe/ingredients'
            resp = requests.post(url, json={'imageId': resp.json()['imageId']}, headers=headers)
            
            food_name = resp.json().get('foodName')
            if not food_name:
                CTkMessagebox(message="No food name found.")
            else:
                return food_name

