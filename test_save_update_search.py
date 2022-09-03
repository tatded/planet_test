import logging
from page_methods.explorer_search_methods import ExplorerPageSearchMethods
from page_methods.save_search_methods import SaveSearchMethods
from filter_options import *


class TestSearch:

    def test_default_search_and_save(self, driver, signin):
        epsm = ExplorerPageSearchMethods(driver)
        ssm = SaveSearchMethods(driver)
        location = 'San Francisco, CA'
        default_filter_options = [ImageryType.SkySatCollect, ImageryType.PSScene]
        logging.info(f'Searching for location: {location}')
        epsm.default_search(location)
        logging.info(f'Saving "{location}" search with default search options')
        ssm.save_search(location, default_filter_options)
        logging.info(f'Validating "{location}" search is present in saved searches')
        epsm.validate_search_saved(location)

    def test_update_saved_search(self, driver, signin):
        epsm = ExplorerPageSearchMethods(driver)
        ssm = SaveSearchMethods(driver)
        search_title = 'San Francisco, CA'
        new_search_title = 'Updated SF search'
        default_filter_options = [ImageryType.SkySatCollect, ImageryType.PSScene]
        new_filter_options = [ImageryType.SkySatScene, ImageryType.PSOrthoTile]
        logging.info('Modifying saved search with new search filter options')
        epsm.edit_saved_search(search_title, new_filter_options)
        logging.info(f'Saving updated search with a new title "{new_search_title}"')
        ssm.save_search(new_search_title, default_filter_options+new_filter_options, is_update=True)
        logging.info(f'Validating "{new_search_title}" search is present in saved searches')
        epsm.validate_search_saved(new_search_title)
