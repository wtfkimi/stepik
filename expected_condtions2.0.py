from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')

def link():
    driver.get('http://suninjuly.github.io/explicit_wait2.html')


def wait_when_house_100():
    link()

    element = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button = driver.find_element(By.ID, 'book')
    button.click()

    val = driver.find_element(By.ID, 'input_value')
    value = val.text

    functions = str(math.log(abs(12*math.sin(int(value)))))

    input_field = driver.find_element(By.ID, 'answer')
    input_field.send_keys(functions)

    button_submit = driver.find_element(By.ID, 'solve')
    button_submit.click()
    time.sleep(5)

wait_when_house_100()
driver.quit()
