from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение х и считаем с ним формулу, вставляем ответ в окно
    x_element=browser.find_element(By.ID, 'input_value')
    x=x_element.text
    y=calc(x)

    answer=browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    robot_checkbox=browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robots_rule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)

    robots_rule.click()
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()


    ...


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
