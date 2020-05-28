from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from test_appium.page.basepage import BasePage


class Search(BasePage):
    def search(self, key: str):
        # 不使用数据驱动的实现
        # self.find(MobileBy.ID, "search_input_text").send_keys(key)
        # self.find(MobileBy.ID, "name").click()
        # 使用数据驱动的实现
        self._params = {}
        self._params["search_name"] = key
        self.data_driven(r"D:\MyProjects\test_appium\page\search.yaml")
        return self

    def get_price(self, key: str):
        price = (MobileBy.ID, "current_price")
        return float(self.find(*price).text)

    def add_select(self):
        self.find(By.ID, "follow_btn").click()
        return self

    def add_selected(self):
        return self.find(By.ID, "followed_btn").text
