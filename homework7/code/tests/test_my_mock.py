import json

from tests.bese_my_mock import BaseMyMock


class TestMyMock(BaseMyMock):

    def test_has_job(self):
        self.create_user_with_job()

    def test_has_not_job(self):
        resp = self.create_user()

        assert json.loads(resp[-1])['job'] is None

    def test_update_job(self):
        new_name = self.create_user_with_job()
        new_job = self.create_job()
        self.custom_request.do_post(self.get_base_put_url() + new_name, data={'job': new_job})
        resp = self.custom_request.do_get(url=f'{self.base_app_url}/get_user/', param=new_name)

        assert json.loads(resp[-1])['job'] == new_job
