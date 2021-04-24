import logging

from ui.locators.main_locators import MainLocators
from utils.decorators import wait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

logger = logging.getLogger('test')


class BasePage(object):

    locators = MainLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, err=NoSuchElementException):
        return wait(self.driver.find_element, error=err, by=locator[0], value=locator[1])

    def click(self, locator, err=ElementClickInterceptedException):
        elem = self.find(locator=locator)
        self.scroll_to(elem)
        logger.info(f'Clicking on {locator}...')
        wait(elem.click, error=err)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    @staticmethod
    def clear_to_send(elem, key):
        elem.clear()
        elem.send_keys(key)


