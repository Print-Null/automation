from selenium.webdriver.common.by import By
from test_selenium.page.basepage import BasePage
from test_selenium.page.image import Image


class ManageTool(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def goto_material_library(self):
        self.find((By.CSS_SELECTOR, "li:nth-child(5)")).click()
        return Image(reuse=True)


