from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from test_appium.page.basepage import BasePage


class Search(BasePage):
    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(MobileBy.ID, "name").click()
        return self

    def get_price(self, key: str):
        price = (MobileBy.ID, "current_price")
        return float(self.find(*price).text)
