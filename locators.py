# invoke browser
import time

from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
# name locator and enter input "Subhan"
driver.find_element(By.NAME, "name").send_keys("Subhan")
# element by css locator
driver.find_element(By.CSS_SELECTOR, "input[name = 'email']").send_keys("subhan.ihsan@codedistrict.com")
# checking the check box
driver.find_element(By.ID, "exampleCheck1").click()
# static dropdown where options are fixed
# select class provide the method to handle the options in dropdown
dropdown = driver.find_element(By.ID, "exampleFormControlSelect1")
dd = Select(dropdown)
dd.select_by_visible_text("Female")
#dd.select_by_index(0)
# using the xpath
driver.find_element(By.XPATH, "//input[@type='submit']").click()
# verify the success text upon submitting the form
message = driver.find_element(By.CLASS_NAME, "alert-success").text
# checking success in the message
assert "success" in message

time.sleep(10)