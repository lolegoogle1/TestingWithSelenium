import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_ad000d0o0p0t0ion(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="With that argument you can explicitly"
                                                                  "enter the browser that program should use"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    driver = webdriver.Firefox(executable_path="C:\\Program Files (x86)\Mozilla Firefox\geckodriver.exe")

    if browser_name == "chrome":
        # Chrome invocation
        pass
    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.close()


