from selenium.webdriver.common.by import By
from test_selenium.page.basepage import BasePage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):  # 封装PO，企业微信首页的立即注册抽象为goto_register方法
        self.find((By.LINK_TEXT, '立即注册')).click()
        return Register(self._driver)  # click完如果跳转到新的页面，则返回新的页面（即PO）

    def goto_login(self):  # 封装PO，企业微信首页的企业登录抽象为goto_login方法
        self.find((By.LINK_TEXT, "企业登录")).click()
        return Login(self._driver)  # click完如果跳转到新的页面，则返回新的页面（即PO）
