from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage
from test_appium.page.profile import Profile
from test_appium.page.search import Search
from test_appium.page.stocks import Stocks


class Main(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, "tv_search").click()
        return Search(self._driver)

    def goto_messages(self):
        pass

    def goto_stocks(self):
        self.find(MobileBy.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='行情')]").click()
        return Stocks(self._driver)

    def goto_trade(self):
        pass

    def goto_profile(self):
        self.find(MobileBy.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='我的')]").click()
        return Profile(self._driver)