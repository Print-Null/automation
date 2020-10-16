from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMain(object):
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "YXF_8.0"
        caps["appPackage"] = "com.flashexpress.express"
        caps["appActivity"] = ".welcome.WelcomeActivity"
        caps["autoGrantPermissions"] = True  # 应用访问权限全部允许
        caps["noReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_main_page(self):
        element = (By.ID, "addressRecycleView")
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, "closeAlert")))
        self.driver.find_element(By.ID, "closeAlert").click()
        self.driver.find_element(By.ID, "deliverTabButton").click()
        self.driver.find_element(By.ID, "inputOrder").click()
        self.driver.find_element(By.ID, "contactsRight").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(self.driver.find_element(*element)))
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'addressRecycleView')]/*[1]").click()
        self.driver.find_element(By.ID, "start_fill").click()
        self.driver.find_element(By.ID, "contactsRight").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(self.driver.find_element(*element)))
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'addressRecycleView')]/*[1]").click()
        self.driver.find_element(By.ID, "right_icon").click()
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'typeText') and (@text='干燥食品')]").click()
        self.driver.find_element(By.ID, "valueInput").send_keys("8")
        self.driver.find_element(By.ID, "lengthInput").send_keys("20")
        self.driver.find_element(By.ID, "widthInput").send_keys("20")
        self.driver.find_element(By.ID, "heightInput").send_keys("20")
        self.driver.find_element(By.ID, "confirmBtn").click()
        self.driver.find_element(By.ID, "tv_right").click()
        self.driver.find_element(By.ID, "agreementCheck").click()
        self.driver.find_element(By.ID, "submitOrder").click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, "confirmBtn")))
        self.driver.find_element(By.ID, "confirmBtn").click()
        self.driver.find_element(By.ID, "toDetial").click()

    def teardown(self):
        sleep(10)
        self.driver.quit()
