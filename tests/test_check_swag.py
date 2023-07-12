from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_find_icon():
    driver = webdriver.Chrome()
    driver.get("http://saucedemo.com/")
    # icon = 'div.login_logo' #решение1
    #
    # if icon == 'div.login_logo':
    #     return True
    # return False

    try:
        driver.find_element(By.CSS_SELECTOR, 'div.login_logo') #решение2
    except NoSuchElementException:
        assert False
    assert True

def test_find_username():
    driver = webdriver.Chrome()
    driver.get("http://saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, '#user-name')
    except NoSuchElementException:
        assert False
    assert True

def test_find_password():
    driver = webdriver.Chrome()
    driver.get("http://saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, '#password')
    except NoSuchElementException:
        assert False
    assert True
