import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LeverPage:
    JOB_CARDS = (By.CSS_SELECTOR, ".posting")

    LOCATION_FILTER_DROPDOWN = (By.CSS_SELECTOR, "div.filter-button.filter-button-mlp")
    LOCATION_FILTER_OPTION = (By.XPATH, "//*[contains(text(),'Istanbul') and contains(text(),'Turkiye')]")

    JOB_TITLE = (By.CSS_SELECTOR, ".posting-header-title")
    JOB_DETAIL_APPLY_BTN = (By.CSS_SELECTOR, "a.postings-btn.template-btn-submit.hex-color")

    FIRST_JOB_APPLY_BTN = (By.XPATH, "(//a[contains(@href,'jobs.lever.co/insiderone/')])[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def verify_redirected_to_lever(self):
        self.wait.until(EC.url_contains("lever.co/insiderone"))
        assert "lever.co/insiderone" in self.driver.current_url

    def close_cookie_banner_if_exists(self):
        try:
            banner = self.driver.find_element(By.CSS_SELECTOR, "button#onetrust-accept-btn-handler")
            self.driver.execute_script("arguments[0].click();", banner)
            time.sleep(1)
        except:
            pass

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)

    def wait_for_jobs_to_load(self, timeout=40):
        end_time = time.time() + timeout
        while time.time() < end_time:
            jobs = self.driver.find_elements(*self.JOB_CARDS)
            if len(jobs) > 0:
                return
            time.sleep(0.5)

        raise TimeoutException("Job listesi yüklenemedi")

    def filter_by_location_istanbul(self):
        self.close_cookie_banner_if_exists()
        self.wait_for_jobs_to_load()

        dropdown = self.wait.until(EC.presence_of_element_located(self.LOCATION_FILTER_DROPDOWN))
        self.scroll_into_view(dropdown)

        try:
            dropdown.click()
        except:
            self.driver.execute_script("arguments[0].click();", dropdown)

        option = self.wait.until(EC.presence_of_element_located(self.LOCATION_FILTER_OPTION))
        self.scroll_into_view(option)

        try:
            option.click()
        except:
            self.driver.execute_script("arguments[0].click();", option)

        # if the Apply button cannot be find, the filtre could be applied to automatically
        time.sleep(3)

        self.wait_for_jobs_to_load()

    def verify_jobs_list_exists(self):
        self.wait_for_jobs_to_load()
        jobs = self.driver.find_elements(*self.JOB_CARDS)
        assert len(jobs) > 0, "Job listesi boş"

    def click_first_apply(self):
        self.wait_for_jobs_to_load()

        first_job = self.wait.until(EC.element_to_be_clickable(self.FIRST_JOB_APPLY_BTN))
        self.scroll_into_view(first_job)

        try:
            first_job.click()
        except:
            self.driver.execute_script("arguments[0].click();", first_job)

        # if the opens another tab, skip it
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_job_page_to_load(self):
        self.wait.until(EC.presence_of_element_located(self.JOB_TITLE))

    def click_apply_for_this_job_and_verify(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.JOB_DETAIL_APPLY_BTN))
        self.scroll_into_view(btn)

        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

        self.wait.until(lambda d: "/apply" in d.current_url)

        assert "/apply" in self.driver.current_url, (
            f"Apply sayfasına gidilemedi. Current URL: {self.driver.current_url}"
        )

    def wait_apply_form_page_loaded(self):
        self.wait.until(lambda d: "/apply" in d.current_url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        time.sleep(5)