
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


@allure.feature('ms网点经理-提交疑难件（货物丢失）-KAM訂單')
class Test_ms_outlet_manager_submits_difficult_parts(object):

    @pytest.mark.parametrize("parameter",['{\'difficulty_marker_category\': 22, \'remark\': \'自动化货物丢失，自动化货物丢失\', \'image_keys\': [], \'pno\': \'$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$\', \'delivery_staff_id\': \'\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_collection_outlets_login_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/store/parcel/difficulty_submission'])
    @pytest.mark.run(order=232)
    def test_test_ms_outlet_manager_submits_difficult_parts(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'difficulty_marker_category\': 22, \'remark\': \'自动化货物丢失，自动化货物丢失\', \'image_keys\': [], \'pno\': \'$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$\', \'delivery_staff_id\': \'\'}']
        
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
                
        _address = ['ms/api/store/parcel/difficulty_submission']
            
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
        