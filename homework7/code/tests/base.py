import pytest
import settings

from _pytest.fixtures import FixtureRequest

from utils.builder import Builder
from utils.htttp_socket_client import Client


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request: FixtureRequest):

        self.custom_request: Client = request.getfixturevalue('get_client')
        self.builder = Builder()
        self.base_app_url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'

    def create_name(self):
        user_name = self.builder.create_name()
        return user_name.name

    def create_surname(self):
        user_surname = self.builder.create_surname()
        return user_surname.surname

    def create_job(self):
        user_job = self.builder.create_job()

        return user_job.job

    def create_user(self):
        new_name = self.create_name()
        self.custom_request.do_post(url=f'{self.base_app_url}/add_user', data={'name': new_name})
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=new_name)
        return resp
