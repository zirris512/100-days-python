import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from dotenv import load_dotenv

load_dotenv()

UDEMY_EMAIL = os.getenv("UDEMY_EMAIL")
UDEMY_PASS = os.getenv("UDEMY_PASS")


def launch_browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_driver = webdriver.Chrome(service=service, options=options)

    chrome_driver.get("https://www.udemy.com")
    return chrome_driver


driver = launch_browser()

login_button = WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.CSS_SELECTOR, 'a[data-purpose="header-login"]'))
)
login_button.click()

email = driver.find_element(by=By.ID, value="email--1")
password = driver.find_element(by=By.ID, value="id_password")
submit_button = driver.find_element(by=By.ID, value="submit-id-submit")

email.send_keys(UDEMY_EMAIL)
password.send_keys(UDEMY_PASS)
submit_button.click()

python_course = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.CSS_SELECTOR, 'div[data-index="0"] a'))
)
python_course.click()

driver.quit()
