
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


@allure.feature('MS-网点经理登录-网点车线任务-打印出车凭证-2')
class Test_ms_van_proof(object):

    @pytest.mark.parametrize("parameter",['{\'id\': \'\', \'fleet_id\': \'$fleetId$\', \'van_line_id\': \'$ms_van_line_0_0_["data"]["items"][#headers#]["id"]$\', \'fleet_name\': \'$company_name$\', \'driver\': \'$[config]driver$\', \'plate_id\': \'$ms_fleet_van_0_0_["data"]["items"][0]["id"]$\', \'driver_phone\': \'$[config]driver_phone$\', \'departure_time\': \'$ms_proof_line_0_0_["data"]["expect_start_time"]$\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_0_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_0_2_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/van/proof'])
    @pytest.mark.run(order=64)
    def test_test_ms_van_proof(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'id\': \'\', \'fleet_id\': \'$fleetId$\', \'van_line_id\': \'$ms_van_line_0_0_["data"]["items"][#headers#]["id"]$\', \'fleet_name\': \'$company_name$\', \'driver\': \'$[config]driver$\', \'plate_id\': \'$ms_fleet_van_0_0_["data"]["items"][0]["id"]$\', \'driver_phone\': \'$[config]driver_phone$\', \'departure_time\': \'$ms_proof_line_0_0_["data"]["expect_start_time"]$\'}']
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_0_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_0_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_0_2_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        address_new = baseTest.parameter_parser(address, _headers, headers)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                
        _address = ['ms/api/fleet/van/proof']
            
        host = 'ms_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        if "application/json" in str(headers).lower():
            resp = requests.post(url = url, json = parameter_new, headers = headers_new, timeout = 120, verify = False)
        else:
            resp = requests.post(url = url, data = parameter_new, headers = headers_new, timeout = 120, verify = False)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("请求参数日志信息：")
        logging.info(parameter_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        
        RedisBase().set('ms_van_proof_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["id"]', resp.json()["data"]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        