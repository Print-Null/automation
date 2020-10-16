import configparser
import os
# from app.kit.Util.common_data import Common_data
import allure
from assertpy import assert_that
import requests
import logging

import pytest

from app.Kit.Util.common_data import Common_data

logging.basicConfig(level=logging.INFO)


@allure.feature('网点经理登入')
class Test_backyard_overtime_car_manager_auth_new_device_login(object):


    @pytest.mark.run(order=65)
    def test_test_backyard_overtime_car_manager_auth_new_device_login(self):

        true = True
        comm = Common_data()
        host = comm.each_parameter("backyard_host")
        url = host + "api/backyard/v1/auth/new_device_login"
        version = comm.each_parameter("by_version")
        headers = {
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json"
        }
        login = comm.each_parameter("Outlet_manager_login")
        password = comm.each_parameter("Outlet_manager_pwd")
        parameter = {
            "login": login,
            "password": password,
            "clientid": "8626360321249741575447597157",
            "clientsd": "1575447597168",
            "os": "android",
            "version": version
        }


        resp = requests.post(url=url, json=parameter, headers=headers, timeout=120, verify=False)
        # 将仓管员登入的sessionid保存
        # 获取sessionid 存储到.ini文件中
        session = resp.json()["data"]["sessionid"]
        logging.info(session)
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/by_warehouse_man_session.ini"

        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/by_warehouse_man_session.ini")

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/by_warehouse_man_session.ini"
        #
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("outlet_manager")
        # cf.set("outlet_manager", option="outlet_manager_session", value=str(session))
        # with open(session_path, "a+") as f:  # 可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)

        comm.write_parameter_to_redis("outlet_manager_session",session)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")