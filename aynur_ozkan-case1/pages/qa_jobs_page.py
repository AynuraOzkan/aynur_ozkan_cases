from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class QAJobsPage(BasePage):

    # Open roles section locator 
    OPEN_ROLES_SECTION = (By.ID, "open-roles")

    # Filter locators (select2)
    DEPARTMENT_FILTER = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    LOCATION_FILTER = (By.XPATH, "//span[@id='select2-filter-by-location-container']")

    # Dropdown options
    QA_OPTION = (By.XPATH, "//li[contains(.,'Quality Assurance')]")
    ISTANBUL_OPTION = (By.XPATH, "//li[contains(.,'Istanbul, Turkey')]")

    # Job list
    JOB_LIST_ITEMS = (By.CSS_SELECTOR, "div.position-list-item")

    def filter_quality_assurance_jobs(self):
        try:
            print("STEP 0: Scroll to Open Roles section...")
            open_roles = self.wait.until(EC.presence_of_element_located(self.OPEN_ROLES_SECTION))
            self.scroll_into_view(open_roles)

            print("STEP A: Click Department filter...")
            dept = self.wait.until(EC.element_to_be_clickable(self.DEPARTMENT_FILTER))
            dept.click()

            print("STEP B: Select QA option...")
            qa = self.wait.until(EC.element_to_be_clickable(self.QA_OPTION))
            qa.click()

            print("STEP C: Click Location filter...")
            loc = self.wait.until(EC.element_to_be_clickable(self.LOCATION_FILTER))
            loc.click()

            print("STEP D: Select Istanbul option...")
            ist = self.wait.until(EC.element_to_be_clickable(self.ISTANBUL_OPTION))
            ist.click()

            print("STEP E: Wait jobs list...")
            self.wait.until(EC.presence_of_all_elements_located(self.JOB_LIST_ITEMS))

            print("SUCCESS: Jobs loaded!")

        except TimeoutException:
            raise AssertionError("Job listeleri yüklenemedi veya TimeoutException oluştu!")

    def verify_jobs_list_exists(self):
        jobs = self.find_elements(self.JOB_LIST_ITEMS)
        assert len(jobs) > 0, "Job listesi boş!"