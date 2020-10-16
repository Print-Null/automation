
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


@allure.feature('ms协商结果赔偿')
class Test_ms_compensation_for_negotiation_result(object):

    @pytest.mark.parametrize("parameter",["{'negotiation_result_category': 6, 'payee_amount': '', 'payee_name': '', 'payee_phone': '', 'payee_account': '', 'payee_bank_category': '', 'remark': '继续配送并赔偿原因', 'doc_show_products': [], 'doc_claim_fs': []}"])
    @pytest.mark.parametrize("headers",['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_collection_outlets_login_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/customer/diff_tickets/$ms_communicated_with_outlets_0_0_0_["data"]["items"][0]["id"]$/consult'])
    @pytest.mark.run(order=117)
    def test_test_ms_compensation_for_negotiation_result(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'negotiation_result_category': 6, 'payee_amount': '', 'payee_name': '', 'payee_phone': '', 'payee_account': '', 'payee_bank_category': '', 'remark': '继续配送并赔偿原因', 'doc_show_products': [], 'doc_claim_fs': []}"]
        
        _headers = ['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_collection_outlets_login_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                
        _address = ['ms/api/customer/diff_tickets/$ms_communicated_with_outlets_0_0_0_["data"]["items"][0]["id"]$/consult']
            
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
        