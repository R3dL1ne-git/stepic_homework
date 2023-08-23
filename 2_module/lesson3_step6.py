import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    # решаем формулу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # вставляем ответ в поле и нажимаем на кнопку
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()