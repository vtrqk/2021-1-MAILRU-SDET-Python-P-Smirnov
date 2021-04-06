import pytest
import time
from ui import locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

CLICK_RETRY = 5


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find_paramitrize(self, variable, title):
        self.login()
        temp_var = (locators.MenuLocs.PARAMITRIZE_VAR[0],
                    locators.MenuLocs.PARAMITRIZE_VAR[1].format(variable))
        self.click(temp_var)
        time.sleep(2)
        assert title in self.driver.title

    def clear_to_send(self, elem, key):
        elem.clear()
        elem.send_keys(key)

    def fill_profile(self):
        self.login()
        self.click(locators.ProfileLocs.PROFILE_BUTTON)
        elem = self.find(locators.ProfileLocs.NAME_FIELD)
        self.clear_to_send(elem, 'pvl')
        elem = self.find(locators.ProfileLocs.PHONE_FIELD)
        self.clear_to_send(elem, '123456')
        elem = self.find(locators.ProfileLocs.MAIL_FILED)
        self.clear_to_send(elem, 'test@mail.ru')
        self.click(locators.ProfileLocs.SUBMIT_BUTTON)
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        elem = self.find(locators.ProfileLocs.NAME_FIELD).get_attribute('value')
        assert 'pvl' == elem
        elem = self.find(locators.ProfileLocs.MAIL_FILED).get_attribute('value')
        assert 'test@mail.ru' == elem
        elem = self.find(locators.ProfileLocs.PHONE_FIELD).get_attribute('value')
        assert '123456' == elem

    def login(self):
        self.click(locators.LoginLocs.ENTER_BUTTON)
        elem = self.find(locators.LoginLocs.LOGIN_FIELD)
        self.clear_to_send(elem, 'another.acc@mail.ru')
        elem = self.find(locators.LoginLocs.PASS_FIELD)
        self.clear_to_send(elem, 'ytr123qwe')
        self.click(locators.LoginLocs.LOGIN_BUTTON)

    def logout(self):
        self.login()
        self.click(locators.MenuLocs.MENU_EXIT)
        time.sleep(1)
        self.click(locators.MenuLocs.EXIT_BUTTON)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
