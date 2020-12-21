from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from test_mubu.base_page.baseApi import BaseApi
from test_mubu.base_page.list_page import ListPage


class LoginPage(BaseApi):
    def login_with_phone_number(self, phone, verify_code):
        pass

    def login_with_account_password(self, account, password):
        password_login_locator = (By.CSS_SELECTOR, "#main-form div:nth-child(4)>a")
        self.find(password_login_locator).click()
        self.find(By.NAME, "phone").send_keys(account)
        self.find(By.NAME, "password").send_keys(password)
        self.find(By.ID, "submit").click()
        try:
            if self.estimate_element((By.NAME, "phone")) < 1:
                return ListPage(self._driver)
        except NoSuchElementException as e:
            print(e)
        else:
            return self.find(By.CSS_SELECTOR, ".toast-box").text
