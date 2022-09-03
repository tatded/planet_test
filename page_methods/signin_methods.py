import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_objects.login_objects import LoginPageObjects


class LoginPageMethods(object):

    def __init__(self, driver):
        self.driver = driver
        self.lpm = LoginPageObjects(driver)

    def input_username(self, email):
        usr_input = self.lpm.email_address_input()
        usr_input.clear()
        usr_input.send_keys(email)

    def input_password(self, password):
        pwd_input = self.lpm.password_input()
        pwd_input.clear()
        pwd_input.send_keys(password)

    def click_next_button(self):
        self.lpm.signin_next_button().click()

    def click_signin_button(self):
        self.lpm.signin_button().click()

    def planet_signin(self, email, password):
        self.input_username(email)
        self.click_next_button()
        self.input_password(password)
        self.click_signin_button()


