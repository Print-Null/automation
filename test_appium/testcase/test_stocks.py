from test_appium.page.app import App


class TestStocks:
    def setup(self):
        self.stocks = App().start().main().goto_stocks()

    def test_goto_search(self):
        self.stocks.goto_search("maotai")

    def teardown(self):
        pass
