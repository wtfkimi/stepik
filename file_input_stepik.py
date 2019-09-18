from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
import os
import time

def link():
    driver.get('http://suninjuly.github.io/file_input.html')

def input_file():
    link()

    first_name = driver.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    first_name.click()
    first_name.send_keys('Vyacheslav')

    second_name = driver.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    second_name.click()
    second_name.send_keys('Bondariev')

    email = driver.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    email.click()
    email.send_keys('rdy2qa@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    file = driver.find_element(By.ID, 'file')
    file.send_keys(file_path)

    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button_submit.click()
    time.sleep(7)

input_file()
driver.quit()
