
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


@allure.feature('到付运费-ms-寄件网点-网点经理登录')
class Test_ms_auth_signin(object):

    @pytest.mark.parametrize("parameter",["{'login': '$[config]p_outlet_manager_login$', 'password': '$[config]p_outlet_manager_pwd$'}", "{'login': '$[config]c_outlet_manager_login$', 'password': '$[config]c_outlet_manager_pwd$'}", "{'login': '$[config]ms_houtai_login_user$', 'password': '$[config]ms_houtai_login_pwd$'}", "{'login': '$finance_login$', 'password': '$[config]finance_pwd$'}"])
    @pytest.mark.parametrize("headers",["{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'zh-CN'}", "{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'en-US'}", "{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'th-TN'}"])
    @pytest.mark.parametrize("address",['ms/api/auth/signin'])
    @pytest.mark.run(order=78)
    def test_test_ms_auth_signin(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'login': '$[config]p_outlet_manager_login$', 'password': '$[config]p_outlet_manager_pwd$'}", "{'login': '$[config]c_outlet_manager_login$', 'password': '$[config]c_outlet_manager_pwd$'}", "{'login': '$[config]ms_houtai_login_user$', 'password': '$[config]ms_houtai_login_pwd$'}", "{'login': '$finance_login$', 'password': '$[config]finance_pwd$'}"]
        
        _headers = ["{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'zh-CN'}", "{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'en-US'}", "{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'th-TN'}"]
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
                
        _address = ['ms/api/auth/signin']
            
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
        
        RedisBase().set('ms_auth_signin_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["session_id"]', resp.json()["data"]["session_id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        