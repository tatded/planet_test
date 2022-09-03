from selenium.webdriver.common.by import By

class ExplorerPageObjects(object):

    def __init__(self, driver):
        self.driver = driver

    def search_icon(self):
        return self.driver.find_element(By.XPATH, '//button[@data-qe="toggle-search"]')

    def saved_searches_icon(self):
        return self.driver.find_element(By.XPATH, '//button[@data-qe="toggle-saved-searches"]')

    def saved_search_titles(self):
        return self.driver.find_elements(By.XPATH, '//h6[@data-qe="search-list-item-title"]')

    def saved_search_by_title(self, search_title):
        return self.driver.find_element(By.XPATH, '//h6[@data-qe="search-list-item-title"][text()="'+search_title+'"]')

    def cadence(self, cadence):
        return self.driver.find_element(By.XPATH, '//button/span[text()="'+cadence+'"]')

    def search_input_field(self):
        return self.driver.find_element(By.XPATH, '//input[@data-qe="search-input"]')

    def input_suggestion(self):
        return self.driver.find_element(By.XPATH, '//ul[@id=":r16:-listbox"]/div[@data-option-index="0"]')

    def filter_button(self):
        return self.driver.find_element(By.XPATH, '//button[@data-qe="filters-button"]')

    def dates_button(self):
        return self.driver.find_element(By.XPATH, '//button[@data-qe="set-date-range-button"]')

    def save_search_button(self):
        return self.driver.find_element(By.XPATH, '//button[@data-qe="click-save-search-button"]')

    def filter_option(self, option):
        return self.driver.find_element(By.XPATH, '//span[contains(text(), "' + option + '")]')

    def clear_all_filters_button(self):
        return self.driver.find_element(By.XPATH, '//button[text()="Clear All"]')

    def apply_filters_button(self):
        return self.driver.find_element(By.XPATH, '//button[@data-qe="apply-filters-button"]')










