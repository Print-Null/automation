
import sys,os

from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
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


@allure.feature('填单接口')
class Test_courier_write_order(object):
    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @pytest.mark.parametrize("i", list_i)
    @allure.title("填单接口")
    @pytest.mark.run(order=2)
    def test_test_courier_write_order(self, i):

        comm = Common_data()
        session_id = read_courier_session_id('courier_login_0_0_0_["data"]["sessionid"]')
        false = False
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/ticket/pickups/parcel"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        client_id = comm.each_parameter("client_id")
        data = {
            "article_category": 99,
            "call_duration": 0,
            "client_id": client_id,
            "cod_amount": 0,
            "cod_enabled": false,
            "customer_type_category": 2,
            "dst_city_code": "TH0502",
            "dst_country_code": "TH",
            "dst_detail_address": "2",
            "dst_district_code": "TH050201",
            "dst_name": "2",
            "dst_phone": "1346999281",
            "dst_postal_code": "13130",
            "dst_province_code": "TH05",
            "express_category": 1,
            "freight_insure_enabled": false,
            "height": 1,
            "insure_declare_value": 0,
            "insured": false,
            "length": 1,
            "settlement_category": 1,
            "skipping_tips": [],
            "src_city_code": "TH1101",
            "src_country_code": "TH",
            "src_detail_address": "1",
            "src_district_code": "TH110101",
            "src_name": "1",
            "src_phone": "1232311232",
            "src_postal_code": "26000",
            "src_province_code": "TH11",
            "total_amount": 4000,
            "weight": 2000,
            "width": 1
        }

        resp = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("填单接口返回的结果是：")
        logging.info(json.dumps(resp.json(), indent=4))
        logging.info("请求参数是：")
        logging.info(data)
        assert_that(resp.json()["message"]).is_equal_to("success")
        # logging.info("jsonschema文件path:../data/jsonschema/2courier_write_order.json")
        # with open("../data/jsonschema/2courier_write_order.json", "r", encoding="utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance=resp.json(), schema=shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        # 将ticket_pickup_id, pno 写入redis
        Common_data().write_parameter_to_redis("ticket_pickup_id" + str(i), resp.json()["data"]["ticket_pickup_id"])
        Common_data().write_parameter_to_redis("courier_pno_number" + str(i), resp.json()["data"]["parcel_info"]["pno"])
