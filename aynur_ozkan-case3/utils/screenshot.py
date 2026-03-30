import os
from datetime import datetime


def take_screenshot(driver, test_name="failed_test"):
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

    driver.save_screenshot(file_path)
    print(f"[INFO] Screenshot saved: {file_path}")