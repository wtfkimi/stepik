from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
import math
import time

def link():
    driver.get('http://suninjuly.github.io/redirect_page.html?')


def switch_to_new_window():
    link()

    val = driver.find_element(By.XPATH, '//*[@id="input_value"]')
    value = val.text
    a = str(math.log(abs(12 * math.sin(int(value)))))

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(a)

    button_submit = driver.find_element(By.TAG_NAME, 'button').click()


    time.sleep(5)



switch_to_new_window()
driver.quit()