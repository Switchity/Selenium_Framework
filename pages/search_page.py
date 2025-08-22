from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_BOX = (By.NAME, "q")
    RESULTS = (By.ID, "search")

    def search(self, term):
        self.type(self.SEARCH_BOX, term + "\n")

    def get_results_text(self):
        return self.get_text(self.RESULTS)
