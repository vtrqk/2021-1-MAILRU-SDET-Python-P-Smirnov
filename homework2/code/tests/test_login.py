import allure
import pytest
import time

from tests.base_case import BaseCase


class TestLogin(BaseCase):

    authorize = False

    @allure.epic('Test username')
    @pytest.mark.negative_username
    def test_email(self):
        login_page = self.main_page.go_to_login()
        login_page.login('sdasdasd', 'asd1231')
        assert "Введите email или телефон" in self.driver.page_source

    @allure.epic('Test password')
    @pytest.mark.negative_password
    def test_password(self):
        login_page = self.main_page.go_to_login()
        login_page.login('another.acc@mail.ru', '12312qwe')
        assert "Login" in self.driver.title


