from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By


class TestMain:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "YXF_6.0"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_login(self):
        self.driver.find_element(By.ID, "tv_agree").click()

    def test_main(self):
        pass

    def teardown(self):
        sleep(10)
        self.driver.quit()
