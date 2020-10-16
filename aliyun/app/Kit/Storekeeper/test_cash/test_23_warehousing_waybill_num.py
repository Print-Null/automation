
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


@allure.feature('到件入仓->出车凭证校验')
class Test_warehousing_waybill_num(object):

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    @pytest.mark.parametrize("i",list_i)
    @allure.story("到件入仓-输入运单号")
    @pytest.mark.run(order=23)
    def test_test_warehousing_waybill_num(self, i):
        comm = Common_data()
        false = False
        host = comm.each_parameter("host")
        pno = read_request_data("courier_pno_number" + str(i))
        logging.info("到件入仓-输入运单号,获取的订单号是")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/" + pno + "/arrival_warehouse_scan"
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
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
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info(resp.json())
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.status_code).is_equal_to(200)

        assert_that(resp.json()["code"]).is_equal_to(1)

        # logging.info("jsonschema文件path:../data/jsonschema/23warehousing_waybill_num.json")
        # with open("../data/jsonschema/23warehousing_waybill_num.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()












        # baseTest = BaseTestCase()
        #
        # _parameter = []
        # address_new = baseTest.parameter_parser(address)
        #
        # _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$storekeeper_login_0_0_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\'}', '{\'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$storekeeper_login_0_0_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\'}', '{\'Accept-Language\': \'th-CN\', \'X-FLE-SESSION-ID\': \'$storekeeper_login_0_0_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\'}']
        # headers_new = baseTest.parameter_parser(headers)
        # headers_new = ast.literal_eval(headers_new)
        #
        # _address = ['api/courier/v1/fleet/proof/$vehicle_voucher_id$']
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
        # logging.info("jsonschema文件path:../data/jsonschema/23warehousing_waybill_num.json")
        # with open("../data/jsonschema/23warehousing_waybill_num.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        #