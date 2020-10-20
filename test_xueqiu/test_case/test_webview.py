from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestWebView(object):
    def setup_method(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "YXF_6.0"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["chromedriverExecutable"] = r"C:\WebDriver\2.20\chromedriver.exe"
        caps["autoGrantPermissions"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["noReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_webview(self):
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='交易')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        for i in range(5):
            print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.ID, "phone-number").send_keys("13466547593")
        self.driver.find_element(By.ID, "code").send_keys("123456")

    def test_webview1(self):
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='交易')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "港美股开户").click()
        for i in range(5):
            print(self.driver.contexts)
        # self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "请输入手机号").send_keys("13466547593")
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "请输入验证码").send_keys("123456")

    def teardown_method(self):
        sleep(10)
        self.driver.quit()
