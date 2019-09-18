from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
import math
import time

def link():
    driver.get('https://suninjuly.github.io/execute_script.html')



def execute_script():
    link()
    x = driver.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    input_value = x.text
    math_function = str(math.log(abs(12*math.sin(int(input_value)))))

    input_field = driver.find_element(By.ID, 'answer')
    input_field.send_keys(math_function)

    im_the_robot_box = driver.find_element(By.ID, 'robotCheckbox')
    im_the_robot_box.click()

    button = driver.find_element(By.TAG_NAME, 'button')
    driver.execute_script('return arguments[0].scrollIntoView(true)', button)

    robots_rule = driver.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    button.click()
    time.sleep(5)

execute_script()
driver.quit()


