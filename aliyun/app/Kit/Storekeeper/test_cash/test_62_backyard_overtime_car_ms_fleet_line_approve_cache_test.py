
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


@allure.feature('ms后台加班车审批列表->查询展示')
class Test_backyard_overtime_car_ms_fleet_line_approve(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'en-US\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1&startTime=$[python]str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00"))$&endTime=$[python]str(datetime.datetime.now().strftime("%Y-%m-%d 23:59:59"))$'])
    @pytest.mark.run(order=62)
    def test_test_backyard_overtime_car_ms_fleet_line_approve(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'en-US\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1&startTime=$[python]str(datetime.datetime.now().strftime("%Y-%m-%d 00:00:00"))$&endTime=$[python]str(datetime.datetime.now().strftime("%Y-%m-%d 23:59:59"))$']
        
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
        
        RedisBase().set('backyard_overtime_car_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-1]["id"]', resp.json()["data"]["items"][-1]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        # logging.info("jsonschema文件path:../data/jsonschema/62backyard_overtime_car_ms_fleet_line_approve.json")
        # with open("../data/jsonschema/62backyard_overtime_car_ms_fleet_line_approve.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        