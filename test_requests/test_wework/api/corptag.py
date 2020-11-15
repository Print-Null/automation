import requests
from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.wework import WeWork
import os


class CorpTag(BaseApi):
    secret = "sFX48HCSBF7P3v0vmYdoL_fYdaJ8ZeQAFdqDkk8-FUI"
    token = WeWork.get_token(secret)

    def __init__(self):
        old_dir = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("api")[0] + "/api/")
        corptag_dir = os.path.join(old_dir, "corptag.yaml")
        self.data = self.api_load(corptag_dir)

    def get_corptag(self):
        url_get = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        r = requests.post(url_get, params={"access_token": self.token})
        self.format(r)
        return r.json()

    # 通过数据驱动实现获取企业标签的功能
    def get_api(self, **kwargs):
        self.data["get"]["params"]["access_token"] = self.token
        return self.api_send(self.data['get'])

    def add_corptag(self, tag_name, name="demo1", **kwargs):
        url_add = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        json_data = {
            "group_name": name,
            "tag": [{"name": tag_name}]
        }
        json_data.update(kwargs)
        r = requests.post(url_add, params={"access_token": self.token},
                          json=json_data)
        self.format(r)
        return r.json()

    # 通过数据驱动实现添加企业标签的功能
    def add_api(self, tag_name, **kwargs):
        self.params["name"] = tag_name
        self.data["add"]["params"]["access_token"] = self.token
        return self.api_send(self.data["add"])

    def update_corptag(self, tag_id, newname):
        self.params["tag_id"] = tag_id
        self.params["newname"] = newname
        self.data["update"]["params"]["access_token"] = self.token
        return self.api_send(self.data["update"])

    def delete_corptag(self, tag_id=[], group_id=[]):
        url_delete = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        r = requests.post(url_delete, params={"access_token": self.token},
                          json={"group_id": group_id,
                                "tag_id": tag_id
                                }
                          )
        self.format(r)
        return r.json()

    # 通过数据驱动实现删除企业标签的功能
    def delete_api(self, tag_id: list, group_id: list):
        self.params["tag_id"] = tag_id
        self.params["group_id"] = group_id
        self.data["delete"]["params"]["access_token"] = self.token
        return self.api_send(self.data["delete"])
