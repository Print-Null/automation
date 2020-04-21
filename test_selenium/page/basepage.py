from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                # 复用已经存在的Chrome进程
                # 在cmd下使用命令 Chrome --remote-debugging-port=9222 启动Chrome浏览器
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)

            self._driver.maximize_window()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        if isinstance(by, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(by, locator)

    def close(self):
        sleep(5)
        self._driver.quit()


