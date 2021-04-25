import allure

from selenium.common.exceptions import ElementNotInteractableException

from ui.pages.base_page import BasePage
from ui.locators.segments_locators import SegmentsLocators
from ui.pages.segments_new_page import SegmentsNewPage


class SegmentsPage(BasePage):
    locators = SegmentsLocators()

    @allure.step('Going to page of creating segment')
    def go_to_segments_new(self):

        try:
            self.click(locator=self.locators.CREATE_BUTTON_FIRST)
        except ElementNotInteractableException:
            self.click(locator=self.locators.CREATE_BUTTON_SECOND)

        return SegmentsNewPage(driver=self.driver)

    def initial_and_create(self, name):
        segments_new_page = self.go_to_segments_new()
        segments_new_page.create_segment(name)

    def check_segment(self, name):
        temp_var = (self.locators.SEGMENT_NAME[0], self.locators.SEGMENT_NAME[1].format(name))
        elem = self.find(temp_var)
        assert name in elem.text

    @allure.step('Deleting segment with name {name}')
    def delete_segment(self, name):
        temp_var = (self.locators.ID_CHECKBOX[0], self.locators.ID_CHECKBOX[1].format(name))
        self.click(locator=temp_var)
        self.click(locator=self.locators.ACTION_BUTTON)
        self.click(locator=self.locators.DELETE_BUTTON)
        self.driver.refresh()
