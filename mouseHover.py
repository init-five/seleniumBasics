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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# mouse hover
action = ActionChains(driver)
menu = driver.find_element(By.ID, "mousehover")
# action can interactions of mouse now
action.move_to_element(menu).perform()
time.sleep(3)
# select an option from the menu
childMenu = driver.find_element(By.LINK_TEXT, "Top")
action.move_to_element(childMenu).click()
time.sleep(5)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# to double-click
time.sleep(5)
doubleClick = driver.find_element(By.ID, "double-click")
action.double_click(doubleClick).perform()
# alert
alert = driver.switch_to.alert
alert.accept()
print(alert.text)

