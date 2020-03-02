from selenium.webdriver.common.by import By
from test_selenium.page.basepage import BasePage
from test_selenium.page.register import Register


class Login(BasePage):
    def scan_code(self):
        pass

    def goto_registry(self):
        self.find((By.LINK_TEXT, "企业注册")).click()
        return Register(self._driver)
