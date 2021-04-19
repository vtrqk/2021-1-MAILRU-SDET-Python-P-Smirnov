import pytest

from api.client import ApiClient


USER_NAME = 'another.acc@mail.ru'
PASSWORD = 'ytr123qwe'


@pytest.fixture()
def api_client():
    return ApiClient()


@pytest.fixture(scope='session')
def cookies():
    api_client = ApiClient()
    api_client.post_login(USER_NAME, PASSWORD)
    api_client.get_csrf_token()

    cookies_list = []
    for cookie in api_client.session.cookies:
        cookie_dict = {'domain': cookie.domain, 'name': cookie.name, 'value': cookie.value, 'secure': cookie.secure}
        cookies_list.append(cookie_dict)

    return cookies_list
