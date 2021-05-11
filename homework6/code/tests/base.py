import pytest


class MySQLBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client

    def get_from_sql(self, name_model):
        result = self.mysql.session.query(name_model).all()
        return result
