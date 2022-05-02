import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from mouseHover import action

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# to double-click
time.sleep(5)
doubleClick = driver.find_element(By.ID, "double-click")
action.double_click(doubleClick).perform()
# alert
alert = driver.switch_to.alert
alert.accept()
print(alert.text)
