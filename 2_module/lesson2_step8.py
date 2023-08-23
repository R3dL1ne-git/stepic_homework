import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем все обязательные поля
    browser.find_element(By.NAME, "firstname").send_keys("test")
    browser.find_element(By.NAME, "lastname").send_keys("test")
    browser.find_element(By.NAME, "email").send_keys("test")

    # находим элемент, файл и загружаем файл на сайт
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = os.path.join(current_dir, "file.txt")
    browser.find_element(By.ID, "file").send_keys(file_name)

    # нажимаем на кнопку Submit
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(5)
    browser.quit()