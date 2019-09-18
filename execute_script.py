from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')


driver.execute_script("document.title='Script executing'; alert('Robot\'s at work');")

time.sleep(3)
driver.quit()