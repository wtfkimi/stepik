from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')


def function_for_math():
    driver.get('http://suninjuly.github.io/math.html')
    #input in field true value
    x_d = driver.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    y = x_d.text
    a = str(math.log(abs(12*math.sin(int(y)))))

    field = driver.find_element(By.ID, 'answer')
    field.click()
    field.send_keys(a)
    #click to robot_checkbox
    check_box = driver.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    #click to radio_button
    radio_button = driver.find_element(By.ID, 'robotsRule')
    radio_button.click()
    #click to button submit
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()

    time.sleep(5)
    driver.quit()


function_for_math()
