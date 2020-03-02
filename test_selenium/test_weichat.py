from logging import exception
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Wchat():
    def setup(self):
        chromeOptions = Options()
        # chromeOptions.binary_location = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_wxchat(self):
        # element1 = (By.CSS_SELECTOR, '.js_has_member div:nth-child(-1) .js_add_member')
        self.driver.find_element(By.ID, 'menu_contacts').click()
        WebDriverWait(self.driver, 10).until(self.wait_element)
        # self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        self.driver.find_element(By.ID, 'username').send_keys("张三")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("12345")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("13577777777")
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def wait_element(self, x):
        size = len(self.driver.find_element(By.ID, 'username'))
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1
