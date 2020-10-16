
import sys,os

from app.Kit.Courier.Utils.read_request_data import read_request_data
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


@allure.feature('交接')
class Test_delivery_note_handover(object):

    list_i = [10, 11, 12, 13, 14, 15, 16, 17]
    @pytest.mark.parametrize("i", list_i)
    @allure.story("交接")
    @pytest.mark.run(order=35)
    def test_test_delivery_note_handover(self, i):
        comm = Common_data()
        false = False
        true = True
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219cn8a/delivery_ticket_creation_scan"
        url = host + "api/courier/v1/parcels/" + pno + "/delivery_ticket_creation_scan"
        logging.info("交接,订单号是：")
        logging.info(pno)
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id('storekeeper_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        ti = int(time.time())
        data = {
            "continue_de_enabled": false,
            "openned": true,
            # "routed_at": 1587032057,
            "routed_at": str(ti),
            "skipped_enabled": false
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("请求头是：")
        logging.info(header)
        logging.info("请求参数日志信息：")
        logging.info(data)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["code"]).is_equal_to(1)

        # logging.info("jsonschema文件path:../data/jsonschema/34pre_problem_piece_short_delivery.json")
        # with open("../data/jsonschema/35delivery_note_handover.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()


