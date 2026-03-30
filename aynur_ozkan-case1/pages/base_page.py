from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def wait_page_loaded(self, timeout=20):
     WebDriverWait(self.driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_into_view(element)
        try:
            element.click()
        except:
            # If the click is blocked, try again with ActionChains
            ActionChains(self.driver).move_to_element(element).click().perform()

    def js_click(self, element):
     self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_into_view(self, element):
     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)