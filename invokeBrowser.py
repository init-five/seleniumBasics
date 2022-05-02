# invoke browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# in case of an error, install webdriver manager from pip and also add from interpreter
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# to maximize the window
driver.maximize_window()
# open the site in the browser
driver.get("https://rahulshettyacademy.com/")

# get the title
print(driver.title)
# get the current url
print(driver.current_url)
# open another url
driver.get("https://rahulshettyacademy.com/practice-project")
time.sleep(5)
# to minimize the window
driver.minimize_window()

# to come back to previous button
driver.back()
# to refresh the page
driver.refresh()
# to keep the browser open for some time
time.sleep(5)
# close the browser
driver.close()
