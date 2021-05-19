import json
import settings

from mock.my_mock import JOB_DATA
from tests.base import BaseCase


class BaseMyMock(BaseCase):

    @staticmethod
    def get_base_put_url():
        return f'http://{settings.MY_MOCK_HOST}:{settings.MY_MOCK_PORT}/update_job/'

    def create_user_with_job(self):
        new_job = self.create_job()
        new_name = self.create_name()
        JOB_DATA[new_name] = new_job
        self.custom_request.do_post(url=f'{self.base_app_url}/add_user', data={'name': new_name})
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=new_name)
        assert json.loads(resp[-1])['job'] == new_job
        return new_name
