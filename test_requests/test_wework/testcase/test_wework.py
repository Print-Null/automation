from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestWeWork:
    @classmethod
    def setup(cls):
        cls.token = WeWork.get_token(GroupChat.secret)

    def test_token_exist(self):
        assert self.token is not None

    def test_get_access_token(self):
        r = WeWork.get_access_token(GroupChat.secret)
        assert r["errcode"] == 0


