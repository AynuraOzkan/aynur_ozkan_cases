from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Browser:
    @staticmethod
    def get_driver(browser_name="chrome"):
        browser_name = browser_name.lower()

        if browser_name == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.maximize_window()
        return driver