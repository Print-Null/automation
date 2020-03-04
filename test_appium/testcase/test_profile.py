from test_appium.page.app import App


class TestProfile:
    def setup(self):
        self.profile = App().start().wait_load_main().goto_profile_page()

    def test_profile(self):
        assert "请稍后再试" in self.profile.login_with_account("13466541234", "123456")

    def teardown(self):
        pass
