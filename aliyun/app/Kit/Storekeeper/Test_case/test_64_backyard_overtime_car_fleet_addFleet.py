
import sys, os
from datetime import datetime

from assertpy import assert_that

# from app.kit.Storekeeper.utils.read_ini_file_all import  read_all_ini
# from app.kit.Util.common_data import Common_data
from app.Kit.Util.common_data import Common_data

sys.path.append(os.getcwd())
import allure

import requests
import logging

import pytest


logging.basicConfig(level=logging.INFO)


@allure.feature('申请加班车')
class Test_backyard_overtime_car_fleet_addFleet(object):

    @pytest.mark.run(order=64)
    def test_test_backyard_overtime_car_fleet_addFleet(self):
        comm = Common_data()
        host = comm.each_parameter("backyard_host")
        url = host + "api/_/fleet/addFleet"
        # SESSION_ID = read_all_ini("by_warehouse_man_session", "by_warehouse", "warehouse_session")
        SESSION_ID = comm.get_parameter_from_redis("warehouse_session")
        headers = {
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json",
            "BY-PLATFORM": "FB_ANDROID",
            "X-BY-SESSION-ID": SESSION_ID
        }
        # start_store = read_all_ini("all_data","store_id_start","store_id")
        start_store = comm.get_parameter_from_redis("store_id_start")
        # end_store = read_all_ini("all_data","store_id_end","store_id")
        end_store = comm.get_parameter_from_redis("store_id_end")
        data = {
            "audit_type":1,
            "car_type":100,
            "capacity":44,
            "arrive_time": datetime.now().strftime('%Y-%m-%d 23:00'),
            "start_store": start_store,
            "end_store": end_store,
            "reason":"Auto加班车"

        }
        resp = requests.post(url=url, json=data, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["msg"]).is_equal_to("请求成功!")

