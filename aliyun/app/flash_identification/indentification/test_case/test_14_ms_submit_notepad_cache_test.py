
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


@allure.feature('普通客服->ms提交记事本')
class Test_ms_submit_notepad(object):

    @pytest.mark.parametrize("parameter",['{\'pno\': \'$courier_write_order_2_0_0_["data"]["parcel_info"]["pno"]$\', \'grade\': \'\', \'channel_category\': 3, \'requester_category\': 1, \'customer_name\': \'自动化姓名\', \'customer_phone\': \'\', \'customer_email\': \'\', \'request_sup_type\': 22, \'request_sub_type\': 220, \'remark\': \'自动化快递丢失。自动化快递丢失。自动化快递丢失。\', \'opened\': False, \'back_visit_category\': \'\', \'need_ring_back\': False, \'assign_to_me\': False, \'need_close\': True, \'customer_team\': 1, \'images\': []}'])
    @pytest.mark.parametrize("headers",['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_general_customer_service_login_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/customer/issues/add'])
    @pytest.mark.run(order=14)
    def test_test_ms_submit_notepad(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'pno\': \'$courier_write_order_2_0_0_["data"]["parcel_info"]["pno"]$\', \'grade\': \'\', \'channel_category\': 3, \'requester_category\': 1, \'customer_name\': \'自动化姓名\', \'customer_phone\': \'\', \'customer_email\': \'\', \'request_sup_type\': 22, \'request_sub_type\': 220, \'remark\': \'自动化快递丢失。自动化快递丢失。自动化快递丢失。\', \'opened\': False, \'back_visit_category\': \'\', \'need_ring_back\': False, \'assign_to_me\': False, \'need_close\': True, \'customer_team\': 1, \'images\': []}']
        
        _headers = ['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_general_customer_service_login_0_0_0_["data"]["session_id"]$\'}']
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
                
        _address = ['ms/api/customer/issues/add']
            
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
        