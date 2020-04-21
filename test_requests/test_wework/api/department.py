import requests

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.wework import WeWork


class Department(BaseApi):
    secret = "duV8doV0W2CcGtGAWrLFZmpj9lk7qtGnUKcnhqqSjts"
    token = WeWork.get_token(secret)

    def create_department(self, name, parentid, **kwargs):
        json_data = {"name": name, "parentid": parentid}
        json_data.update(kwargs)
        url_create = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        r = requests.post(url_create, params={"access_token": self.token}, json=json_data)
        self.format(r)
        return r.json()

    def delete_department(self, id):
        url_delete = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(url_delete, params={"access_token": self.token, "id": id})
        self.format(r)
        return r.json()

    def update_department(self, id, **kwargs):
        json_data = {"id": id}
        json_data.update(kwargs)
        url_update = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        r = requests.post(url_update, params={"access_token": self.token}, json=json_data)
        self.format(r)
        return r.json()

    def check_department(self):
        url_check = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(url_check, params={"access_token": self.token})
        print("以下是企业所有部门：", end="\n")
        self.format(r)
        return r.json()
