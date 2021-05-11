from tests.base import MySQLBase
from mysql.models import FavoriteRequests, LargestReq, TopUsers


class TestFavorite(MySQLBase):
    def test(self):
        request = self.get_from_sql(FavoriteRequests)
        assert len(request) == 10


class TestLargest(MySQLBase):
    def test(self):
        requests = self.get_from_sql(LargestReq)
        assert  len(requests) == 5


class TestTopUsers(MySQLBase):
    def test(self):
        requests = self.get_from_sql(TopUsers)
        assert len(requests) == 5