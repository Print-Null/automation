
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


@allure.feature('到付运费-ms-提交疑难件网点登录-问题件处理-2')
class Test_ms_store_diff_tickets_stat(object):

    @pytest.mark.parametrize("parameter",["{'weight': 1100, 'oprate_result_category': 1, 'remark': '', 'settlement_type': 2, 'length': '', 'width': '', 'height': ''}"])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_1_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_1_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_1_2_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/store/diff_tickets/$ms_store_diff_tickets_#headers#_0_["data"]["items"][0]["id"]$/dispose'])
    @pytest.mark.run(order=83)
    def test_test_ms_store_diff_tickets_stat(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'weight': 1100, 'oprate_result_category': 1, 'remark': '', 'settlement_type': 2, 'length': '', 'width': '', 'height': ''}"]
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_1_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_1_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_1_2_0_["data"]["session_id"]$\'}']
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
                
        _address = ['ms/api/store/diff_tickets/$ms_store_diff_tickets_#headers#_0_["data"]["items"][0]["id"]$/dispose']
            
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
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        