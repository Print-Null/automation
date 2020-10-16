
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


@allure.feature('backyard网点经理登入')
class Test_DC_warehouse_login(object):

    @pytest.mark.parametrize("parameter",["{'login': '$[config]DC_manager_login_usr$', 'password': '$[config]DC_manager_login_pwd$', 'clientid': '8626360321249741575447597157', 'clientsd': '1575447597168', 'os': 'android', 'version': '$[config]backyard_version$'}", "{'login': '$[config]by_warehose_man_end_login$', 'password': '$[config]by_warehose_man_end_pwd$', 'clientid': '8626360321249741575447597157', 'clientsd': '1575447597168', 'os': 'android', 'version': '$[config]backyard_version$'}"])
    @pytest.mark.parametrize("headers",["{'content-type': 'application/json', 'Accept-Language': 'zh-CN'}", "{'content-type': 'application/json', 'Accept-Language': 'en-US'}", "{'content-type': 'application/json', 'Accept-Language': 'th-CN'}"])
    @pytest.mark.parametrize("address",['api/backyard/v1/auth/new_device_login'])
    @pytest.mark.run(order=280)
    def test_test_DC_warehouse_login(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'login': '$[config]DC_manager_login_usr$', 'password': '$[config]DC_manager_login_pwd$', 'clientid': '8626360321249741575447597157', 'clientsd': '1575447597168', 'os': 'android', 'version': '$[config]backyard_version$'}", "{'login': '$[config]by_warehose_man_end_login$', 'password': '$[config]by_warehose_man_end_pwd$', 'clientid': '8626360321249741575447597157', 'clientsd': '1575447597168', 'os': 'android', 'version': '$[config]backyard_version$'}"]
        
        _headers = ["{'content-type': 'application/json', 'Accept-Language': 'zh-CN'}", "{'content-type': 'application/json', 'Accept-Language': 'en-US'}", "{'content-type': 'application/json', 'Accept-Language': 'th-CN'}"]
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
                
        _address = ['api/backyard/v1/auth/new_device_login']
            
        host = 'backyard_host'
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
        
        RedisBase().set('DC_warehouse_login_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/DC_warehouse_login.json")
        with open("../data/jsonschema/DC_warehouse_login.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        