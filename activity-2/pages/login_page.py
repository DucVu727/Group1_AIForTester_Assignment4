from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    BASE_URL = "https://the-internet.herokuapp.com/login"
    TIMEOUT = 10

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def open(self):
        """Mở trang Login."""
        self.driver.get(self.BASE_URL)
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )

    def login(self, username, password):
        """Thực hiện đăng nhập."""
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )

        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        login_button.click()

    def get_flash_message(self):
        """Lấy nội dung thông báo sau khi đăng nhập."""
        flash = self.wait.until(
            EC.visibility_of_element_located(self.FLASH_MESSAGE)
        )
        return flash.text.strip()