# Python 3 | Selenium 4.x

import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Import LoginPage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.login_page import LoginPage

VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"
INVALID_USERNAME = "user_sai"
INVALID_PASSWORD = "pass_sai"
TIMEOUT = 10


def create_driver():
    """Khởi tạo Chrome WebDriver."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def run_tc_01_login_success():
    """TC_01: Đăng nhập thành công."""
    driver = create_driver()

    try:
        print("Running TC_01 - Login Success")

        page = LoginPage(driver)
        page.open()
        page.login(VALID_USERNAME, VALID_PASSWORD)

        WebDriverWait(driver, TIMEOUT).until(
            EC.url_contains("/secure")
        )

        flash_text = page.get_flash_message()

        assert "/secure" in driver.current_url
        assert "You logged into a secure area!" in flash_text

        print("TC_01 PASSED")

    finally:
        driver.quit()


def run_tc_02_login_failure():
    """TC_02: Đăng nhập thất bại."""
    driver = create_driver()

    try:
        print("Running TC_02 - Login Failure")

        page = LoginPage(driver)
        page.open()
        page.login(INVALID_USERNAME, INVALID_PASSWORD)

        flash_text = page.get_flash_message()

        assert "/secure" not in driver.current_url
        assert "Your username is invalid!" in flash_text

        print("TC_02 PASSED")

    finally:
        driver.quit()


def main():
    run_tc_01_login_success()
    run_tc_02_login_failure()

    print("ALL TEST CASES PASSED")


if __name__ == "__main__":
    main()