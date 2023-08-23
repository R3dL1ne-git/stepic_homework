import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstName_input = browser.find_element(By.TAG_NAME, "input")
    lastName_input = browser.find_element(By.NAME, "last_name")
    city_input = browser.find_element(By.CLASS_NAME, "city")
    country_input = browser.find_element(By.ID, "country")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    firstName_input.send_keys("Ivan")
    lastName_input.send_keys("Petrov")
    city_input.send_keys("Smolensk")
    country_input.send_keys("Russia")
    button.click()
    

finally:
    time.sleep(30)
    browser.exit()
