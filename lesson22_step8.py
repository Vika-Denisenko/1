import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
print(current_dir)
print(file_path)

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем обязательные поля
    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys('Ivan')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Petrov')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('gmai@gmail.com')
    file_input = browser.find_element(By.ID, 'file')
    file_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
