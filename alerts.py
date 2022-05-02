import time

from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# alert boxes
validateText = "Subhan"
driver.find_element(By.NAME, "enter-name").send_keys("Subhan")
driver.find_element(By.ID, "alertbtn").click()
#driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
# to check whether the text is in the alert box or not
alertText = alert.text
assert validateText in alertText
alert.accept()
#alert.dismiss()
# to click on cancel button in alert box

time.sleep(5)