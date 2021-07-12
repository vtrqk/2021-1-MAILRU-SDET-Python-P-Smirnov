import json

import settings
from mock.flask_mock import SURNAME_DATA
from tests.base import BaseCase


class BaseAgeAndSurname(BaseCase):

    @staticmethod
    def get_base_put_url():
        return f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/update_surname/'

    @staticmethod
    def get_base_delete_url():
        return f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/delete_surname/'

    def create_user_with_surname(self):
        new_surname = self.create_surname()
        new_name = self.create_name()
        SURNAME_DATA[new_name] = new_surname
        self.custom_request.do_post(url=f'{self.base_app_url}/add_user', data={'name': new_name})
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=new_name)

        assert json.loads(resp[-1])['surname'] == new_surname

        return new_name
