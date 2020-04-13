from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestGroupChat:
    @classmethod
    def setup(cls):
        cls.group_chat = GroupChat()
        cls.token = WeWork.get_token(GroupChat.secret)

    def test_group_chat_status(self):
        r = self.group_chat.group_chat_list(status_filler=0)
        assert r["errcode"] == 0

    def test_group_chat_list(self):
        r = self.group_chat.group_chat_list()
        assert r["errcode"] == 0

    def test_group_chat_detail(self):
        r = self.group_chat.group_chat_list()
        chat_id = r["group_chat_list"][0]["chat_id"]
        r = self.group_chat.group_chat_detail(chat_id=chat_id)
        assert r["errcode"] == 0
