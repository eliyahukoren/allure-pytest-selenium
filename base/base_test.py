import pytest
from pages.login_page import LoginPage


class BaseTest:
    login_page: LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.instance.driver = driver
        request.instance.login_page = LoginPage(driver=driver)
