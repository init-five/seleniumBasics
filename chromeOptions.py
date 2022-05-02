import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# in case of an error, install webdriver manager from pip and also add from interpreter
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
# start with maximize window
chrome_options.add_argument("--start-maximized")
# do not open browser
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)