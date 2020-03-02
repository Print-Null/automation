import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().wait_load_main()

    def test_search(self):
        self.main.goto_search().search("alibaba").get_price("BABA")

    @pytest.mark.parametrize("key, stock_key, price", [
        ("alibaba", "BABA", 200),
        ("JD", "JD", 20)
    ])
    def test_search_price(self, key, stock_key, price):
        assert self.main.goto_search().search(key).get_price(stock_key) > price

    def teardown(self):
        pass
