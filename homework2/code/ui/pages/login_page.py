from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginLocators


class LoginPage(BasePage):

    locators = LoginLocators()

    def login(self, user, password):

        elem = self.find(locator=self.locators.LOGIN_FIELD)
        self.clear_to_send(elem, user)
        elem = self.find(locator=self.locators.PASS_FIELD)
        self.clear_to_send(elem, password)
        self.click(locator=self.locators.LOGIN_BUTTON)
