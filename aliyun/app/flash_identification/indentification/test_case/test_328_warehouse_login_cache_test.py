
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


@allure.feature('仓管员登入')
class Test_warehouse_login(object):

    @pytest.mark.parametrize("parameter",["{'login': '$[config]indentifi_kit_warehouse_usr$', 'password': '$[config]indentifi_kit_warehouse_pwd$', 'clientid': '8698940239062391583120286987', 'clientsd': '1583120286995', 'os': 'android', 'version': '$[config]login_version$'}"])
    @pytest.mark.parametrize("headers",["{'content-type': 'application/json', 'Accept-Language': 'zh-CN'}"])
    @pytest.mark.parametrize("address",['api/courier/v1/auth/new_device_login'])
    @pytest.mark.run(order=328)
    def test_test_warehouse_login(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'login': '$[config]indentifi_kit_warehouse_usr$', 'password': '$[config]indentifi_kit_warehouse_pwd$', 'clientid': '8698940239062391583120286987', 'clientsd': '1583120286995', 'os': 'android', 'version': '$[config]login_version$'}"]
        
        _headers = ["{'content-type': 'application/json', 'Accept-Language': 'zh-CN'}"]
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
                
        _address = ['api/courier/v1/auth/new_device_login']
            
        host = 'host'
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
        
        RedisBase().set('warehouse_login_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        