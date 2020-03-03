import logging
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _black_list = [
        (By.ID, "tv_agree"),
        (By.XPATH, "//*[@text='确定']"),
        (By.XPATH, "//*[@text='取消']"),
        (By.XPATH, "//*[@text='确认']")
    ]
    _error_max = 3
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 二次封装默认的find_element方法
    def find(self, by, locator: str = None):
        logging.info(by)
        logging.info(locator)
        try:
            if isinstance(by, tuple):
                return self._driver.find_element(*by)
            else:
                return self._driver.find_element(by, locator)
            # self._error_max = 0
        except Exception as e:
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
                # else:
                #     self._error_count += 1
                #     if self._error_count > self._error_max:
                #         raise e

