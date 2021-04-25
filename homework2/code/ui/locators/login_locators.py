from selenium.webdriver.common.by import By
from ui.locators.main_locators import MainLocators


class LoginLocators():

    LOGIN_FIELD = (By.XPATH, "//input[contains(@name, 'email')]")
    PASS_FIELD = (By.XPATH, "//input[contains(@name, 'pass')]")
    LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
