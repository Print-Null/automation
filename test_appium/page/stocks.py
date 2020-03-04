from selenium.webdriver.common.by import By
from test_appium.page.basepage import BasePage


class Stocks(BasePage):
    def stocks_search(self, key: str):
        self.find(By.XPATH, "//*[contains(@resource-id,'action_search')]").click()
        self.find(By.ID, "search_input_text").send_keys(key)
        self.find(By.XPATH, "//*[contains(@resource-id,'listview')]//*[@text='贵州茅台']").click()
        self.find(By.XPATH, "//*[@text='加自选']").click()
        self.find(By.XPATH, "//*[contains(@resource-id,'action_close') and (@text='取消')]").click()
        return self
