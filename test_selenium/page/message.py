from time import sleep
from selenium.webdriver.common.by import By
from test_selenium.page.basepage import BasePage


class Message(BasePage):
    def send(self, app="", content="", group=""):
        self.find((By.LINK_TEXT, "选择需要发消息的应用")).click()
        self.find((By.CSS_SELECTOR, "div[data-name*='%s']" % app)).click()
        self.find((By.LINK_TEXT, "确定")).click()
        self.find((By.CSS_SELECTOR, ".js_select_range_btn")).click()
        self._driver.find_elements(By.CSS_SELECTOR, ".ww_searchInput_text")[-1].send_keys(group)
        # self.find((By.CSS_SELECTOR, "#searchResult li")).click()
        sleep(3)
        self._driver.find_elements(By.CSS_SELECTOR, ".ww_searchResult_item_Curr")[-1].click()
        self.find((By.LINK_TEXT, "确认")).click()
        self.find((By.CSS_SELECTOR, ".js_send_msg_text")).send_keys(content)
        self.find((By.LINK_TEXT, "发送")).click()
        self.find((By.LINK_TEXT, "确定")).click()

    def get_message(self):
        result = []
        self.find((By.LINK_TEXT, "已发送")).click()
        for message in self._driver.find_elements(By.CSS_SELECTOR, ".js_msg_row>td:nth-child(3)"):
            result.append(message.text)
        return result
