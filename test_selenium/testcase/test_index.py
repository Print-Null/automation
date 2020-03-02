from test_selenium.page.index import Index


class TestIndex:

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register("天道有轮回")

    def test_login(self):
        register_message = self.index.goto_login().goto_registry().register("河北家里蹲公司")
        print(register_message.get_error_message())
        print("|".join(register_message.get_error_message()))
        assert "请选择" in "|".join(register_message.get_error_message())

    def teardown(self):
        self.index.close()
