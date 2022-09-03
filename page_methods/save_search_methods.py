from page_objects.save_search_objects import SaveSearchPageObjects
from selenium.webdriver.common.action_chains import ActionChains

class SaveSearchMethods(object):

    def __init__(self, driver):
        self.driver = driver
        self.sspo = SaveSearchPageObjects(driver)

    def click_save_search_button(self):
        self.sspo.save_search_button().click()

    def click_update_search_button(self):
        self.sspo.update_search_button().click()

    def click_save_as_new_search_button(self):
        self.sspo.save_as_new_search_button().click()

    def update_search_name(self, search_name):
        self.sspo.search_name_input().click()
        input_txt = self.sspo.search_name_input()
        actionChains = ActionChains(self.driver)
        actionChains.click(input_txt).click(input_txt).click(input_txt).perform()
        self.sspo.search_name_input().send_keys(search_name)

    def save_search(self, search_name, search_options, default=True, is_update=False, is_save_as_new=False):
        self.update_search_name(search_name)
        for option in search_options:
            assert option in self.sspo.satellite_constellations().text
        filters = self.sspo.filters()
        if default:
            for search_filter in filters:
                assert search_filter.text == 'Default'
        if is_update:
            self.click_update_search_button()
        elif is_save_as_new:
            self.click_save_as_new_search_button()
        else:
            self.click_save_search_button()



















