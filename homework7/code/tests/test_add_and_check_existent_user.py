import json

from tests.base_add_and_check_existent import BaseAddAndCheckExistent


class TestAddAndCheckExistentUser(BaseAddAndCheckExistent):

    def test_add_get_user(self):
        self.create_user()

    def test_get_non_existent_user(self):
        random_name = self.create_name()
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=random_name)
        assert f'User name {random_name} not found' == json.loads(resp[-1])

    def test_add_existent_user(self):
        new_name = self.create_name()
        self.create_user()
        self.custom_request.do_post(url=f'{self.base_app_url}/add_user', data={'name': new_name})
        resp = self.custom_request.do_post(url=f'{self.base_app_url}/add_user', data={'name': new_name})
        assert f'User name {new_name} already exists' in json.loads(resp[-1])
















