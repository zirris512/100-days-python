from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# chrome_driver_path = "D:\\Users\\Mina5\\Development\\chromedriver.exe"
def launch_browser():

    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://www.python.org")
    return chrome_driver


driver = launch_browser()

dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li > a")

events_dict = {
    n: {"time": dates[n].text, "name": events[n].text} for n in range(len(dates))
}

# for n in range(len(dates)):
#     events_dict[n] = {"time": dates[n].text, "name": events[n].text}

print(events_dict)
