from selenium.webdriver.common.by import By


class SharedObjects(object):

    def __init__(self, driver):
        self.driver = driver

    def skip_tour_button(self):
        return self.driver.find_element(By.XPATH, '//button[@data-qe="skip-tour-button"]')






