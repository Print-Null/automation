import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BaseApi(object):
    _driver: WebDriver
    _url = "https://mubu.com/"

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.get(self._url)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

    def find(self, by, locator=None):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def estimate_element(self, element):
        return len(self._driver.find_elements(*element))
        # try:
        #     if len(self._driver.find_elements(*element)) >= 1:
        #         return False
        #     else:
        #         return True
        # except NoSuchElementException:
        #     print("页面跳转成功，元素找不到了")

    def quit(self):
        time.sleep(5)
        self._driver.quit()
