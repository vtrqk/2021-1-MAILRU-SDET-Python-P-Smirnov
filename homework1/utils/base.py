import pytest
import locators

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

    def search(self, variable):
        TEMP_VAR = (By.XPATH, f"//a[contains(@class, '{variable}')]")
        self.click(TEMP_VAR)

    def info(self, flag=False):
        self.register()
        self.click(locators.MenuLocs.PROFILE_BUTTON)
        elem = self.find(locators.MenuLocs.NAME_FIELD)
        elem.clear()
        elem.send_keys('pvl')
        elem = self.find(locators.ProfileLocs.PHONE_FIELD)
        elem.clear()
        elem.send_keys('123456')
        elem = self.find(locators.MenuLocs.MAIL_FILED)
        elem.clear()
        elem.send_keys('test@mail.ru')
        self.click(locators.MenuLocs.SUBMIT_BUTTON)
        self.driver.refresh()
        if(flag):
            return self.driver.page_source

    def register(self, flag=False):
        self.click(locators.LoginLocs.ENTER_BUTTON)
        elem = self.find(locators.LoginLocs.LOGIN_FIELD)
        elem.clear()
        elem.send_keys('another.acc@mail.ru')
        elem = self.find(locators.LoginLocs.PASS_FIELD)
        elem.clear()
        elem.send_keys('ytr123qwe')
        self.click(locators.LoginLocs.LOGIN_BUTTON)
        if(flag):
            return self.driver.title

    def logout(self, flag=False):
        self.click(locators.MenuLocs.MENU_EXIT)
        self.click(locators.MenuLocs.EXIT_BUTTON)
        if (flag):
            return self.driver.title

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