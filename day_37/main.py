# Habit Tracker
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USER = os.getenv("PIXELA_USER")
GRAPH_ID = os.getenv("GRAPH_ID")

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"

header = {"X-USER-TOKEN": PIXELA_TOKEN}

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
print(response.text)

yesterday = datetime(year=2021, month=11, day=7)

update_params = {"quantity": "1.5"}

# response = requests.put(
#     url=f"{pixel_endpoint}/{yesterday.strftime('%Y%m%d')}",
#     json=update_params,
#     headers=header,
# )
# print(response.text)

# response = requests.delete(
#     url=f"{pixel_endpoint}/{today.strftime('%Y%m%d')}", headers=header
# )
# print(response.text)
