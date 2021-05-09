import pytest

from api.client import ApiClient


@pytest.fixture()
def api_client():
    return ApiClient()
