
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


@allure.feature('收件入仓')
class Test_receipt_and_entry(object):
    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
              30, 31, 32, 33, 34]
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("i", list_i)
    def test_test_receipt_and_entry(self, i):
        comm = Common_data()
        false = False
        pno = read_request_data("courier_pno_number" + str(i))
        logging.info(pno)
        host = comm.each_parameter("host")
        url = "api/courier/v1/parcels/" + str(pno) + "/receive_warehouse_scan"
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        logging.info(session_id)
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        ti = int(time.time())
        data = {
            "routed_at": ti,
            "skipped_enabled": false
        }
        resp = requests.post(url=host + url, headers=header, json=data, verify=False)
        logging.info(resp.json())
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        # logging.info("jsonschema文件path:../data/jsonschema/4storekeeper_login.json")
        # with open("../data/jsonschema/5receipt_and_entry.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()