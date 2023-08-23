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

    # нажимаем на чек-бокс I'm the robot
    browser.find_element(By.ID, "robotCheckbox").click()

    # нажимаем на радиобаттон Robots rule
    browser.find_element(By.ID, "robotsRule").click()

    # нажимаем на кнопку Submit
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(5)
    browser.quit()