
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


@allure.feature('拆包')
class Test_unpack(object):


    @pytest.mark.run(order=26)
    def test_test_unpack(self):
        comm = Common_data()
        pno_list = []
        true = True
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/unseal"
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        pack_num = comm.get_parameter_from_redis("pack_no")
        # 修改 list_i
        list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        for i in range(len(list_i)):
            pno = read_request_data("courier_pno_number" + str(i + 1))
            pno_list.append(pno)
        logging.info("订单号读取结果是：")
        logging.info(pno_list)

        data = {
            "continue_flag": true,
            # "pack_no": "P5712",
            "pack_no": pack_num,
            "recent_pnos": pno_list
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("请求头是：")
        logging.info(header)
        logging.info("请求参数：")
        logging.info(data)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        # with open("../data/jsonschema/26unpack.json", "r", encoding = "utf-8") as f:
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
        # _address = ['api/courier/v1/pack/unseal/verify/$pack_no$']
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
        # logging.info("jsonschema文件path:../data/jsonschema/26unpack.json")
        # with open("../data/jsonschema/26unpack.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        #