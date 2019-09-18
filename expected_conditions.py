from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')


def link():
    driver.get('http://suninjuly.github.io/wait2.html')

def code():
    link()
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'verify'))
        )
    button.click()
    message = driver.find_element(By.ID, 'verify_message')
    assert 'successful' in message.text



code()
driver.quit()