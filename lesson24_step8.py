
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим элемент с ценой
    element_price = WebDriverWait(browser, 15).until(
        text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()


    # Считываем значение х и считаем с ним формулу, вставляем ответ в окно
    x_element=browser.find_element(By.ID, 'input_value')
    x=x_element.text
    y=calc(x)

    answer=browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    # закрываем браузер после всех манипуляций
    browser.quit()
