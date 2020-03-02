from test_selenium.page.contacts import Contacts


class TestContacts:
    contact = Contacts(reuse=True)

    def test_add_member(self):
        self.contact.add_member(name="张四", account="zhangsi", number="13422222222")

    def test_edit_member(self):
        self.contact.edit_member(tell="13400000000", alias="san", address="北京", position="test_engineer")


