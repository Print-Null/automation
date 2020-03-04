import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().wait_load_main()

    def test_search(self):
        self.main.goto_search_page().search("alibaba").get_price("BABA")

    def test_add_selected(self):
        assert "已添加" in self.main.goto_search_page().search("maotai").add_select().add_selected()

    @pytest.mark.parametrize("key, stock_key, price", [
        ("alibaba", "BABA", 200),
        ("JD", "JD", 20)
    ])
    def test_search_price(self, key, stock_key, price):
        assert self.main.goto_search_page().search(key).get_price(stock_key) > price

    def teardown(self):
        pass
