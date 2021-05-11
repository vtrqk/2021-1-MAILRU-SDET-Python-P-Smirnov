import pytest

from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_PYTHON')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_PYTHON')
        mysql_client.recreate_db()

        mysql_client.connect()
        mysql_client.create_all_requests()
        mysql_client.create_favorite_req()
        mysql_client.create_largest_req()
        mysql_client.create_top_users()
        mysql_client.create_post_and_get()

        mysql_client.connection.close()