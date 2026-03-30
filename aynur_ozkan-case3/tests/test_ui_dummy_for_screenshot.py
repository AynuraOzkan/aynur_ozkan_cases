from pages.base_page import BasePage


def test_open_swagger_page(driver):
    page = BasePage(driver)
    page.open_url("https://petstore.swagger.io/")

    assert "Swagger" in page.get_title()

# @pytest.mark.xfail(reason="# I deliberately fail to take a screenshot")
def test_fail_screenshot_demo(driver):
    page = BasePage(driver)
    page.open_url("https://petstore.swagger.io/")

    
    assert "THIS_WILL_FAIL" in page.get_title()