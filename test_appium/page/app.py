from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        # 初始化driver，如果继承至父类的driver默认是None，则按以下方式初始化driver
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "YXF_6.0"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            # adb shell pm dump com.android.webview | grep version 获取到webview对应的chromedriver版本后使用
            # caps["chromedriverExecutable"] = r"C:\WebDriver\2.20\chromedriver.exe"指定对应的driver启动webview
            caps["chromedriverExecutable"] = r"C:\WebDriver\2.20\chromedriver.exe"
            # caps["chromedriverExecutableDir"] = r"C:\WebDriver\2.20"
            # caps["noReset"] = True
            # caps["unicodeKeyrboard"] = True
            # caps["resetKeyboard"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(20)
        else:
            # 如果driver已经存在，则直接复用driver启动activity
            self._driver.start_activity(self._package, self._activity)
        # return self以便初始化App实例时继续调用该方法以初始化driver
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def close(self):
        sleep(5)
        self._driver.quit()

    def wait_load_main(self):
        self.find(MobileBy.ID, "tv_agree").click()
        return Main(self._driver)
