# invoke browser
import time

from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")
# clear the already present text
# switch to frame
# we need frame name, index or value to get a specific frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I'm trying to enter text here")
# switch back to window
driver.switch_to.default_content()
# print the header text
