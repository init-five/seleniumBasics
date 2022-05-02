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
# check box
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
# check all the checkboxes
for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()
# to select one option
#for checkbox in checkboxes:
    #if checkbox.get_attribute("value") == "option2":
        #checkbox.click()
        #assert checkbox.is_selected()
time.sleep(5)