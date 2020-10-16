
import sys,os
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


@allure.feature('网点车线任务列表by')
class Test_outlet_vehicle_line_by(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'Accept\': \'application/json, text/plain, */*\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-US\', \'Accept\': \'application/json, text/plain, */*\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Accept\': \'application/json, text/plain, */*\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/van/line/task?type=1&startDate=$[python]datetime.date.today()$&pageNum=1&pageSize=20'])
    @pytest.mark.run(order=68)
    def test_test_outlet_vehicle_line_by(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'Accept\': \'application/json, text/plain, */*\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-US\', \'Accept\': \'application/json, text/plain, */*\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Accept\': \'application/json, text/plain, */*\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/fleet/van/line/task?type=1&startDate=$[python]datetime.date.today()$&pageNum=1&pageSize=20']
        # _address = ['ms/api/fleet/van/line?sortingNo=&type=&originStoreId=&targetStoreId=&lineName=&pageSize=20&pageNum=1&passStoreId=']

        host = 'ms_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        resp = requests.get(url=url, headers=headers_new, verify=False, timeout=120)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        logging.info(_headers.index(headers))
        logging.info(_address.index(address))
        RedisBase().set('outlet_vehicle_line_by_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]', str(resp.json()["data"]["items"][0]), ex=6000)

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
        
        # logging.info("jsonschema文件path:../data/jsonschema/68outlet_vehicle_line_by.json")
        # with open("../data/jsonschema/68outlet_vehicle_line_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        