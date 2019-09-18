from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
import math
import time

def link():
    driver.get('http://suninjuly.github.io/alert_accept.html')


def accept_alert():
    link()
    button_magic = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button_magic.click()

    alert = driver.switch_to.alert
    alert.accept()

    input_value = driver.find_element(By.ID, 'input_value').text
    a = str(math.log(abs(12*math.sin(int(input_value)))))
    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(a)

    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button_submit.click()
    time.sleep(5)

accept_alert()
driver.quit()