from test_appium.page.app import App


class TestDataDriven:
    def test_main_yaml(self):
        App().start().wait_load_main().goto_search_page()

    def test_search(self):
        App().start().wait_load_main().goto_search_page().search("maotai")
