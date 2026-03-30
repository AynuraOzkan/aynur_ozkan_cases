import os
import pytest
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome or firefox")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        drv = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        drv.maximize_window()

    else:
        raise Exception("Unsupported browser! Use --browser=chrome or --browser=firefox")

    yield drv
    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # If the test fails, take a screenshot
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")