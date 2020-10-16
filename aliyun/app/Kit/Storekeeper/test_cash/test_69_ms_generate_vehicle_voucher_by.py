
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
class Test_ms_generate_vehicle_voucher_by(object):

    @allure.story("生成出车凭证功能")
    @pytest.mark.run(order=69)
    def test_test_ms_generate_vehicle_voucher_by(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/fleet/van/proof"
        SESSION_ID = comm.get_parameter_from_redis('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-CN",
            "Content-Type": "application/json;charset=UTF-8",
            "X-MS-SESSION-ID": SESSION_ID
        }
        null = None

        data = dict(eval(comm.get_parameter_from_redis('outlet_vehicle_line_by_0_0_["data"]["items"][0]')))
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
        vehicle_voucher_by_id = resp.json()["data"]["id"]
        comm.write_parameter_to_redis("vehicle_voucher_by_id", vehicle_voucher_by_id)
        logging.info("常规线路生成出车凭证接口响应结果是：")
        logging.info(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")

        # logging.info("jsonschema文件path:../data/jsonschema/69ms_generate_vehicle_voucher_by.json")
        # with open("../data/jsonschema/69ms_generate_vehicle_voucher_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        