import pytest
from utils.browser import Browser
from utils.screenshot import take_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome or firefox"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = Browser.get_driver(browser_name)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, item.name)