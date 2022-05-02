# invoke browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://login.salesforce.com/")
print(driver.find_element(By.XPATH, '//*[@id="usernamegroup"]/label').text)
print(driver.find_element(By.XPATH, '//*[@id="login_form"]/label').text)
# finding element by tag name
driver.find_element(By.ID, "username").send_keys("check@check.com")
# find element by class name
driver.find_element(By.CLASS_NAME, "password").send_keys("password")
# to clear the input
driver.find_element(By.CLASS_NAME, "password").clear()
driver.find_element(By.ID, "Login").click()
# link
#driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()


time.sleep(10)
