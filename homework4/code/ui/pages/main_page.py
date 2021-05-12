from ui.locators.main_page_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.settings_page import SettingsPage


class MainPage(BasePage):

    locators = MainPageLocators()

    def go_to_settings(self):
        self.click(locator=self.locators.SETTINGS_BUTTON)
        return SettingsPage(self.driver, self.config)

    def send_text_to_search(self, word_to_search):
        self.click(locator=self.locators.KEYBOARD_BUTTON)
        self.find(locator=self.locators.INPUT_TEXT_FIELD).send_keys(word_to_search)
        self.click(locator=self.locators.INPUT_TEXT_BUTTON)

    def check_serve_news(self, name_news, word_to_search):
        self.send_text_to_search(word_to_search=word_to_search)
        self.driver.hide_keyboard()
        temp_var = (self.locators.NAME_NEWS_FIELD[0], self.locators.NAME_NEWS_FIELD[1].format(name_news))
        assert name_news == self.find(temp_var).text

    def check_search_results(self, check_text):
        assert check_text in self.find(locator=self.locators.FACT_CARD_FIELD).text

    def check_population(self, population):
        self.swipe_element_lo_left(locator=self.locators.SCROLL_TO_BUTTON, max_swipes=5)
        self.click(locator=self.locators.POPULATION_BUTTON)
        assert population in self.find(locator=self.locators.POPULATION_FIELD).text

    def send_expression_and_check_result(self, expression, result):
        self.send_text_to_search(word_to_search=expression)
        temp_var = (self.locators.RESULT_OF_MATH_FIELD[0], self.locators.RESULT_OF_MATH_FIELD[1].format(result))

        assert result == self.find(locator=temp_var).text