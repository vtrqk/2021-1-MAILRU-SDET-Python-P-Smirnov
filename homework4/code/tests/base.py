import pytest

from _pytest.fixtures import FixtureRequest
from ui.pages.main_page import MainPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.repo_root = request.getfixturevalue('repo_root')
        self.main_page : MainPage = request.getfixturevalue('get_main_page')