import json

from mock.flask_mock import SURNAME_DATA
from tests.base import BaseCase


class BaseAgeAndSurname(BaseCase):

    def create_user_with_surname(self):
        new_surname = self.create_surname()
        new_name = self.create_name()
        SURNAME_DATA[new_surname] = new_surname
        self.custom_request.do_post(url=f'{self.base_app_url}/add_user', data={'name': new_name})
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=new_name)

        assert json.loads(resp[-1])['surname'] == new_surname