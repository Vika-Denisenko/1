from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element=browser.find_element(By.ID, 'treasure')
    x=x_element.get_attribute('valuex')
    print(x)
    y=calc(x)
    print(y)
    answer=browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    robot_checkbox=browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robots_rule=browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()
    button=browser.find_element(By.CLASS_NAME, 'btn-default')
    button.click()

    ...


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
