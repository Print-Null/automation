from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPrice:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "YXF_6.0"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # adb shell pm dump com.android.webview | grep version 获取到webview对应的chromedriver版本后使用
        # caps["chromedriverExecutable"] = r"C:\WebDriver\2.20\chromedriver.exe"指定对应的driver启动webview
        caps["chromedriverExecutable"] = r"C:\WebDriver\2.20\chromedriver.exe"
        # caps["chromedriverExecutableDir"] = r"C:\WebDriver\2.20"
        # caps["noReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_price(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='行情']").click()

    def test_scroll(self):
        size = self.driver.get_window_size()
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        sleep(5)
        for i in range(10):
            # 长按住屏幕的点1拖动鼠标到屏幕的点2（起到滑动屏幕的作用）
            TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.9).move_to(
                x=size['width'] * 0.5, y=size['height'] * 0.1).release().perform()

    def test_price1(self):
        size = self.driver.get_window_size()
        x = int(size['width'] * 0.95)
        y = int(size['height'] * 0.95)
        # 点击首页弹框的同意
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # 点击首页的搜索框
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # 在搜索框中输入"alibaba"
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("alibaba")
        # 点击输入键盘上的搜索图标
        self.driver.swipe(x, y, x, y, 100)
        # 点击股票
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'title_container')]/*[2]").click()
        price = (By.XPATH, "//*[contains(@resource-id,'list')]/*[2]//*[contains(@resource-id,'current_price')]")
        # 断言香港上市的阿里巴巴股价大于200
        assert float(self.driver.find_element(*price).text) > 200

    def test_selected(self):
        # 定义加自选按钮的定位符
        go_to_select_locator = (
            MobileBy.XPATH, "//*[@text='SH600519']/../../..//*[contains(@resource-id,'follow_btn')]")
        # 定义已添加按钮的定位符
        selected_locator = (MobileBy.XPATH, "//*[@text='SH600519']/../../..//*[contains(@resource-id,'followed_btn')]")
        # 点击首页弹框的同意
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # 点击首页的搜索框
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # 在搜索框中输入"茅台"
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("茅台")
        # 选择"贵州茅台"并点击
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'listview')]//*[@text='贵州茅台']").click()
        # 点击"贵州茅台"的"加自选"
        self.driver.find_element(*go_to_select_locator).click()
        # 点击弹出框上的"下次再说"
        self.driver.find_element(MobileBy.ID, "tv_left").click()
        # 点击"取消"搜索
        self.driver.find_element(MobileBy.ID, "action_close").click()
        # 再次点击搜索框
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # 再次在搜索框中输入"茅台"
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("茅台")
        # 再次选中"贵州茅台"并点击
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'listview')]//*[@text='贵州茅台']").click()
        # 判断"贵州茅台"是否已加入自选
        assert self.driver.find_element(*selected_locator).get_attribute("text") == "已添加"

    def test_source(self):
        print(self.driver.page_source)

    def test_webview_native(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='交易')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        sleep(10)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "输入11位手机号").send_keys("13444444444")

    # webview只有在安卓6.0以下的系统上才能调试，如果高于6.0系统，需要打开app内WebView调试开关，要启动WebView调试，请在WebView类上调用静态方法
    # setWebContentsDebuggingEnabled
    # if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
    #     WebView.setWebContentsDebuggingEnabled(true);
    # }
    # 此设置适用于应用的所有 WebView
    def test_webview_context(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='交易')]").click()
        # 打印所有的context以判断是不是有新增的webview context
        for i in range(5):
            print(self.driver.contexts)
            sleep(1)
        # 切换context到webview（可以直接使用selenium的元素定位方法），一般如果有新增的webview context都是在最后一个，所以使用-1
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 打印当前的页面窗口
        print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()
        # 打印点击操作后的页面窗口以查看是不是有新增的窗口
        for i in range(5):
            print(self.driver.window_handles)
            sleep(1)
        # 切换到新增的窗口，一般如果有新增的窗口都是在最后一个，所以使用-1
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 显示等待页面元素出现
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "phone-number")))
        self.driver.find_element(By.ID, "phone-number").send_keys("13466544444")
        # 切换context到原生context
        self.driver.switch_to.context(self.driver.contexts[-2])
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Navigate up").click()

    def test_webview_contexts(self):
        self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'tab_name') and (@text='交易')]").click()
        # 显示等待context大于1，即原生context和新出现的webview context
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.contexts) > 1)
        # 从原生context切换到webview context
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_xueying_SJY").click()
        # 显示等待新窗口出现
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.window_handles) > 3)
        # 切换到新窗口页面
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".open_input-wrapper_13S")))
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入手机号']").send_keys("13466544444")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入验证码']").send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".open_form-submit_1Ms").click()
        # 从webview context切换到原生context
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'action_bar_back')]").click()

    def teardown(self):
        sleep(5)
        self.driver.quit()
