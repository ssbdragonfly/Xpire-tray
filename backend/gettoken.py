import requests

# Set the API Company Token in the header of the request
headers = {'Authorization': 'Bearer ' + '15ce8843e122167e593a87160b2bfe5f1892d749'}

# Get all your API Users
response = requests.post('/users/APIUsers', headers=headers)

# Get the API User Token from the response
APIUsers_list = response.get_json()

# Get the Id, Token, language and username of the first API User:
APIUsers_list[0]["id"]
APIUsers_list[0]["token"]
APIUsers_list[0]["language"]
APIUsers_list[0]["user"]
