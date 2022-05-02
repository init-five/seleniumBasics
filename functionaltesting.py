import time

from select import select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# list to put all the items
list = []
list2 = []
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
    # getting names of all the searched items
    # //div[@class='product-action']/button/parent::div/parent::div/h4
    list.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    button.click()
#print(list)
# click on cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in veggies:
    list2.append(veg.text)
#print(list2)
# compare the lists
assert list == list2
# price before discount
priceBeforeDiscount = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
#print(priceBeforeDiscount)
# enter promo code to get discount
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
# click on apply
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(10)
# price after discount
priceAfterDiscount = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
#print(priceAfterDiscount)
assert int(priceBeforeDiscount) > float(priceAfterDiscount)
#print(driver.find_element(By.CSS_SELECTOR, ".promoBtn").text)
# comparing price in the table with the total amount
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")
total_amount = 0
for amount in amounts:
    total_amount += int(amount.text)
print(f"total in table is {total_amount}")
final_total = driver.find_element(By.CLASS_NAME, "totAmt").text
print(f"total amount in total is {final_total}")
assert int(final_total) == total_amount



