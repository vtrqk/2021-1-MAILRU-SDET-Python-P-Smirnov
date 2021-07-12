import json

from tests.base import BaseCase


class BaseAddAndCheckExistent(BaseCase):

    def create_user(self):
        new_name = self.create_name()
        resp = self.custom_request.do_post(url=f'{self.base_app_url}/add_user', data={'name': new_name})
        user_id_from_add = json.loads(resp[-1])['user_id']
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=new_name)
        user_id_from_get = json.loads(resp[-1])['user_id']

        assert user_id_from_add == user_id_from_get
