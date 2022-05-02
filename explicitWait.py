import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
# import to use with explicit wait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
# explicit wait
wait = WebDriverWait(driver, 10)
# wait for this test
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='products']/div")))
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
# explicit wait until promo code is present
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))
# enter promo code to get discount
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
# click on apply
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "promoBtn")))
print(driver.find_element(By.CSS_SELECTOR, ".promoBtn").text)

