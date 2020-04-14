import json

import requests

from test_requests.test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    url_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww945dd462b685567d"
    token = dict()

    @classmethod
    def get_token(cls, secret):
        # if secret is None:
        #     return cls.token[secret]
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            cls.token[secret] = r["access_token"]
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(cls.url_token,
                         params={"corpid": cls.corpid, "corpsecret": secret})
        cls.format(r)
        return r.json()
