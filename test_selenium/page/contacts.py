from selenium.webdriver.common.by import By
from test_selenium.page.basepage import BasePage


class Contacts(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self, name="", account="", number=""):
        name_locator = (By.NAME, "username")
        acct_locator = (By.NAME, "acctid")
        sex_locator = (By.CSS_SELECTOR, ".ww_radio[value='2']")
        mobile_locator = (By.NAME, "mobile")
        save_locator = (By.LINK_TEXT, "保存")
        self.find(name_locator).send_keys(name)
        self.find(acct_locator).send_keys(account)
        self.find(sex_locator).click()
        # self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        # self.find((By.CSS_SELECTOR, "li[data-value='853']")).click()
        self.find(mobile_locator).send_keys(number)
        self.find(save_locator).click()
        return self

    def edit_member(self, tell="", alias="", address="", position=""):
        self.find((By.CSS_SELECTOR, '[title="%s"]' % tell)).click()
        self.find((By.LINK_TEXT, "编辑")).click()
        self.find((By.NAME, "english_name")).send_keys(alias)
        self.find((By.NAME, "xcx_corp_address")).send_keys(address)
        self.find((By.NAME, "position")).send_keys(position)
        self.find((By.LINK_TEXT, "保存")).click()


'''     #edit_member方法的另一种实现，使用鼠标悬浮点击隐藏的编辑按钮
    def edit_member(self):
        hidden_button = self.find((By.XPATH, "//*[contains(@class,'js_ww_table')]/tbody[1]/tr/td[7]"))
        ActionChains(self._driver).move_to_element(hidden_button).perform()
        self.find((By.XPATH, "//*[contains(@class,'js_ww_table')]/tbody[1]/tr/td[7]/a")).click()
        sleep(2)
        self.find((By.XPATH, "//*[contains(@class,'smart_menu_box')]/div/ul/li[1]/a")).click()

        # hidden_button = self._driver.find_element_by_xpath("//*[contains(@class,'js_ww_table')]/tbody[1]/tr/td[7]")
        # point = self._driver.find_element_by_xpath("//*[contains(@class,'js_ww_table')]/tbody[1]/tr/td[7]/a")
        # ActionChains(self._driver).move_to_element(hidden_button).perform()
        # self._driver.execute_script("arguments[0].click();", point)
        # sleep(2)
        # self.find((By.XPATH, "//*[contains(@class,'smart_menu_box')]/div/ul/li[1]/a")).click()
'''
