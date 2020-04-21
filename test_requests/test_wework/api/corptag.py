import requests
from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.wework import WeWork


class CorpTag(BaseApi):
    secret = "sFX48HCSBF7P3v0vmYdoL_fYdaJ8ZeQAFdqDkk8-FUI"
    token = WeWork.get_token(secret)

    def __init__(self):
        self.data = self.api_load(r"D:\MyProjects\test_requests\test_wework\api\corptag.yaml")
        self.data["get"]["params"]["access_token"] = self.token
        # print("\n打印初始化的data", self.data)

    def get_corptag(self):
        url_get = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        r = requests.post(url_get, params={"access_token": self.token})
        self.format(r)
        return r.json()

    # 通过数据驱动实现获取企业标签的功能
    def get_api(self):
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

    def update_corptag(self):
        pass

    def delete_corptag(self, tag_id=[], group_id=[]):
        url_delete = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        r = requests.post(url_delete, params={"access_token": self.token},
                          json={"group_id": group_id,
                                "tag_id": tag_id
                                }
                          )
        self.format(r)
        return r.json()
