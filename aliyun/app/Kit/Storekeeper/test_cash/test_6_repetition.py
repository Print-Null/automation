import sys, os

from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")
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


@allure.feature('复称功能')
class Test_receipt_and_entry(object):
    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
              30, 31, 32, 33, 34]

    @allure.story("复称功能")
    @pytest.mark.parametrize("i", list_i)
    @pytest.mark.run(order=6)
    def test_test_receipt_and_entry(self, i):
        comm = Common_data()
        false = False
        host = comm.each_parameter("host")
        pno = read_request_data("courier_pno_number" + str(i))
        logging.info("复称接口，读取到的订单号是：")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/" + str(pno) + "/store_keeper_update_weight"
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        data = {
            "height": 1,
            "length": 1,
            "skipped_enabled": false,
            "skipping_tips": [],
            "weight": 4000,
            "width": 1
        }

        resp = requests.request("PATCH", url=url, headers=header, json=data, verify=False)
        logging.info("请求头是：")
        logging.info(header)
        logging.info("请求参数日志信息：")
        logging.info(data)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        # logging.info("jsonschema文件path:../data/jsonschema/4storekeeper_login.json")
        # with open("../data/jsonschema/6repetition.json", "r", encoding="utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance=resp.json(), schema=shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        #