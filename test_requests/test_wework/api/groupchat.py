import json

import requests

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.wework import WeWork


class GroupChat(BaseApi):
    secret = "sFX48HCSBF7P3v0vmYdoL_fYdaJ8ZeQAFdqDkk8-FUI"

    def group_chat_list(self, offset=0, limit=100, **kwargs):
        json_data = {"offset": offset, "limit": limit}
        print("\n追加参数", kwargs)
        print("\n原始json_data数据", json_data)
        json_data.update(kwargs)
        print("\n追加参数后的json_data数据", json_data)
        url_groupchat = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(url_groupchat, params={"access_token": WeWork.get_token(self.secret)},
                          json=json_data)
        self.format(r)
        return r.json()

    def group_chat_detail(self, chat_id):
        url_detail = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(url_detail, params={"access_token": WeWork.get_token(self.secret)},
                          json={"chat_id": chat_id})
        self.format(r)
        return r.json()
