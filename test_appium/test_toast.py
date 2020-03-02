from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "YXF_6.0"
        caps["appPackage"] = "com.example.android.apis"
        caps["appActivity"] = ".ApiDemos"
        self.dirver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.dirver.implicitly_wait(20)

    def test_toast(self):
        # 滚屏到Views菜单
        scroll_to_element1 = (MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0));')
        # 滚屏到Popup Menu菜单
        scroll_to_element2 = (MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));')
        # 滚屏到Views菜单并点击
        self.dirver.find_element(*scroll_to_element1).click()
        # 滚屏到Popup Menu菜单并点击
        self.dirver.find_element(*scroll_to_element2).click()
        self.dirver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Button']").click()
        self.dirver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'title') and (@text='Search')]").click()
        # 打印点击search后弹出的Toast内容(获取Toast可以使用固定类"android.widget.Toast")
        toast = self.dirver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "Clicked" in toast
        assert "Search" in toast

    def teardown(self):
        sleep(5)
        self.dirver.quit()
