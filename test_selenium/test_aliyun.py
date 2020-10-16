from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestALiYun(object):
    driver: webdriver = None

    def setup(self):
        if self.driver is None:
            url = "https://developer.aliyun.com/mirror/"
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            self.driver.maximize_window()

    def test_search(self):
        self.driver.find_element(By.CSS_SELECTOR, ".search-input").send_keys("centos")
        self.driver.find_element(By.CSS_SELECTOR, ".search-btn").click()

    def teardown(self):
        sleep(5)
        self.driver.quit()
