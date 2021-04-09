import allure

from ui.pages.base_page import BasePage
from ui.locators.segments_locators import SegmentsLocators
from ui.pages.segments_new_page import SegmentsNewPage


class SegmentsPage(BasePage):
    locators = SegmentsLocators()

    @allure.step('Going to login')
    def go_to_segments_new(self):
        self.click(locator=self.locators.CREATE_BUTTON)
        return SegmentsNewPage(driver=self.driver)

    def check_segment(self, name):
        temp_var = (self.locators.SEGMENT_NAME[0], self.locators.SEGMENT_NAME[1].format(name))
        elem = self.find(temp_var)
        assert name in elem.text

    def delete_segment(self):
        self.click(locator=self.locators.ID_CHECKBOX)
        self.click(locator=self.locators.ACTION_BUTTON)
        self.click(locator=self.locators.DELETE_BUTTON)
        self.driver.refresh()


