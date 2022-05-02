# invoke browser
import time

from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
# get the parent window
#parentWindow = driver.window_handles[0]
# getting child window
childWindow = driver.window_handles[1]
# switch window to child window
driver.switch_to.window(childWindow)
# get text of new window
text = driver.find_element(By.TAG_NAME, "h3").text
print(text)
# close the child window
driver.close()
# go back to parent window
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(3)