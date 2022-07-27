import requests
import json
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

with open('env.json', 'r') as file:
    env = json.load(file)

user_params = {
    "token": env.get("token"),
    "username": env.get("username"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# creatring a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{env.get("username")}/graphs'

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": env.get("token")
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{env.get("username")}/graphs/graph1'

headers = {
    "X-USER-TOKEN": env.get("token")
}

# today = datetime.now()
today = datetime(year=2022, month=7, day=18)
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.74"
}


# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


pixel_update_url = f'{pixel_endpoint}/20220725'

update_params = {
    "quantity": "3.45"
}

# response = requests.put(url=pixel_update_url, json=update_params, headers=headers)
# print(response.text)

resposne = requests.delete(url=pixel_update_url, headers=headers)
print(resposne.text)
