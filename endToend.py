import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# in case of an error, install webdriver manager from pip and also add from interpreter
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/angularpractice/")
# click on shop
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
# select products
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    # //div[@class='card h-100']/div/h4/a
    # get the product names
    productName = product.find_element(By.XPATH, "div/h4/a").text
    # select blackberry in the products
    if productName == "Blackberry":
        # add in the card
        # //div[@class='card h-100']/div[2]/button
        product.find_element(By.XPATH, "div[2]/button").click()
# click on checkout button
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
# click on checkout on next page
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
# search a country
driver.find_element(By.ID, "country").send_keys("Pak")
# wait till it loads
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Pakistan")))
# click on pakistan in the list
driver.find_element(By.LINK_TEXT, "Pakistan").click()
# click on purchase
driver.find_element(By.CSS_SELECTOR, "input[class*='btn-lg']").click()
successText = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-dismissible']").text
assert "Success!" in successText
# take screenshot
driver.get_screenshot_as_file("screen.png")
