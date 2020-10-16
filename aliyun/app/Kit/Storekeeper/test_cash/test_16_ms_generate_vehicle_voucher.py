
import sys,os

from app.Kit.Util.common_data import Common_data

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0]+"/flash")
import allure
from assertpy import assert_that
import requests
import logging
import ast
import json
import time
import pytest
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
                
logging.basicConfig(level=logging.INFO)


@allure.feature('生成出车凭证')
class Test_ms_generate_vehicle_voucher(object):


    @pytest.mark.run(order=16)
    def test_test_ms_generate_vehicle_voucher(self):
        comm = Common_data()
        # host = read_common("ms_host")
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/fleet/van/proof"
        # SESSION_ID = read_ms_session("ms", "ms_session")
        SESSION_ID = comm.get_parameter_from_redis('ms_login_0_0_0_["data"]["session_id"]')
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json;charset=UTF-8",
            "X-MS-SESSION-ID": SESSION_ID
        }
        null = None
        # data = read_ms_generate_vehicle_voucher("ms_generate_vehicle_voucher_actual.json")
        data = dict(eval(comm.get_parameter_from_redis('ms_generate_vehicle_voucher_1_0_0_["data"]["items"][0]')))

        fleet_id = data["fleet_id"]
        van_line_id = data["id"]
        fleet_name = data["fleet_name"]
        driver = data["driver"]
        plate_id = data["plate_id"]
        driver_phone = data["driver_phone"]
        departure_time = data["expect_start_time"]
        data_vehi = {
            "id": null,
            "fleet_id": fleet_id,
            "van_line_id": van_line_id,
            "fleet_name": fleet_name,
            "driver": driver,
            "plate_id": plate_id,
            "driver_phone": driver_phone,
            "departure_time": departure_time
        }
        logging.info("请求data是：")
        logging.info(data_vehi)
        resp = requests.post(url=url, json=data_vehi, headers=header, verify=False)
        logging.info("响应结果是：")
        logging.info(resp.json())
        vehicle_voucher_id = resp.json()["data"]["id"]
        comm.write_parameter_to_redis("vehicle_voucher_id", vehicle_voucher_id)
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        # with open("../data/jsonschema/16ms_generate_vehicle_voucher.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()

