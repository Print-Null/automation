import json

import pytest
import requests
from assertpy import assert_that

from app.backyard.test_backstage.util.read_ini import read_ini
from app.backyard.test_backstage.util.read_json_file import read_json_file
from common.readconfig import ReadConfig
from utils import redisbase
from utils.redisbase import RedisBase


class Test_Ms_Update_Manager():
    def setup(self):
        self.redisObj = redisbase.RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.host = ReadConfig().get_config(self.runenv_py, "ms_host")

    @pytest.mark.run(order=7)
    def test_ms_manager(self):
        url_te = self.host + "ms/api/setting/store/manager/TH01010314"
        # url_tra = self.host + "ms/api/setting/store/manager/TH01280201"
        url_tra = self.host + "ms/api/setting/store/manager/TH74040201"
        # self.ms_session = read_ini("bi_login","ms_token","ms_token")
        self.ms_session = self.redisObj.get("ms_token")
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json;charset=UTF-8",
            "X-MS-SESSION-ID": self.ms_session
        }
        print(self.runenv_py)
        if self.runenv_py == 'trunk':
            data_te = json.dumps(read_json_file("ms_update_manage_te"))  # 测试环境仓管
            resp_te = requests.post(url=url_te, data=data_te, headers=header, verify=False)
            print(resp_te.json())
            assert_that(resp_te.json()["code"]).is_equal_to(1)
            assert_that(resp_te.json()["message"]).is_equal_to("success")
            assert_that(resp_te.json()["data"]).is_none()
        elif self.runenv_py == 'training':
            # 将网点出纳设置为离职
            # 22419
            data_22419 = json.dumps(read_json_file("ms_data_22419_tra"))
            url_22419 = self.host + "ms/api/setting/store/staffs/22419/edit"
            res_22419 = requests.post(url=url_22419, headers=header, data=data_22419, verify=False)
            print("将网点出纳22419设置为离职,响应结果是：")
            print(res_22419.json())
            # 31725
            data_31725 = json.dumps(read_json_file("ms_data_31725_tra"))
            url_31725 = self.host + "ms/api/setting/store/staffs/31725/edit"
            res_31725 = requests.post(url=url_31725, data=data_31725, headers=header, verify=False)
            print("将网点出纳31725设置为离职,响应结果是：")
            print(res_31725.json())
            data_tra = json.dumps(read_json_file("ms_update_manage_tra"))  # 预发布环境仓管
            resp_tra = requests.post(url=url_tra, data=data_tra, headers=header, verify=False)
            print(url_tra)
            print(header)
            print(resp_tra.json())
            assert_that(resp_tra.json()["code"]).is_equal_to(1)
            assert_that(resp_tra.json()["message"]).is_equal_to("success")
            assert_that(resp_tra.json()["data"]).is_none()
