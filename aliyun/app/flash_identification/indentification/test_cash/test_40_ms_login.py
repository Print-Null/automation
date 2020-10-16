import configparser
import logging
import os

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase

@allure.feature('ms登入')
class Test_Ms_Login():
    logging.basicConfig(level=logging.INFO)

    @pytest.mark.run(order=40)
    def test_ms_login(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/auth/signin"
        header = {
            "Content-Type": "application/json"
        }
        user = comm.each_parameter("ms_login_user")
        pwd = comm.each_parameter("ms_login_pwd")
        data ={"login": user, "password": pwd}
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        RedisBase().set("ms_login_indentification", resp.json()["data"]["session_id"], ex=6000)
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["data"]).is_not_none()



