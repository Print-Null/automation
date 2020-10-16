
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


@allure.feature('ms待网点沟通')
class Test_ms_communicated_with_outlets(object):

    @pytest.mark.parametrize("parameter",['{\'states\': [], \'pno\': \'$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_collection_outlets_login_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/customer/diff_tickets/kam'])
    @pytest.mark.run(order=376)
    def test_test_ms_communicated_with_outlets(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'states\': [], \'pno\': \'$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}']
        parameter_new = baseTest.parameter_parser(parameter)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        
        _headers = ['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_collection_outlets_login_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/customer/diff_tickets/kam']
            
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
        
        RedisBase().set('ms_communicated_with_outlets_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["id"]', resp.json()["data"]["items"][0]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        if resp.json()["data"]["items"][0]["state_text"] == "转交闪速系统(丢失类)":
            assert_that(resp.json()["data"]["items"][-1]["state_text"] == "转交闪速系统(丢失类)").is_true()
        else:
            assert_that(resp.json()["data"]["items"][0]["state_text"] == "未处理").is_true()
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        