import json

import requests

from test_requests.test_wework.api.wework import WeWork


class Department:
    secret = "duV8doV0W2CcGtGAWrLFZmpj9lk7qtGnUKcnhqqSjts"

    def create_department(self, name, parentid, **kwargs):
        json_data = {"name": name, "parentid": parentid}
        json_data.update(kwargs)
        url_create = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        r = requests.post(url_create, params={"access_token": WeWork.get_token(self.secret)}, json=json_data)
        print(json.dumps(r.json(), indent=2))
        return r.json()

    def delete_department(self, id):
        url_delete = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(url_delete, params={"access_token": WeWork.get_token(self.secret), "id": id})
        print(json.dumps(r.json(), indent=2))
        return r.json()

    def update_department(self, id, name, **kwargs):
        json_data = {"id": id, "name": name}
        json_data.update(kwargs)
        url_update = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        r = requests.post(url_update, params={"access_token": WeWork.get_token(self.secret)}, json=json_data)
        print(json.dumps(r.json(), indent=2))
        return r.json()

    def check_department(self):
        url_check = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(url_check, params={"access_token": WeWork.get_token(self.secret)})
        print("以下是企业所有部门：", end="\n")
        print(json.dumps(r.json()["department"], ensure_ascii=False, indent=2))
        return r.json()
