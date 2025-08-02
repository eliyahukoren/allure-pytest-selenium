import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    # locators = {
    #     "user_name": "//input[@name='username']",
    #     "password": "//input[@name='password']",
    #     "login": "//button[@type='submit'"
    # }
    username_field = ("xpath", "//input[@name='username']")
    password_field = ("xpath", "//input[@name='password']")
    submit_button = ("xpath", "//button[@type='submit']")

    @allure.step("Enter username")
    def enter_username(self, username: str):
        self.wait.until(EC.element_to_be_clickable(self.username_field)).send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password: str):
        self.wait.until(EC.element_to_be_clickable(self.password_field)).send_keys(password)

    @allure.step("Click submit button")
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
