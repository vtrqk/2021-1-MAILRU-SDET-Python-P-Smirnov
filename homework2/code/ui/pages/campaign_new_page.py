from ui.pages.base_page import BasePage
from ui.locators.campaign_new_locators import CampaignNewLocators

CAMPAIGN_LINK = 'https://vk.com/fanpapich'


class CampaignNewPage(BasePage):
    locators = CampaignNewLocators()

    def create_new_campaign(self, file_path):
        self.click(locator=self.locators.TRAFFIC_BUTTON)
        elem = self.find(locator=self.locators.LINK_FIELD)
        self.clear_to_send(elem, CAMPAIGN_LINK)
        self.click(locator=self.locators.TEASER_BUTTON)
        input_field = self.find(locator=self.locators.ADD_IMG_BUTTON)
        input_field.send_keys(file_path)
        elem = self.find(locator=self.locators.SAVE_IMG)
        elem.click()
        self.click(locator=self.locators.DELETE_IMG)
        self.click(locator=self.locators.APPLY_DELETE)
        elem = self.find(locator=self.locators.HEADER_FIELD)
        self.clear_to_send(elem, "Header")
        elem = self.find(locator=self.locators.DESCRIPTION_FIELD)
        self.clear_to_send(elem, "Some description")
        self.click(locator=self.locators.CREATE_COMPANY_BUTTON)
