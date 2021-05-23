from tests.base import MySQLBase
from mysql.models import FavoriteRequests, LargestReq, TopUsers


class TestFavorite(MySQLBase):
    def prepare(self):
        self.mysql_builder.create_favorite_req()

    def test(self):
        request = self.get_from_sql(FavoriteRequests)
        assert len(request) == 10


class TestLargest(MySQLBase):
    def prepare(self):
        self.mysql_builder.create_largest_requests()

    def test(self):
        requests = self.get_from_sql(LargestReq)
        assert len(requests) == 5


class TestTopUsers(MySQLBase):
    def prepare(self):
        self.mysql_builder.create_top_users()

    def test(self):
        requests = self.get_from_sql(TopUsers)
        assert len(requests) == 5