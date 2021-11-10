import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
USERNAME = os.getenv("SHEETY_USERNAME")
PASSWORD = os.getenv("SHEETY_PASSWORD")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY, "x-remote-user-id": "0"}
nutritionix_params = {"query": input("What exercise did you do today? ")}

response = requests.post(
    url=nutritionix_endpoint, json=nutritionix_params, headers=headers
)
nutritionix_data = response.json()["exercises"]

today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%H:%M:%S")

for calorie_data in nutritionix_data:
    sheety_params = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": calorie_data["name"].title(),
            "duration": calorie_data["duration_min"],
            "calories": calorie_data["nf_calories"],
        }
    }

    response = requests.post(
        url=SHEET_ENDPOINT, json=sheety_params, auth=(USERNAME, PASSWORD)
    )

    if response.status_code == 200:
        print(f"Successfully added {calorie_data['name'].title()}.")
