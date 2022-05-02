import time

from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
# implicit wait applied to all the steps
# each step will wait till 10 seconds to load the page
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
# to check the count is 3
assert count == 3
# adding all the items in the cart with one click
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
# we pulled all the buttons one by one and clicked
for button in buttons:
    button.click()
# click on cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# enter promo code to get discount
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
# click on apply
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(10)
print(driver.find_element(By.CSS_SELECTOR, ".promoBtn").text)

