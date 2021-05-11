from tests.base import MySQLBase
from mysql.models import PostAndGet, AllRequests


class TestPostAndGet(MySQLBase):
    def test(self):
        request = self.get_from_sql(PostAndGet)
        assert len(request) == 2


class TestAllRequests(MySQLBase):
    def test(self):
        request = self.get_from_sql(AllRequests)
        assert len(request) == 1