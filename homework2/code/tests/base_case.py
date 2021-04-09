import logging
import pytest

from _pytest.fixtures import FixtureRequest
from ui.pages.dashboard_page import DashBoardPage
from ui.pages.main_page import MainPage

logger = logging.getLogger('test')


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger
        self.main_page: MainPage = request.getfixturevalue('main_page')

        if (self.authorize):
            logger.info(f'Authorize is starting...')
            self.dashboard_page: DashBoardPage = request.getfixturevalue('auto_login')
