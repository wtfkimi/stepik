from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')
driver.get('http://suninjuly.github.io/registration2.html')

def test_registration():
    first_name = driver.find_element(By.CSS_SELECTOR, 'input.form-control.first')
    first_name.click()
    first_name.send_keys('Vyacheslav')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input.form-control.second')
    if last_name == 'input.form-control.second':
        pass
    else:
        driver.quit()
        print('error in CSS_SELECTOR')
    last_name.click()
    last_name.send_keys('Bondariev')

    email = driver.find_element(By.CSS_SELECTOR, 'input.form-control.third')
    email.click()
    email.send_keys('573918824')
    time.sleep(3)

    button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()
    time.sleep(3)

    welcome_text_elt = driver.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(5)
    driver.quit()


