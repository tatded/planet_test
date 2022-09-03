from selenium.webdriver.common.by import By

class LoginPageObjects(object):

    def __init__(self, driver):
        self.driver = driver

    def email_address_input(self):
        return self.driver.find_element(By.ID, 'idp-discovery-username')

    def signin_next_button(self):
        return self.driver.find_element(By.ID, 'idp-discovery-submit')

    def password_input(self):
        return self.driver.find_element(By.ID, 'okta-signin-password')

    def signin_button(self):
        return self.driver.find_element(By.ID, 'okta-signin-submit')



