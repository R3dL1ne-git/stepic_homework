import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    # находим кнопку Book
    button = browser.find_element(By.ID, "book")

    # ожидаем, пока цена не станет равной 100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # после жмем на кнопку
    button.click()

    # находим значение x и считаем по формуле
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # вводим ответ формулы в поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # нажимаем на кнопку Submit
    browser.find_element(By.ID, "solve").click()

finally:
    #time.sleep(2)
    print(browser.switch_to.alert.text)
    browser.quit()