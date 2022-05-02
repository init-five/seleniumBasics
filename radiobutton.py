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
# radio button
radiobutton = driver.find_elements(By.NAME, "radioButton")
radiobutton[2].click()
time.sleep(5)
