from selenium.webdriver.common.by import By

from test_appium.page.basepage import BasePage


class Profile(BasePage):
    def login_with_account(self, account, password):
        self.find(By.XPATH, "//*[contains(@resource-id,'rl_login')]/*[2]").click()
        self.find(By.ID, "login_account").send_keys(account)
        self.find(By.ID, "login_password").send_keys(password)
        self.find(By.ID, "button_next").click()
        msg = self.find(By.ID, "md_content").text
        self.find(By.ID, "md_buttonDefaultPositive").click()
        return msg

