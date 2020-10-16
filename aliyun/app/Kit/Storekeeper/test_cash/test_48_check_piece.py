
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


@allure.feature('查单')
class Test_check_piece(object):


    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("查单")
    @pytest.mark.run(order=48)
    def test_test_check_piece(self, i):
        comm = Common_data()
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        host = comm.each_parameter("host")
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/parcels/" + pno + "/find?isFromScanner=false"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        resp = requests.get(url=url, headers=header, verify=False)
        logging.info("url日志信息:")
        logging.info(url)
        logging.info("请求头是：")
        logging.info(header)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        # logging.info("jsonschema文件path:../data/jsonschema/48check_piece.json")
        # with open("../data/jsonschema/48check_piece.json", "r", encoding="utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance=resp.json(), schema=shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()




















        #
        # baseTest = BaseTestCase()
        #
        # _parameter = []
        # address_new = baseTest.parameter_parser(address)
        #
        # _headers = ['{\'Accept-Language\': \'th-CN\', \'X-FLE-SESSION-ID\': \'$storekeeper_login_0_0_0_["data"]["sessionid"]$\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\', \'Content-Type\': \'application/json\', \'X-DEVICE-ID\': \'8673510346528821571665712622\'}']
        # headers_new = baseTest.parameter_parser(headers)
        # headers_new = ast.literal_eval(headers_new)
        #
        # _address = ['api/courier/v1/staff/material/desc?itemCode=4&businessDate=$[python]str(datetime.date.today())$&pageNum=1&pageSize=20']
        #
        # host = 'host'
        # host = baseTest.get_host(host)
        # url_data = host + address_new
        # url = baseTest.parameter_parser(url_data)
        # logging.info("url日志信息:")
        # logging.info(url)
        # resp = requests.get(url=url, headers=headers_new, verify=False, timeout=120)
        # logging.info("请求头是：")
        # logging.info(headers_new)
        # logging.info("响应结果日志信息：")
        # logging.info(resp.json())
        #
        # assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        #
        # assert_that(resp.status_code).is_equal_to(200)
        #
        # assert_that(resp.json()["code"]).is_equal_to(1)
        #
        # if "zh" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        # elif "th" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        # elif "en" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        #
        # logging.info("jsonschema文件path:../data/jsonschema/47material_sold_details.json")
        # with open("../data/jsonschema/47material_sold_details.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        #