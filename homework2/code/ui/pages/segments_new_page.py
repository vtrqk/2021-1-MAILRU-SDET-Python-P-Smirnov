
from ui.pages.base_page import BasePage
from ui.locators.segments_new_locators import SegmentsNewLocators


class SegmentsNewPage(BasePage):

    locators = SegmentsNewLocators()

    def create_segment(self):
        self.click(locator=self.locators.PARAM_CHECKBOX)
        self.click(locator=self.locators.ADD_BUTTON)
        self.click(locator=self.locators.CREATE_BUTTON)
