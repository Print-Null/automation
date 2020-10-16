import configparser
import os

import allure
from assertpy import assert_that
import requests
import logging

import pytest

# from app.kit.Util.common_data import Common_data
from app.Kit.Util.common_data import Common_data

logging.basicConfig(level=logging.INFO)


@allure.feature('backyard登入,加班车申请，目的地网点')
class Test_backyard_overtime_car_auth_new_device_login_End():

    @pytest.mark.run(order=61)
    def test_test_backyard_overtime_car_auth_new_device_login_end(self):
        true = True
        comm = Common_data()
        host = comm.each_parameter("backyard_host")
        url = host + "api/backyard/v1/auth/new_device_login"

        headers = {
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json"
        }
        login = comm.each_parameter("Warehouse_man_personInfo_end_login")
        password = comm.each_parameter("Warehouse_man_personInfo_end_pwd")
        version = comm.each_parameter("by_version")
        parameter = {
            "login": login,
            "password": password,
            "clientid": "8626360321249741575447597157",
            "clientsd": "1575447597168",
            "os": "android",
            "version": version
        }
        resp = requests.post(url=url, json=parameter, headers=headers, timeout=120, verify=False)
        #将仓管员登入的sessionid保存
        # 获取sessionid 存储到.ini文件中
        session = resp.json()["data"]["sessionid"]
        logging.info(session)
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/by_warehouse_man_session.ini"
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("by_warehouse_end")
        # cf.set("by_warehouse_end", option="warehouse_session_end", value=str(session))
        # with open(session_path, "a+") as f:  #可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)
        comm.write_parameter_to_redis("warehouse_session_end",session)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
