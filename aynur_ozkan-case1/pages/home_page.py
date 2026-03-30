from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://insiderone.com/"

    MAIN_BLOCKS = [
        (By.TAG_NAME, "header"),
        (By.TAG_NAME, "footer"),
    ]

    def open(self):
        self.driver.get(self.URL)

    def verify_home_loaded(self):
        for block in self.MAIN_BLOCKS:
            assert self.is_visible(block), f"Main block not visible: {block}"