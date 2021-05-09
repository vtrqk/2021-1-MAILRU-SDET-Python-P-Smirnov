import pytest

from utils.builder import Builder

USER_NAME = 'another.acc@mail.ru'
PASSWORD = 'ytr123qwe'


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.builder = Builder()
        self.api_client = api_client

        if self.authorize:
            api_client.post_login(user=USER_NAME, password=PASSWORD)
