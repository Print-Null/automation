from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:
    url = "https://testerhome.com/"

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def can_not_click(self):
        self.driver.get("https://www.12306.cn/index/")
        sleep(5)
        self.driver.find_element(By.ID, "fromStationText").click()
        self.driver.find_element(By.ID, "fromStationText").send_keys("北京北")
        self.driver.find_element(By.ID, "citem_0").click()
        self.driver.find_element(By.ID, "toStationText").click()
        self.driver.find_element(By.ID, "toStationText").send_keys("上海南")
        self.driver.find_element(By.ID, "citem_0").click()
        self.driver.find_element(By.ID, "search_one").click()
        for i in self.driver.window_handles:
            print(i)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        selector = (By.CSS_SELECTOR, "#ticket_2400000G210A .no-br")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(selector))
        self.driver.find_element(*selector).click()
        sleep(5)
        selector1 = (By.CSS_SELECTOR, ".modal-login-tit .icon-close")
        self.driver.find_element(*selector1).click()
        sleep(5)
        self.driver.find_element(*selector).click()
        sleep(5)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(selector1))
        try:
            self.driver.find_element(*selector).click()
        except ElementClickInterceptedException:
            return "element click intercepted: Element is not clickable.Other element would receive the click"

    def test_click(self):
        msg = self.can_not_click()
        assert "element click intercepted" in msg

    def test_search(self):
        selector = (By.XPATH, '//*[@class="panel-body"]/*[1]')
        selector1 = (By.CSS_SELECTOR, '.navbar-nav [href="/teams"]')
        self.driver.get(self.url)
        self.driver.find_element(*selector1).click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-name="求职面试圈"]').click()
        element = expected_conditions.visibility_of_element_located(selector1)
        print(element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(selector))
        self.driver.find_element(*selector).click()

    def test_work(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, '//*[@data-name="simple"]/../..//*[@class="title media-heading"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.fa-list').click()
        self.driver.find_element(By.CSS_SELECTOR, '.list-container li:nth-child(4)').click()
