from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим кнопку и кликаем по ней
    button=browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

    #Переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    # Считываем значение х и считаем с ним формулу, вставляем ответ в окно
    x_element=browser.find_element(By.ID, 'input_value')
    x=x_element.text
    y=calc(x)

    answer=browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()


    ...


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
