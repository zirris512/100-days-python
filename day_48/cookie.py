import time
from math import floor

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def launch_chrome_browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    chrome_driver = webdriver.Chrome(service=service, options=options)

    chrome_driver.get("https://orteil.dashnet.org/experiments/cookie/")
    return chrome_driver


# Driver instance to avoid garbage collection
driver = launch_chrome_browser()
# Will run for 5 minutes
end_time = time.time() + 5 * 60
cookie = driver.find_element(by=By.ID, value="cookie")
is_upgraded = False

while time.time() < end_time:
    elapsed_time = floor(end_time - time.time())
    cookie.click()

    # Check and purchase upgrades every 5 seconds
    if (elapsed_time % 5) == 0 and not is_upgraded:
        shop = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
        upgrade_list = []
        for item in shop:
            class_name = item.get_attribute("class")
            if not class_name:
                upgrade_list.append(item)
        # click and upgrade most expensive upgrade available
        upgrade_list[-1].click()
        is_upgraded = True
    elif (elapsed_time % 5) == 1:
        is_upgraded = False

# Display cookies/second at finish
cps = driver.find_element(by=By.ID, value="cps")
print(cps.text)

driver.quit()
