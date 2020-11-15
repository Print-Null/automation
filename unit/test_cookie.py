import json

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCookie:
    def get_myself_cookie(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_option)
        # self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        return self.driver.get_cookies()

    def test_cookie(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.delete_all_cookies()
        cookies = self.get_myself_cookie()
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element(By.ID, "ember33").click()
        sleep(5)

    def test_json(self):
        a = {"data": {"name": {"name": "yxf", "name": "gcx"}}}
        b = json.loads(json.dumps(a))
        print(b["data"]["name"])

