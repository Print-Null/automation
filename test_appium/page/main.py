from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage
from test_appium.page.profile import Profile
from test_appium.page.search import Search
from test_appium.page.stocks import Stocks


class Main(BasePage):
    def goto_search_page(self):
        # 不使用数据驱动的实现
        self.find(MobileBy.ID, "tv_search").click()
        # 使用数据驱动的实现
        self.data_driven(r"D:\MyProjects\test_appium\page\main.yaml")
        return Search(self._driver)

    def goto_messages(self):
        pass

    def goto_stocks_page(self):
        self.find(MobileBy.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='行情')]").click()
        return Stocks(self._driver)

    def goto_trade(self):
        pass

    def goto_profile_page(self):
        self.find(MobileBy.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='我的')]").click()
        return Profile(self._driver)
