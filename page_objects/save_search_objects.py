from selenium.webdriver.common.by import By

class SaveSearchPageObjects(object):

    def __init__(self, driver):
        self.driver = driver

    def search_name_input(self):
        return self.driver.find_element(By.XPATH, '//div[@data-qe="save-search-name"]/div/input')

    def save_search_button(self):
        return self.driver.find_element(By.XPATH, '//button[@data-cy="dialog-save-search-button"]')

    def update_search_button(self):
        return self.driver.find_element(By.XPATH, '//button[text()="Update"]')

    def save_as_new_search_button(self):
        return self.driver.find_element(By.XPATH, '//button[text()="Save as new search"]')

    def satellite_constellations(self):
        return self.driver.find_element(By.XPATH, '//h6[text()="Satellite Constellations"]/following-sibling::span')

    def filters(self):
        return self.driver.find_elements(By.XPATH, '//table/tbody/tr/td[2]/span')













