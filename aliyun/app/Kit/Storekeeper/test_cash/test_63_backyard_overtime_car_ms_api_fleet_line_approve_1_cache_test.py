
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


@allure.feature('加班车申请（中控审批界面）')
class Test_backyard_overtime_car_ms_api_fleet_line_approve_1(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'en-US\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve/$backyard_overtime_car_ms_fleet_line_approve_0_0_["data"]["items"][-1]["id"]$'])
    @pytest.mark.run(order=63)
    def test_test_backyard_overtime_car_ms_api_fleet_line_approve_1(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'en-US\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/fleet/line/approve/$backyard_overtime_car_ms_fleet_line_approve_0_0_["data"]["items"][-1]["id"]$']
        
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
        
        RedisBase().set('backyard_overtime_car_ms_api_fleet_line_approve_1_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["start_store"]', resp.json()["data"]["start_store"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_api_fleet_line_approve_1_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["end_store"]', resp.json()["data"]["end_store"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_api_fleet_line_approve_1_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["car_type"]', resp.json()["data"]["car_type"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_api_fleet_line_approve_1_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["car_type_text"]', resp.json()["data"]["car_type_text"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        # logging.info("jsonschema文件path:../data/jsonschema/63backyard_overtime_car_ms_api_fleet_line_approve_1.json")
        # with open("../data/jsonschema/63backyard_overtime_car_ms_api_fleet_line_approve_1.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        