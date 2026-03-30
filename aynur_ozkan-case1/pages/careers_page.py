import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CareersPage(BasePage):

    URL = "https://insiderone.com/careers/#open-roles"

    # Pop-up Allow button (cookie popup)
    ALLOW_BTN = (By.XPATH, "//button[contains(.,'Allow')]")

    # See all teams button
    SEE_ALL_TEAMS_BTN = (By.CSS_SELECTOR, "a.inso-btn.see-more")

    # QA Open Positions button (Lever link)
    QA_OPEN_POSITIONS_BTN = (
        By.XPATH,
        "//div[@data-department='Quality Assurance']//a[contains(@href,'jobs.lever.co')]"
    )

    def open(self):
        self.driver.get(self.URL)
        self.wait_page_loaded(timeout=25)

    def click_allow_popup(self):
        """Popup çıkarsa Allow'a bas"""
        try:
            allow = self.wait.until(EC.element_to_be_clickable(self.ALLOW_BTN))
            allow.click()
            time.sleep(1)
        except:
            pass

    def click_see_all_teams(self):
        #Click to See all teams
        btn = self.wait.until(EC.element_to_be_clickable(self.SEE_ALL_TEAMS_BTN))
        self.scroll_into_view(btn)

        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

        time.sleep(2)

    def scroll_page_to_bottom(self):
        #scroll to page for the page totally loaded 
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def click_qa_open_positions(self):
         # click to QA Open Positions link and go to the Lever page
        btn = self.wait.until(EC.presence_of_element_located(self.QA_OPEN_POSITIONS_BTN))
        self.scroll_into_view(btn)

        try:
            self.wait.until(EC.element_to_be_clickable(self.QA_OPEN_POSITIONS_BTN))
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

        # if a new tab opens, skip it.
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])