import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_SwichWindows:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.6vgood.com/dy6/")
        self.driver.implicitly_wait(4)


    def test_swiwindows(self):
        element1 = (By.LINK_TEXT, "谍影重重2[高清]")
        element2 = (By.CSS_SELECTOR, "tr a")
        element3 = (By.CSS_SELECTOR, "#content > div:nth-child(1) > div.context > div:nth-child(3) > a:nth-child(2)")
        element4 = (By.CSS_SELECTOR, ".dplayer-icon > svg > path")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, ".input_key").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input_key").send_keys("谍影重重")
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换浏览器窗口
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(element1))
        self.driver.find_element(*element1).click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element2))
        self.driver.find_element(*element2).click()
        self.driver.switch_to.window(self.driver.window_handles[3])
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element3))
        point = self.driver.find_element(*element3)
        self.driver.execute_script("arguments[0].click();", point)
        #self.driver.switch_to.window(self.driver.window_handles[3])
        #self.driver.execute_script("arguments[0].click();", point)
        self.driver.switch_to.window(self.driver.window_handles[4])
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element4))
        self.driver.find_element(*element4).click()
        print(self.driver.window_handles)
        #self.driver.switch_to.window(self.driver.window_handles[1])
        #self.driver.close()  # 关闭window_handles[1]标签页
        # WebDriverWait(self.driver, 10, lambda x: len(self.driver.window_handles) > 1) #lambda表达式的用法

    def teardown_method(self, method):
        pass



""" #多浏览器支持
        broswer = os.getenv("broswer", "").lower()
        print(broswer)
        if broswer == "headless":
            self.driver = webdriver.PhantomJS()
        elif broswer == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
"""
