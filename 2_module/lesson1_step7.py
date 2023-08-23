import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    #img = browser.find_element(By.ID, "treasure")
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")

    #x = img.get_attribute("valuex")

    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "robotCheckbox").click()

    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(5)
    browser.quit()
