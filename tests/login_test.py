import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Test functionality")
class TestLoginFeature(BaseTest):

    @allure.title("Title: Login")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_login(self):
        self.login_page.open_page()
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login()
