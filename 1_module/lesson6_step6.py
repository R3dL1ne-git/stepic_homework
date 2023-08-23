from selenium import webdriver
from selenium.webdriver.common.by import By

# Подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен для примера
link = "https://fake-shop.com"
browser = webdriver.Chrome()
browser.get(link + "/book1.html")

# Добавляем товар в корзину
add_button = browser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# открываем страницу второго товара
browser.get(link + "/book2.html")

# добавляем товар в корзину
add_button = browser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get(link + "/basket.html")

# ищем все добавленные товары
goods = browser.find_elements(By.CSS_SELECTOR, ".good")

# проверяем, что количество товаров равно 2
assert len(goods) == 2