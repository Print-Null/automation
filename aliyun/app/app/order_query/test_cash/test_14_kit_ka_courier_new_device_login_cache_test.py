
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


@allure.feature('B客户的快递员登录kit')
class Test_kit_ka_courier_new_device_login(object):

    @pytest.mark.parametrize("parameter",['{\'login\': \'$app_ka_ticket_pickup_list_0_0_["data"]["list"][0]["staff_info_id"]$\', \'password\': \'$[config]kit_ka_pw$\', \'clientid\': \'$[config]kit_ka_clientid$\', \'clientsd\': \'$[config]kit_ka_clientsd$\', \'os\': \'android\', \'version\': \'$[config]kit_version$\'}'])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-CN', 'content-type': 'application/json; charset=UTF-8'}", "{'content-type': 'application/json', 'Accept-Language': 'en-US'}", "{'content-type': 'application/json', 'Accept-Language': 'th-CN'}"])
    @pytest.mark.parametrize("address",['/api/courier/v1/auth/new_device_login'])
    @pytest.mark.run(order=14)
    def test_test_kit_ka_courier_new_device_login(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'login\': \'$app_ka_ticket_pickup_list_0_0_["data"]["list"][0]["staff_info_id"]$\', \'password\': \'$[config]kit_ka_pw$\', \'clientid\': \'$[config]kit_ka_clientid$\', \'clientsd\': \'$[config]kit_ka_clientsd$\', \'os\': \'android\', \'version\': \'$[config]kit_version$\'}']
        
        _headers = ["{'Accept-Language': 'zh-CN', 'content-type': 'application/json; charset=UTF-8'}", "{'content-type': 'application/json', 'Accept-Language': 'en-US'}", "{'content-type': 'application/json', 'Accept-Language': 'th-CN'}"]
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
                
        _address = ['/api/courier/v1/auth/new_device_login']
            
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
        
        RedisBase().set('kit_ka_courier_new_device_login_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        
        RedisBase().set('kit_ka_courier_new_device_login_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["tid"]', resp.json()["data"]["tid"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/14_kit_ka_courier_new_device_login.json")
        with open("../data/jsonschema/14_kit_ka_courier_new_device_login.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        