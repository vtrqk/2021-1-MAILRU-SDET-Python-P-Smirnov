import allure
import pytest

from tests.base_case import BaseCase


class TestCampaign(BaseCase):

    @allure.feature('Test campaign')
    @pytest.mark.campaign
    def test_create_campaign(self, file_path):
        name = self.generate_random_string(length=8)
        campaign_new_page = self.dashboard_page.go_to_campaign_new()
        with allure.step('Going to creat campaign'):
            campaign_new_page.create_new_campaign(file_path, name)
        self.dashboard_page.check_campaign(name)
        self.dashboard_page.delete_campaign(name)
