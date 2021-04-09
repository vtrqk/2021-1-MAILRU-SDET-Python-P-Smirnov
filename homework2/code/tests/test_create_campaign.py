import allure
import pytest

from tests.base_case import BaseCase


class TestCampaign(BaseCase):

    @allure.feature('Test campaign')
    @pytest.mark.campaign
    def test_create_campaign(self, file_path):

        camapign_new_page = self.dashboard_page.go_to_campaign_new()
        with allure.step('Going to creat campaign'):
            camapign_new_page.create_new_campaign(file_path)
        self.dashboard_page.check_campaign('Новая кампания')
        self.dashboard_page.delete_campaign()
