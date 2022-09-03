
from page_objects.shared_objects import SharedObjects

class SharedMethods(object):

    def __init__(self, driver):
        self.driver = driver
        self.so = SharedObjects(driver)

    def skip_tour(self):
        self.so.skip_tour_button().click()










