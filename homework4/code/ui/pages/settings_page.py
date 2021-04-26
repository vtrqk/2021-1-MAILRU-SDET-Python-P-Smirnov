from ui.locators.settings_page_locators import SettingsPageLocators
from ui.pages.about_page import AboutPage
from ui.pages.base_page import BasePage
from ui.pages.source_news_page import SourceNewsPage


class SettingsPage(BasePage):
    locators = SettingsPageLocators()

    def go_to_source_news(self):
        self.swipe_to_element(locator=self.locators.NEWS_BUTTON, max_swipes=5)
        self.click(locator=self.locators.NEWS_BUTTON)
        return SourceNewsPage(self.driver, self.config)

    def go_to_about_page(self):
        self.swipe_to_element(locator=self.locators.ABOUT_BUTTON, max_swipes=5)
        self.click(locator=self.locators.ABOUT_BUTTON)
        return AboutPage(self.driver, self.config)
