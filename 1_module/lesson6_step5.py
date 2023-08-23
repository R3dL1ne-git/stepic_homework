import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
result = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    driver = webdriver.Chrome()
    driver.get(link)

    link_ = driver.find_element(By.LINK_TEXT, result)
    link_.click()

    firstName_input = driver.find_element(By.TAG_NAME, "input")
    lastName_input = driver.find_element(By.NAME, "last_name")
    city_input = driver.find_element(By.CLASS_NAME, "city")
    country_input = driver.find_element(By.ID, "country")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")

    firstName_input.send_keys("Ivan")
    lastName_input.send_keys("Petrov")
    city_input.send_keys("Smolensk")
    country_input.send_keys("Russia")
    button.click()

finally:
    time.sleep(10)
    driver.exit()