import pytest

from utils.htttp_socket_client import Client


@pytest.fixture
def get_client():
    return Client()