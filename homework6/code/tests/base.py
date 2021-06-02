import pytest

from  mysql.builder import MySQLBuilder


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()

    def get_from_sql(self, name_model):
        result = self.mysql.session.query(name_model).all()
        return result
