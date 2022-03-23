import time
from math import floor

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def launch_browser():

    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://orteil.dashnet.org/experiments/cookie/")
    return chrome_driver


driver = launch_browser()
end_time = time.time() + 5 * 60
cookie = driver.find_element(by=By.ID, value="cookie")
is_upgraded = False

while time.time() < end_time:
    elapsed_time = floor(end_time - time.time())
    cookie.click()
    if (elapsed_time % 5) == 0 and not is_upgraded:
        shop = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
        upgrade_list = []
        for item in shop:
            class_name = item.get_attribute("class")
            if not class_name:
                upgrade_list.append(item)
        upgrade_list[-1].click()
        is_upgraded = True
    elif (elapsed_time % 5) == 1:
        is_upgraded = False

cps = driver.find_element(by=By.ID, value="cps")
print(cps.text)
driver.quit()
