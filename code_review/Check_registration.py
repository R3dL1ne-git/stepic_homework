from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = 'Васисуалий'
    last_name = 'Воханкин'
    email = 'vasya@example.org'
    phone = '88005553535'
    address = 'ул. Пушкина, д. Плюшкина'
    
    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').clear()
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys(first_name)
    
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').clear()
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys(last_name)    
    
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').clear()
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys(email)
        
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone:"]').clear()
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone:"]').send_keys(phone)
    
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]').clear()
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]').send_keys(address)   

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()