import os

import allure
import pytest

from ui.pages.main_page import MainPage
from ui.pages.dashboard_page import DashBoardPage


USER_NAME = "another.acc@mail.ru"
PASSWORD = "ytr123qwe"


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture(scope='function')
def file_path(repo_root):
    return os.path.join(repo_root, 'resources', 'test_img.png')


@pytest.fixture
def auto_login(driver, main_page):
    login_page = main_page.go_to_login()
    login_page.login(user=USER_NAME, password=PASSWORD)
    return DashBoardPage(driver=driver)


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)