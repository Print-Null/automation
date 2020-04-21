from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:
    url = "https://testerhome.com/"

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_search(self):
        selector = (By.XPATH, '//*[@class="panel-body"]/*[1]')
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, '.navbar-nav [href="/teams').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(selector))
        self.driver.find_element(*selector).click()

    def test_work(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, '//*[@data-name="simple"]/../..//*[@class="title media-heading"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.fa-list').click()
        self.driver.find_element(By.CSS_SELECTOR, '.list-container li:nth-child(4)').click()
