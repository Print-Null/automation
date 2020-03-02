from selenium.webdriver.common.by import By

from test_selenium.page.basepage import BasePage


class Register(BasePage):

    def register(self, corpname):
        self.find((By.ID, 'corp_name')).send_keys(corpname)
        self.find((By.ID, 'submit_btn')).click()
        return self  # 这里如果注册成功应该会跳转到别的页面，所以要返回新的page，但是这里故意没有注册成功，依旧停留在当前页面，所以返回self

    def get_error_message(self):
        result = []
        for message in self._driver.find_elements(By.CSS_SELECTOR, '.js_error_msg'):
            result.append(message.text)
        return result
