
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


@allure.feature('ms后台中控登入')
class Test_backyard_overtime_car_ms_api_auth_signin(object):

    @pytest.mark.parametrize("parameter",["{'login': '$[config]ms_central_control_login$', 'password': '$[config]ms_central_control_pwd$'}"])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-CN', 'Accept-Accept': 'application/json, text/plain, */*'}", "{'Accept-Language': 'en-US', 'Accept-Accept': 'application/json, text/plain, */*'}", "{'Accept-Language': 'th-CN', 'Accept-Accept': 'application/json, text/plain, */*'}"])
    @pytest.mark.parametrize("address",['ms/api/auth/signin'])
    @pytest.mark.run(order=61)
    def test_test_backyard_overtime_car_ms_api_auth_signin(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'login': '$[config]ms_central_control_login$', 'password': '$[config]ms_central_control_pwd$'}"]
        
        _headers = ["{'Accept-Language': 'zh-CN', 'Accept-Accept': 'application/json, text/plain, */*'}", "{'Accept-Language': 'en-US', 'Accept-Accept': 'application/json, text/plain, */*'}", "{'Accept-Language': 'th-CN', 'Accept-Accept': 'application/json, text/plain, */*'}"]
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
        
        RedisBase().set('backyard_overtime_car_ms_api_auth_signin_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["session_id"]', resp.json()["data"]["session_id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        # logging.info("jsonschema文件path:../data/jsonschema/61backyard_overtime_car_ms_api_auth_signin.json")
        # with open("../data/jsonschema/61backyard_overtime_car_ms_api_auth_signin.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        