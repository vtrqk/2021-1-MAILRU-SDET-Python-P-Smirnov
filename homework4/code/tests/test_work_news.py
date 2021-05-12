import pytest
from tests.base import BaseCase


class TestNews(BaseCase):

    @pytest.mark.AndroidUI_Check_News
    def test_check_work_news(self):
        settings_page = self.main_page.go_to_settings()
        source_page = settings_page.go_to_source_news()
        source_page.apply_news()
        self.driver.back()
        self.driver.back()
        self.main_page.check_serve_news(name_news='Вести ФМ', word_to_search='News')