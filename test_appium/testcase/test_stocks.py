from test_appium.page.app import App


class TestStocks:
    def setup(self):
        self.stocks = App().start().wait_load_main()

    def test_goto_search(self):
        self.stocks.goto_stocks_page().stocks_search("maotai")

    def teardown(self):
        pass
