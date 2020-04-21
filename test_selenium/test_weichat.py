from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Wchat():
    def setup(self):
        options = webdriver.ChromeOptions()
        # 使用headless模式(浏览器不可见)
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--window-size=1280,1696")
        # 使用已经存在的chrome进程(配合命令：Chrome --remote-debugging-port=9222)
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_wxchat(self):
        element1 = (By.CSS_SELECTOR, '.js_operationBar_footer .js_add_member')
        self.driver.find_element(By.ID, 'menu_contacts').click()
        # sleep(5)
        # WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.find_element(*element1)) > 0)
        self.driver.find_element(*element1).click()
        # self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element1))
        # WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.find_elements(By.ID, 'username')) > 0)
        self.driver.find_element(By.ID, 'username').send_keys("CSGO")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("cs1.6")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("13877777777")
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
