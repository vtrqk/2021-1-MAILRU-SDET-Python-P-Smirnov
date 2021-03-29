import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(executable_path='P:\\python\\chromedriver', options=options)
    browser.get('https://target.my.com')
    browser.set_window_size(1400, 1000)
    yield browser
    browser.close()
