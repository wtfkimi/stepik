from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
driver.get('http://suninjuly.github.io/find_xpath_form')
def find_by_xpath():
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

    button = driver.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]')
    button.click()
    time.sleep(5)
    driver.quit()

find_by_xpath()
