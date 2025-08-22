from selenium.webdriver.common.by import By
from utils.helpers import wait_for_element

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return wait_for_element(self.driver, locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
