import pytest

from ui.capability import capability_select
from appium import webdriver
from ui.pages.main_page import MainPage


@pytest.fixture
def get_main_page(driver, config):
    return MainPage(driver=driver, config=config)


def get_driver(appium_url):
    desired_caps = capability_select()
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    return driver


@pytest.fixture(scope='function')
def driver(config):
    appium_url = config['appium']
    browser = get_driver(appium_url)
    yield browser
    browser.quit()
