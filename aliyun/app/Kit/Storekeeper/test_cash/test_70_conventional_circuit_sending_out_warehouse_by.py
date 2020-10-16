
import sys,os

from app.Kit.Courier.Utils.read_request_data import read_request_data
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


@allure.feature('常规线路发件出仓')
class Test_conventional_circuit_sending_out_warehouse_by(object):

    list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @allure.story("常规线路发件出仓功能_by")
    @pytest.mark.parametrize("i", list_i)
    @pytest.mark.run(order=70)
    def test_test_conventional_circuit_sending_out_warehouse_by(self, i):

        comm = Common_data()
        true = True
        false = False
        host = comm.each_parameter("host")
        # pno = read_request_data("courier_pno_number" + str(i), "pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        logging.info("常规线路发件出仓功能_by,订单号是：")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/" + str(pno) + "/shipment_warehouse_scan?isFromScanner=false"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "en-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        proof_id = comm.get_parameter_from_redis("vehicle_voucher_by_id")
        ti = int(time.time())
        van_id = dict(eval(comm.get_parameter_from_redis('outlet_vehicle_line_by_0_0_["data"]["items"][0]')))
        van_line_id = van_id["id"]
        data = {
            "exist_dst": true,
            "next_store_id": "TH01470301",
            "proof_id": proof_id,
            # "proof_id": "BKK3A3081",
            # "routed_at": 1586854291,
            "routed_at": ti,
            "shipment_switch": true,
            "skipped_enabled": false,
            "transportion_category": 1,
            # "van_line_id": "5d1dc8642d738a29e93034e9"
            "van_line_id": van_line_id
        }
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        logging.info("常规线路发件出仓功能,响应结果是:")
        logging.info(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["data"]).is_not_empty()
        
        # logging.info("jsonschema文件path:../data/jsonschema/70conventional_circuit_sending_out_warehouse_by.json")
        # with open("../data/jsonschema/70conventional_circuit_sending_out_warehouse_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        