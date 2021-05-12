from ui.locators.source_news_locators import SourceNewsLocators
from ui.pages.base_page import BasePage


class SourceNewsPage(BasePage):

    localors = SourceNewsLocators()

    def apply_news(self):
        self.click(locator=self.localors.NAME_NEWS_BUTT0N)

        assert self.find(locator=self.localors.SELECT_NEWS_BUTTON).get_attribute("enabled")

