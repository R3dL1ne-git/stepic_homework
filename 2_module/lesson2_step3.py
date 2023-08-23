import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим числа с h1 и складываем
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    num3 = int(num1) + int(num2)

    # выбираем в селекте с value = num3
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num3))

    # нажимаем на кнопку Submit
    browser.find_element(By.CLASS_NAME, "btn").click()
    
finally:
    time.sleep(5)
    browser.quit()