from tests.base import MySQLBase
from mysql.models import PostAndGet, AllRequests


class TestPostAndGet(MySQLBase):
    def prepare(self):
        self.mysql_builder.create_post_and_get()

    def test(self):
        request = self.get_from_sql(PostAndGet)
        assert len(request) == 1


class TestAllRequests(MySQLBase):
    def prepare(self):
        self.mysql_builder.create_all_requests()

    def test(self):
        request = self.get_from_sql(AllRequests)
        assert len(request) == 1