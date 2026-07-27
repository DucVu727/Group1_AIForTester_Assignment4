# Python 3 | Selenium 4.x

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://the-internet.herokuapp.com/login"
VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"
INVALID_USERNAME = "user_sai"
INVALID_PASSWORD = "pass_sai"
TIMEOUT = 10


def create_driver():
    """Khởi tạo Chrome WebDriver bằng webdriver_manager."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def open_login_page(driver):
    """Mở trang Login và chờ ô Username hiển thị."""
    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )


def login(driver, username, password):
    """Điền dữ liệu đăng nhập và bấm Login."""
    username_input = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    password_input = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    login_button = WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )

    # Điền Username
    username_input.clear()
    username_input.send_keys(username)

    # Điền Password
    password_input.clear()
    password_input.send_keys(password)

    # Nhấn nút Login
    login_button.click()


def wait_for_flash_text(driver, timeout=TIMEOUT):
    """Chờ flash message xuất hiện và có text."""
    def _get_flash_text(d):
        try:
            flash = d.find_element(By.ID, "flash")
            text = flash.text.strip()
            return text if text else False
        except Exception:
            return False

    return WebDriverWait(driver, timeout).until(_get_flash_text)


def run_tc_01_login_success():
    """TC_01: Đăng nhập thành công với credential hợp lệ."""
    driver = create_driver()
    try:
        print("Running TC_01 - Login success")

        open_login_page(driver)
        login(driver, VALID_USERNAME, VALID_PASSWORD)

        # Chờ chuyển hướng đến /secure
        WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/secure"))

        # Chờ thông báo thành công
        flash_text = wait_for_flash_text(driver)

        # Assertion
        assert "/secure" in driver.current_url, \
            f"Expected URL to contain '/secure', but got: {driver.current_url}"
        assert "You logged into a secure area!" in flash_text, \
            f"Expected success message not found. Actual message: {flash_text}"

        print("TC_01 PASSED")
    finally:
        driver.quit()


def run_tc_02_login_failure():
    """TC_02: Đăng nhập thất bại với thông tin sai."""
    driver = create_driver()
    try:
        print("Running TC_02 - Login failure")

        open_login_page(driver)
        login(driver, INVALID_USERNAME, INVALID_PASSWORD)

        # Chờ thông báo lỗi xuất hiện
        flash_text = wait_for_flash_text(driver)

        # Assertion
        assert "/secure" not in driver.current_url, \
            f"Expected not to redirect to '/secure', but got: {driver.current_url}"
        assert "Your username is invalid!" in flash_text, \
            f"Expected error message not found. Actual message: {flash_text}"

        print("TC_02 PASSED")
    finally:
        driver.quit()


def main():
    run_tc_01_login_success()
    run_tc_02_login_failure()
    print("ALL TEST CASES PASSED")


if __name__ == "__main__":
    main()