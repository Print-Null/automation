
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


@allure.feature('APP端C客户获取图片验证码')
class Test_app_user_get_image_code(object):

    @pytest.mark.parametrize("parameter",["{'version': '$[config]app_version$', 'os': 'ios', 'clientsd': '$[config]user_clientsd$', 'clientid': '$[config]app_clientid$', 'mobile': '$[config]user_phone$'}"])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-Hans-CN', 'content-type': 'application/json'}"])
    @pytest.mark.parametrize("address",['/api/user/v1/auth/get_image_code'])
    @pytest.mark.run(order=2)
    def test_test_app_user_get_image_code(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'version': '$[config]app_version$', 'os': 'ios', 'clientsd': '$[config]user_clientsd$', 'clientid': '$[config]app_clientid$', 'mobile': '$[config]user_phone$'}"]
        parameter_new = baseTest.parameter_parser(parameter)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        
        _headers = ["{'Accept-Language': 'zh-Hans-CN', 'content-type': 'application/json'}"]
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/user/v1/auth/get_image_code']
            
        host = 'app_host'
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
        