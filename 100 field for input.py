from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
driver.get('http://suninjuly.github.io/huge_form.html')
def input_all_field():
    all_field = driver.find_elements(By.CSS_SELECTOR, 'input')
    for field in all_field:
        field.send_keys('Text field')
    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    time.sleep(7)
    driver.quit()

input_all_field()