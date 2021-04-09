import allure
import pytest
from tests.base_case import BaseCase


class TestSegment(BaseCase):

    def initial_and_create(self):
        segments_page = self.dashboard_page.go_to_segments()
        segments_new_page = segments_page.go_to_segments_new()
        segments_new_page.create_segment()
        return segments_page

    @allure.story('Test new segment')
    @pytest.mark.create_segment
    def test_create_segment(self):
        with allure.step('Going to initial and create segments pages'):
            segments_page = self.initial_and_create()
        segments_page.check_segment("Новый аудиторный сегмент")
        segments_page.delete_segment()

    @allure.story('Test delete segment')
    @pytest.mark.delete_segment
    def test_delete_segment(self):
        with allure.step('Going to initial and create segments pages'):
            segments_page = self.initial_and_create()
        segments_page.delete_segment()
        assert "Новый аудиторный сегмент" not in self.driver.page_source
