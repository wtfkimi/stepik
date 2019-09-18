from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')

try:
    def click_to_link_complete_form():
        driver.get('http://suninjuly.github.io/find_link_text')
        encrypted_link = driver.find_element(By.LINK_TEXT, '224592')
        encrypted_link.click()

        name = driver.find_element(By.NAME, 'first_name')
        name.click()
        name.send_keys('Ivan')

        surname = driver.find_element(By.NAME, 'last_name')
        surname.click()
        surname.send_keys('Petrov')

        city = driver.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(3) > input')
        city.click()
        city.send_keys('Smolensk')

        country = driver.find_element(By.ID, 'country')
        country.click()
        country.send_keys('Russia')

        button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

    click_to_link_complete_form()

finally:
    time.sleep(10)
    driver.quit()

