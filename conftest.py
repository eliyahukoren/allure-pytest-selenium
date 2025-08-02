import pytest
import os
from selenium.webdriver.chrome.service import Service
# from seleniumwire import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    service = Service("./driver/chromedriver")
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options, service=service)
    request.cls.driver = driver
    yield driver
    driver.quit()
