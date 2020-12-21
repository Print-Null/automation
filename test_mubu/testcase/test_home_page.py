from test_mubu.base_page.home_page import HomePage


class TestHomePage:
    def setup(self):
        self.homepage = HomePage()

    def test_home_goto_login(self):
        assert "页面跳转成功" in self.homepage.home_goto_login()

    def test_login_with_account_password(self):
        print(self.homepage.goto_login().login_with_account_password("13466547593", "xiao238304"))

    def teardown(self):
        self.homepage.quit()
