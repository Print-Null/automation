from test_selenium.page.main import Main


class TestMain:
    main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member(name="李逵", account="likui", number="13433333333")

    def test_import_member(self):
        self.main.import_contacts(r"D:\MyProjects\test_selenium\通讯录批量导入模板.xlsx")

    def test_send_message(self):
        self.main.send_messages().send(app="一", content="content", group="一")
        self.main.send_messages().send(app="一", content="Wuhan cheer!China cheer!", group="一")

    def test_get_message(self):
        sended_message = self.main.send_messages().get_message()
        print("|".join(sended_message))
        assert "content" in sended_message
        assert "Wuhan cheer!China cheer!" in sended_message
