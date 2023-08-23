import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    browser.find_element(By.ID, "verify").click()

    message = browser.find_element(By.ID, "verify_message")
    
    assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()