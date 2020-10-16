import json

import allure
import pytest
import requests
from assertpy import assert_that

from app.backyard.test_backstage.util.read_ini import read_ini
from app.backyard.test_backstage.util.read_json_file import read_json_file
from common.readconfig import ReadConfig
from utils import redisbase
import time

from utils.redisbase import RedisBase


@allure.feature("修改快递员账号")
class Test_Bi_Update_warehouse_1():

    def setup(self):
        # self.session_bi = read_ini("bi_login","token","token")
        self.session_bi = RedisBase().get("bi_login")
        self.redisObj = redisbase.RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.host = ReadConfig().get_config(self.runenv_py, "fbi_host")
        self.courier = ReadConfig().get_config(self.runenv_py, "courier")
    @pytest.mark.run(order=5)
    def test_bi_update_warehouse_1(self):
        null = None
        time_bi = int(time.time())
        # url = self.host + "v1/staffs/create?lang=&time="+str(time_bi)+"&auth=92f1ff3bbff587d3c33bd70366ef33c7&fbid=10000&_view=formal"
        url = self.host + "v1/staffs/create?lang=&time="+str(time_bi)+"&auth=92f1ff3bbff587d3c33bd70366ef33c7&fbid=10000&_view=formal"
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Authorization": "Bearer " + self.session_bi,
            "Content-Type": "application/json;charset=UTF-8"
        }

        data_te = json.dumps(read_json_file("courier_te")) #测试环境仓管
        print(data_te)
        print(type(data_te))
        if self.runenv_py == "trunk":
            resp = requests.post(url=url, headers=header, data=data_te, verify=False)
            print(resp.json())
            assert_that(resp.json()["code"]).is_equal_to(0)
            assert_that(resp.json()["body"]["staff_info_id"]).is_equal_to(int(self.courier))
        elif self.runenv_py == "training":
            data_tra = json.dumps(read_json_file("courier_tra")) #测试环境仓管
            resp_tra = requests.post(url=url, headers=header, data=data_tra, verify=False)
            print(resp_tra.json())
            assert_that(resp_tra.json()["code"]).is_equal_to(0)
            assert_that(resp_tra.json()["body"]["staff_info_id"]).is_equal_to(int(self.courier))



