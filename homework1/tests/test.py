import pytest
from utils.base import BaseCase


class TestReg(BaseCase):

    @pytest.mark.login
    def test_login(self):
        assert "Вход" not in self.register(True)
        self.logout()

    @pytest.mark.logout
    def test_logout(self):
        self.register()
        assert "Рекламная платформа myTarget" in self.logout(True)

    @pytest.mark.info
    def test_info(self):
        assert 'pvl' in self.info(True)
        self.logout()

    @pytest.mark.menu
    @pytest.mark.parametrize("srch, test", [('3y1hDo', 'Список сегментов'),
        ('3EnTS8', 'Список фидов')])
    def test_menu(self, srch, test):
        self.register()
        self.search(srch)
        assert test in self.driver.title
        self.logout()
