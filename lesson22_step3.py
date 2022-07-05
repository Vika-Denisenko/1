from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:

    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Ищем два числа и считаем сумму
    num1=browser.find_element(By.ID, 'num1').text
    num2=browser.find_element(By.ID, 'num2').text
    summa=int(num1)+int(num2)

    #ищем селект и выбираем сумму
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summa))  # ищем элемент с текстом = summa

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
