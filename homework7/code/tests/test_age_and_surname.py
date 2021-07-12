import json
import settings

from tests.base_age_and_surname import BaseAgeAndSurname


class TestAgeAndSurname(BaseAgeAndSurname):

    def test_get_age(self):
        resp = self.create_user()

        assert isinstance(json.loads(resp[-1])['age'], int)
        assert 0 <= json.loads(resp[-1])['age'] <= 100

    def test_has_surname(self):
        self.create_user_with_surname()

    def test_update_surname(self):
        name = self.create_user_with_surname()
        new_surname = self.create_surname()
        self.custom_request.do_post(url=self.get_base_put_url() + name, data={'surname': new_surname},
                                    host=settings.MOCK_HOST, port=settings.MOCK_PORT, method='PUT')
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=name)

        assert json.loads(resp[-1])['surname'] == new_surname

    def test_delete_surname(self):
        name = self.create_user_with_surname()
        self.custom_request.do_post(url=self.get_base_delete_url() + name, data=None,
                                    host=settings.MOCK_HOST, port=settings.MOCK_PORT, method='DELETE')

        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=name)
        assert json.loads(resp[-1])['surname'] is None

    def test_has_not_surname(self):
        resp = self.create_user()

        assert json.loads(resp[-1])['surname'] is None
