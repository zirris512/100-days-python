import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

load_dotenv()

API_KEY = os.getenv("API_KEY")
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")
MY_PHONE = os.getenv("MY_PHONE")
ACCT_SID = os.getenv("TWILIO_ACCT_ID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}


def check_for_rain(hours):
    for hour in hours:
        if hour["id"] < 700:
            return True
    return False


response = requests.get(OWM_URL, params=params)
response.raise_for_status()

weather_data = response.json()
half_day_weather = [weather["weather"][0] for weather in weather_data["hourly"][:12]]

if check_for_rain(half_day_weather):
    proxy_client = TwilioHttpClient(
        proxy={"http": os.environ["http_proxy"], "https": os.environ["https_proxy"]}
    )
    client = Client(ACCT_SID, AUTH_TOKEN, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_="+14436478809",
        to=MY_PHONE,
    )
    print(message.status)
