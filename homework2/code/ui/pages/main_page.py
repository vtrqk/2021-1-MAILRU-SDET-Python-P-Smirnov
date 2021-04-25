import allure

from ui.locators.main_locators import MainLocators
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


class MainPage(BasePage):
    locators = MainLocators()

    @allure.step('Going to login')
    def go_to_login(self):
        self.click(locator=self.locators.ENTER_BUTTON)

        return LoginPage(driver=self.driver)
