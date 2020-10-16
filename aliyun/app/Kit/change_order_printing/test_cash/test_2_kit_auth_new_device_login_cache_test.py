
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


@allure.feature('kit-快递员、仓管员登入')
class Test_kit_auth_new_device_login(object):

    @pytest.mark.parametrize("parameter",["{'login': '$my_public_funds_courier_login$', 'password': '$[config]my_public_funds_courier_pwd$', 'clientid': '$[config]my_public_funds_courier_clientid$', 'clientsd': '$[config]my_public_funds_courier_clientsd$', 'os': '$[config]my_public_funds_courier_os$', 'version': '$[config]my_public_funds_courier_version$'}", "{'login': '$warehouse_keeper_login$', 'password': '$[config]warehouse_keeper_pwd$', 'clientid': '$[config]warehouse_keeper_clientid$', 'clientsd': '$[config]warehouse_keeper_clientsd$', 'os': '$[config]warehouse_keeper_os$', 'version': '$[config]warehouse_keeper_version$'}"])
    @pytest.mark.parametrize("headers",["{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'zh-CN'}", "{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'en-US'}", "{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'th-TN'}"])
    @pytest.mark.parametrize("address",['api/courier/v1/auth/new_device_login'])
    @pytest.mark.run(order=2)
    def test_test_kit_auth_new_device_login(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'login': '$my_public_funds_courier_login$', 'password': '$[config]my_public_funds_courier_pwd$', 'clientid': '$[config]my_public_funds_courier_clientid$', 'clientsd': '$[config]my_public_funds_courier_clientsd$', 'os': '$[config]my_public_funds_courier_os$', 'version': '$[config]my_public_funds_courier_version$'}", "{'login': '$warehouse_keeper_login$', 'password': '$[config]warehouse_keeper_pwd$', 'clientid': '$[config]warehouse_keeper_clientid$', 'clientsd': '$[config]warehouse_keeper_clientsd$', 'os': '$[config]warehouse_keeper_os$', 'version': '$[config]warehouse_keeper_version$'}"]
        
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
                
        _address = ['api/courier/v1/auth/new_device_login']
            
        host = 'kit_host'
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
        
        RedisBase().set('kit_auth_new_device_login_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        # logging.info("jsonschema文件path:../data/jsonschema/2_kit_login.json")
        # with open("../data/jsonschema/2_kit_login.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        