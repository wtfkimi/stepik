from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
import time


def link():
    driver.get('https://SunInJuly.github.io/execute_script.html')

def scroll_to_button():
    link()
    button = driver.find_element(By.TAG_NAME, 'button')
    driver.execute_script('return arguments[0].scrollIntoView(true)', button)
    button.click()


scroll_to_button()
time.sleep(3)
driver.quit()
