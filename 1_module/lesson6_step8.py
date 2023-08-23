from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstName_input = browser.find_element(By.TAG_NAME, "input")
    lastName_input = browser.find_element(By.NAME, "last_name")
    city_input = browser.find_element(By.CLASS_NAME, "city")
    country_input = browser.find_element(By.ID, "country")

    button = browser.find_element(By.XPATH, "//button[text() = 'Submit']")

    firstName_input.send_keys("Ivan")
    lastName_input.send_keys("Petrov")
    city_input.send_keys("Smolensk")
    country_input.send_keys("Russia")
    button.click()
    

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла