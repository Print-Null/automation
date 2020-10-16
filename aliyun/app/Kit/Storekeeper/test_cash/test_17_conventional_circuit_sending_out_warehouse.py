
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


@allure.feature('网点车线任务列表')
class Test_conventional_circuit_sending_out_warehouse(object):

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    @allure.story("常规线路发件出仓功能")
    @pytest.mark.parametrize("i", list_i)
    @pytest.mark.run(order=17)
    def test_test_conventional_circuit_sending_out_warehouse(self, i):
        comm = Common_data()
        true = True
        false = False
        host = comm.each_parameter("host")
        pno = read_request_data("courier_pno_number" + str(i))
        logging.info("新建常规线路获取到的订单号是")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/" + str(pno) + "/shipment_warehouse_scan?isFromScanner=false"
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }

        proof_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        ti = int(time.time())
        van_id = dict(eval(comm.get_parameter_from_redis('ms_generate_vehicle_voucher_1_0_0_["data"]["items"][0]')))
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
            "van_line_id": str(van_line_id)
        }
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        logging.info(resp.json())
        # logging.info("jsonschema文件path:../data/jsonschema/17conventional_circuit_sending_out_warehouse.json")
        # with open("../data/jsonschema/17conventional_circuit_sending_out_warehouse.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
