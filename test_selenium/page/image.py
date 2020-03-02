from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test_selenium.page.basepage import BasePage


class Image(BasePage):

    def upload_text(self):
        pass

    def upload_imagetext(self):
        pass

    def upload_image(self, path):
        self.find((By.CSS_SELECTOR, ".ww_icon_GrayPic")).click()
        self.find((By.CSS_SELECTOR, ".ww_commonImg_AddMember")).click()
        self.find((By.ID, "js_upload_input")).send_keys(path)
        sleep(5)
        self.find((By.LINK_TEXT, "完成")).click()

    def delete_image(self):
        self.find((By.CSS_SELECTOR, ".ww_icon_GrayPic")).click()
        mouse = self.find((By.XPATH, "//*[contains(@class,'js_pic_preview_item')]/div/div"))
        hidden_ele = self.find((By.XPATH, "//*[contains(@class,'ww_fileOperationBar_BlackBg')]/div[3]/a"))
        ActionChains(self._driver).move_to_element(mouse).perform()
        self._driver.execute_script("arguments[0].click();", hidden_ele)
        self.find((By.CSS_SELECTOR, "[node-type='ok']")).click()

    def upload_voice(self):
        pass

    def upload_vedio(self):
        pass

    def upload_file(self):
        pass
