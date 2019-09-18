from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\webdriver\chromedriver.exe')

def link():
    driver.get('http://suninjuly.github.io/math.html')

def check_atribute():
    link()
    people_radio = driver.find_element(By.ID, 'peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('Value of people radio', people_checked)
    assert people_checked is not None, 'People radio is not selected by default'
    assert people_checked == 'true', 'People radio is not selected by default'

def check_another_atribute():
    link()
    robots_radio = driver.find_element(By.ID, 'robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('Atribut robots_radio = : ', robots_checked)
    assert robots_checked is None


check_another_atribute()
check_atribute()
driver.quit()


