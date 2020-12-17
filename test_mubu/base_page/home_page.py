from selenium.webdriver.common.by import By

from test_mubu.base_page.baseApi import BaseApi
from test_mubu.base_page.login_page import LoginPage


class HomePage(BaseApi):
    main_button_locator = (By.CSS_SELECTOR, ".main-btn")

    def goto_login(self):
        self.find(self.main_button_locator).click()
        return LoginPage(self._driver)

    def home_goto_login(self):
        self.find(self.main_button_locator).click()
        if self.estimate_element(self.main_button_locator) is True:
            return "页面跳转成功"
        else:
            return "页面跳转失败"
