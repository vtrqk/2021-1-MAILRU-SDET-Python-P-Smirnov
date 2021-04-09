import allure

from ui.pages.base_page import BasePage
from ui.locators.dashboard_locators import DashBoardLocators
from ui.pages.segments_page import SegmentsPage
from ui.pages.campaign_new_page import CampaignNewPage


class DashBoardPage(BasePage):
    locators = DashBoardLocators()

    @allure.step('Going to segments')
    def go_to_segments(self):
        self.click(locator=self.locators.SEGMENTS_BUTTON)
        return SegmentsPage(driver=self.driver)

    @allure.step('Going to campaign_new')
    def go_to_campaign_new(self):
        self.click(locator=self.locators.NEW_CAMPAIGN_BUTTON)
        return CampaignNewPage(driver=self.driver)

    def check_campaign(self, name):
        temp_var = (self.locators.CHECK_COMPANY[0], self.locators.CHECK_COMPANY[1].format(name))
        elem = self.find(temp_var)
        assert name in elem.text

    def delete_campaign(self):
        self.click(locator=self.locators.ID_CHECKBOX)
        self.click(locator=self.locators.ACTION_BUTTON)
        self.click(locator=self.locators.DELETE_COMPANY_BUTTON)
