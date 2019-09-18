from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
from selenium.webdriver.support.ui import Select
import time

def link():
    driver.get('http://suninjuly.github.io/selects1.html')


def sum_numbers():
    link()
    num1 = driver.find_element(By.CSS_SELECTOR, 'span#num1.nowrap').text
    num2 = driver.find_element(By.CSS_SELECTOR, 'span#num2.nowrap').text
    summa = str(str(int(num1) + int(num2)))
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    otvet = select.select_by_visible_text('{}'.format(summa))
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    submit_button.click()
    time.sleep(6)

sum_numbers()
driver.quit()