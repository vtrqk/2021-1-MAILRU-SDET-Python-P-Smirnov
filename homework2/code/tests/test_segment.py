import allure
import pytest
from tests.base_case import BaseCase


class TestSegment(BaseCase):

    @allure.story('Test new segment')
    @pytest.mark.create_segment
    def test_create_segment(self):
        name = self.generate_random_string(length=6)
        with allure.step('Going to initial and create segments pages'):
            segments_page = self.dashboard_page.go_to_segments()
            segments_page.initial_and_create(name)
        segments_page.check_segment(name)
        segments_page.delete_segment(name)

    @allure.story('Test delete segment')
    @pytest.mark.delete_segment
    def test_delete_segment(self):
        name = self.generate_random_string(length=6)
        with allure.step('Going to initial and create segments pages'):
            segments_page = self.dashboard_page.go_to_segments()
            segments_page.initial_and_create(name)
        segments_page.delete_segment(name)
        assert name not in self.driver.page_source

