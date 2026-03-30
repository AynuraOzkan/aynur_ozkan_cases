from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.lever_page import LeverPage


def test_insider_qa_jobs_flow(driver):

    # Step 1: Home page
    home = HomePage(driver)
    home.open()
    home.verify_home_loaded()

    # Step 2: Careers open roles page
    careers = CareersPage(driver)
    careers.open()

    # Step 3: Allow popup
    careers.click_allow_popup()

    # Step 4: See all teams
    careers.click_see_all_teams()

    # Step 5: Scroll down until page fully loaded
    careers.scroll_page_to_bottom()

    # Step 6: Click QA Open Positions
    careers.click_qa_open_positions()

    # Step 7: Verify Lever page opened and jobs exist
    lever = LeverPage(driver)
    lever.verify_redirected_to_lever()
    lever.wait_for_jobs_to_load()
    lever.filter_by_location_istanbul()
    lever.verify_jobs_list_exists()
    #lever.verify_jobs_match_criteria()
    lever.click_first_apply()
    #lever.wait_for_job_page_to_load() 
    lever.click_apply_for_this_job_and_verify()
    lever.wait_apply_form_page_loaded()