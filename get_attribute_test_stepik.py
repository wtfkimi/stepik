from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
import math
import time

def link():
    driver.get('http://suninjuly.github.io/get_attribute.html')

def find_riches():
    link()
    riches = driver.find_element(By.ID, 'treasure')
    check_riches = riches.get_attribute('valuex')

    value_of_check_riches = str(math.log(abs(12*math.sin(int(check_riches)))))
    input_field = driver.find_element(By.ID, 'answer')
    input_field.click()
    input_field.send_keys(value_of_check_riches)
    check_box = driver.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    radio_button = driver.find_element(By.ID, 'robotsRule')
    radio_button.click()
    sumbit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    sumbit_button.click()
    time.sleep(7)

find_riches()
driver.quit()