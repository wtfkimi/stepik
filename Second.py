from selenium import webdriver

from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')

driver.get('http://suninjuly.github.io/simple_form_find_task.html')

s = driver.find_element(By.CSS_SELECTOR, 'button.btn')

s.click()

time.sleep(3)

driver.quit()