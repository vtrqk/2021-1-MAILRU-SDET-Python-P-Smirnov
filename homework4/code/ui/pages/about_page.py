from ui.locators.about_page_locators import AboutPageLocators
from ui.pages.base_page import BasePage


class AboutPage(BasePage):
    locators = AboutPageLocators()

    def check_version(self, version_apk):
        version_in_app = self.find(locator=self.locators.ABOUT_VERSION_FIELD).text
        assert version_apk in version_in_app

    def check_copyright(self, name_trademark):
        app_trademark = self.find(locator=self.locators.COPYRIGHT_FIELD).text
        assert name_trademark in app_trademark
