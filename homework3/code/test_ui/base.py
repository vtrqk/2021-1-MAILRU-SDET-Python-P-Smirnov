import pytest
from _pytest.fixtures import FixtureRequest


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, api_client, request: FixtureRequest):
        self.driver = driver
        self.api_client = api_client

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
