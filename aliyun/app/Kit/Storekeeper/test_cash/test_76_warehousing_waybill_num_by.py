
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


@allure.feature('到件入仓-输入运单号')
class Test_warehousing_waybill_num_by(object):

    list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @pytest.mark.parametrize("i",list_i)
    @allure.story("到件入仓-输入运单号")
    @pytest.mark.run(order=76)
    def test_test_warehousing_waybill_num_by(self, i):

        comm = Common_data()
        false = False
        host = comm.each_parameter("host")
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/parcels/" + pno + "/arrival_warehouse_scan"
        session_id = comm.get_parameter_from_redis('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        ti = int(time.time())
        data = {
            # "proof_id": "BKK3A3163",
            "proof_id": conventional_circuit_id,
            # "routed_at": 1587020880,
            "routed_at": ti,
            "skipped_enabled": false
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("到件入仓-输入运单号,响应结果:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
        # with open("../data/jsonschema/76warehousing_waybill_num_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = res.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()






















        # baseTest = BaseTestCase()
        #
        # _parameter = []
        # address_new = baseTest.parameter_parser(address)
        #
        # _headers = ['{\'Accept-Language\': \'th-CN\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\', \'X-FLE-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
        # headers_new = baseTest.parameter_parser(headers)
        # headers_new = ast.literal_eval(headers_new)
        #
        # _address = ['api/courier/v1/fleet/proof/$vehicle_voucher_by_id$']
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
        # logging.info("jsonschema文件path:../data/jsonschema/75warehousing_vehicle_voucher_check_by.json")
        # with open("../data/jsonschema/75warehousing_vehicle_voucher_check_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        #