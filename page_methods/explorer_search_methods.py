from page_objects.explorer_objects import ExplorerPageObjects

class ExplorerPageSearchMethods(object):

    def __init__(self, driver):
        self.driver = driver
        self.epo = ExplorerPageObjects(driver)

    def click_saved_searches_icon(self):
        self.epo.saved_searches_icon().click()

    def input_search(self, location):
        search_input = self.epo.search_input_field()
        search_input.clear()
        search_input.send_keys(location)
        search_input.click()
        self.epo.input_suggestion().click()

    def click_filters_button(self):
        self.epo.filter_button().click()

    def select_filter_option(self, option):
        self.epo.filter_option(option).click()

    def click_apply_filters_button(self):
        self.epo.apply_filters_button().click()

    def click_save_search_button(self):
        self.epo.save_search_button().click()

    def default_search(self, location):
        self.input_search(location)
        self.click_save_search_button()

    def get_saved_search_titles(self):
        for saved_search in self.epo.saved_search_titles():
            search_titles = [saved_search.text]
            return search_titles

    def validate_search_saved(self, search_name):
        self.click_saved_searches_icon()
        search_titles = self.get_saved_search_titles()
        assert search_name in search_titles

    def edit_saved_search(self, search_name, new_search_options):
        self.click_saved_searches_icon()
        self.epo.saved_search_by_title(search_name).click()
        self.click_filters_button()
        for f_option in new_search_options:
            self.select_filter_option(f_option)
        self.click_apply_filters_button()
        self.click_save_search_button()









