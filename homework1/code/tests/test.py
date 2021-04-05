import pytest
from ui.base import BaseCase


class TestReg(BaseCase):

    @pytest.mark.login
    def test_login(self):
        self.login()
        assert 'Login' not in self.driver.title

    @pytest.mark.logout
    def test_logout(self):
        self.logout()
        assert "Рекламная платформа myTarget" in self.driver.title

    @pytest.mark.profile
    def test_profile(self):
        self.fill_profile()

    @pytest.mark.menu
    @pytest.mark.parametrize("find, title", [
                                 pytest.param('/segments', 'Список сегментов'),
                                 pytest.param('/tools', 'Список фидов')])
    def test_menu(self, find, title):
        self.find_paramitrize(find, title)
