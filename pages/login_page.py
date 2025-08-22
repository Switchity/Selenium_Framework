from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.radius")
    FLASH = (By.ID, "flash")

    def open_login_page(self):
        self.open(Config.BASE_URL + "/login")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_flash_message(self):
        return self.get_text(self.FLASH)
