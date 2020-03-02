from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExerciseTwo:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com")
        self.driver.implicitly_wait(5)

    def test_mtsc(self):
        element1 = (By.CSS_SELECTOR, ".topic-21839 .title > a")
        element2 = (By.CSS_SELECTOR, ".toc-container .btn")
        # element3 = (By.CSS_SELECTOR, ".list .toc-item:nth-child(4)")
        element3 = (By.LINK_TEXT, "TesterHome 成都沙龙")
        self.driver.set_window_size(1936, 1056)
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(element1))
        self.driver.find_element(*element1).click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(element2))
        self.driver.find_element(*element2).click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(element3))
        self.driver.find_element(*element3).click()
        # self.driver.switch_to.frame(0)                                    #切换frame
        # self.driver.window_handles                                        #列举windows窗口数量
        # self.driver.switch_to.window(self.driver.window_handles[x])       #切换windows窗口

    # 执行js脚本
    def test_js(self):
        for code in [
            'return document.title',
            'return document.querySelector(".active").className',
            'return JSON.stringify(performance.timing)'
        ]:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self, method):
        sleep(10)
        self.driver.quit()
