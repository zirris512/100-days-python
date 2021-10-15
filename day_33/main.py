import smtplib

import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv("./.env")

MY_LAT = int(os.getenv("MY_LAT"))
MY_LONG = int(os.getenv("MY_LONG"))
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (
        MY_LAT - 5 >= iss_latitude >= MY_LAT + 5
        and MY_LONG >= iss_longitude >= MY_LONG + 5
    ):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 6
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 18

    time_now = datetime.now().hour

    if sunset < time_now < sunrise:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you now!",
        )

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
