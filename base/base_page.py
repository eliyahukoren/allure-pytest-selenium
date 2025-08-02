import allure
from allure_commons.types import AttachmentType
# from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open_page(self):
        with allure.step("Open OrangeHRM login page"):
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def is_opened(self):
        with allure.step("Page [name/url] is opened"):
            self.wait.until(EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))

    def save_screenshot(self, name: str):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )
