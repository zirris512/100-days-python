import pandas
from datetime import datetime
import smtplib
from random import randint
from dotenv import load_dotenv
import os

load_dotenv("./.env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

today = (datetime.now().month, datetime.now().day)

contacts = pandas.read_csv("birthdays.csv")
birthdays_dict = {(val["month"], val["day"]): val for (key, val) in contacts.iterrows()}

if today in birthdays_dict:
    letter_number = randint(1, 3)
    birthday_name = birthdays_dict[today]["name"]
    birthday_email = birthdays_dict[today]["email"]

    with open(f"letter_templates/letter_{letter_number}.txt") as file:
        birthday_letter = file.read()
    birthday_letter = birthday_letter.replace("[NAME]", birthday_name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday\n\n{birthday_letter}",
        )
