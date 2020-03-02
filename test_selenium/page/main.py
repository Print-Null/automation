from selenium.webdriver.common.by import By
from test_selenium.page.basepage import BasePage
from test_selenium.page.contacts import Contacts
from test_selenium.page.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def download(self):
        pass

    def send_invite(self):
        pass

    def go_check(self):
        pass

    def get_message(self):
        pass

    def add_member(self):
        self.find((By.LINK_TEXT, "添加成员")).click()
        # 当原生点击方法点击不到元素的时候使用如下的js点击方法实现
        # self._driver.execute_script("argument[0].click();", self.find((By.LINK_TEXT, "添加成员")))
        return Contacts(reuse=True)

    def import_contacts(self, path):
        self.find((By.LINK_TEXT, "导入通讯录")).click()
        # self.find((By.CSS_SELECTOR, ".import_settingStage_upload_inputWrap")).click()
        self.find((By.ID, "js_upload_file_input")).send_keys(path)
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "submit_csv")))
        self.find((By.ID, "submit_csv")).click()
        return self

    def member_join(self):
        pass

    def send_messages(self):
        self.find((By.LINK_TEXT, "消息群发")).click()
        return Message(reuse=True)

    def customer_contact(self):
        pass

    def punch_card(self):
        pass
