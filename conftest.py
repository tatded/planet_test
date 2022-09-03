import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from credentials import LoginCredentials
from page_methods.signin_methods import LoginPageMethods
from page_methods.shared_methods import SharedMethods


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.planet.com/login')
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def signin(driver):
    """Login and navigate to the Explorer page"""
    lpm = LoginPageMethods(driver)
    lpm.planet_signin(email=LoginCredentials.EMAIL, password=LoginCredentials.PASSWORD)
    driver.get('http://www.planet.com/explorer/')

    sm = SharedMethods(driver)
    sm.skip_tour()
    yield signin
