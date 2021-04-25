import allure

from ui.pages.base_page import BasePage
from ui.locators.segments_new_locators import SegmentsNewLocators


class SegmentsNewPage(BasePage):

    locators = SegmentsNewLocators()

    @allure.step('Creating segment with name {name}')
    def create_segment(self, name):
        self.click(locator=self.locators.PARAM_CHECKBOX)
        self.click(locator=self.locators.ADD_BUTTON)
        elem = self.find(locator=self.locators.NEW_NAME_FIELD)
        self.clear_to_send(elem=elem, key=name)
        self.click(locator=self.locators.CREATE_BUTTON)
