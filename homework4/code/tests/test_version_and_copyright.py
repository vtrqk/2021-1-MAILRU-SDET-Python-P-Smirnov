import pytest
from tests.base import BaseCase


class TestVersionAndCopyright(BaseCase):

    @pytest.mark.AndroidUI_Version
    def test_version(self):
        settings_page = self.main_page.go_to_settings()
        about_page = settings_page.go_to_about_page()
        about_page.check_version(version_apk=self.main_page.get_version(repo_root=self.repo_root))

    @pytest.mark.AndroidUI_Trademark
    def test_trademark(self):
        settings_page = self.main_page.go_to_settings()
        about_page = settings_page.go_to_about_page()
        about_page.check_copyright(name_trademark='Все права защищены')
