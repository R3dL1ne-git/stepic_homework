import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение x
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    
    # считаем мат.функцию от x
    y = calc(x)

    # вводим ответ в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # находим элемент radioButton
    people_radio = browser.find_element(By.ID, "peopleRule")

    # находим элемент 'checked' с помощью встроенного метода get_attribute 
    # и проверим значение
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

finally:
    time.sleep(5)
    browser.quit()