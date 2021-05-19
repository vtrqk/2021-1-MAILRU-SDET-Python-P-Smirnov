import json

import requests

from tests.base import BaseCase
from mock.flask_mock import SURNAME_DATA
from tests.base_age_and_surname import BaseAgeAndSurname


class TestAgeAndSurname(BaseAgeAndSurname):

    def test_get_age(self):

        resp = self.create_user()

        assert isinstance(json.loads(resp[-1])['age'], int)
        assert 0 <= json.loads(resp[-1])['age'] <= 100

    def test_has_surname(self):
        self.create_user_with_surname()

    def test_has_not_surname(self):

        resp = self.create_user()

        assert json.loads(resp[-1])['surname'] == None

