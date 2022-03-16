from bs4 import BeautifulSoup
import requests

BUY_PRICE = 100
URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_fod_1?pd_rd_i=B08PQ2KWHS&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price_el = soup.select(
    "#corePrice_desktop span.a-price.a-text-price > span.a-offscreen"
)[1]

price = float(price_el.text.split("$")[1])

if price < BUY_PRICE:
    print(f"Your item is now below your ideal price of ${BUY_PRICE} at {price}!")
