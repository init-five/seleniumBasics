# invoke browser
import time

from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# dynamic list
driver.find_element(By.ID, "autocomplete").send_keys("pak")
time.sleep(5)
countries = driver.find_elements(By.XPATH, '//*[@id="autocomplete"]')
print(len(countries))
for country in countries:
    if country == "Pakistan":
        country.click()
        break
assert driver.find_element(By.ID, "autocomplete").get_attribute('value') == "Pakistan"