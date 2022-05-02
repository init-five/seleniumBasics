# invoke browser
import time

from select import select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# to double-click
actions = ActionChains(driver)
time.sleep(5)
doubleClick = driver.find_element(By.ID, "double-click")
actions.double_click(doubleClick).perform()
# alert
#alerts = driver.switch_to.alert
#alerts.accept()
#print(alerts.text)
time.sleep(5)
