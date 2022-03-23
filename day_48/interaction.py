from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com")

first_name_input = driver.find_element(by=By.NAME, value="fName")
last_name_input = driver.find_element(by=By.NAME, value="lName")
email_input = driver.find_element(by=By.NAME, value="email")

first_name_input.send_keys("Billy")
last_name_input.send_keys("Jean")
email_input.send_keys("billy.jean@notlover.com")
email_input.submit()

success = driver.find_element(by=By.CLASS_NAME, value="display-3")
print(success.text)
