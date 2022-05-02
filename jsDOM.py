import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# in case of an error, install webdriver manager from pip and also add from interpreter
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("hello")
# text = driver.find_element(By.NAME, "name").get_attribute("value")
# use javascript to get text entered by selenium
text = driver.execute_script('return document.getElementsByName("name")[0].value')
print(text)
# click on button using javascript
shopButton = driver.find_element(By.XPATH, '/html/body/app-root/app-navbar/div/nav/ul/li[2]/a')
driver.execute_script("arguments[0].click();", shopButton)
# scroll down the browser
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)