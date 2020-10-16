
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


@allure.feature('C客户的快递员登录kit')
class Test_kit_user_sender_courier_new_device_login_cn(object):

    @pytest.mark.parametrize("parameter",['{\'login\': \'$app_user_sender_ticket_pickup_list_cn_0_0_["data"]["list"][0]["staff_info_id"]$\', \'password\': \'$[config]kit_user_pw$\', \'clientid\': \'$[config]kit_user_clientid$\', \'clientsd\': \'$[config]kit_user_clientsd$\', \'os\': \'android\', \'version\': \'$[config]kit_version$\'}'])
    @pytest.mark.parametrize("headers",["{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'en-US'}"])
    @pytest.mark.parametrize("address",['/api/courier/v1/auth/new_device_login'])
    @pytest.mark.run(order=357)
    def test_test_kit_user_sender_courier_new_device_login_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'login\': \'$app_user_sender_ticket_pickup_list_cn_0_0_["data"]["list"][0]["staff_info_id"]$\', \'password\': \'$[config]kit_user_pw$\', \'clientid\': \'$[config]kit_user_clientid$\', \'clientsd\': \'$[config]kit_user_clientsd$\', \'os\': \'android\', \'version\': \'$[config]kit_version$\'}']
        
        _headers = ["{'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'en-US'}"]
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
        
        RedisBase().set('kit_user_sender_courier_new_device_login_cn_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        
        RedisBase().set('kit_user_sender_courier_new_device_login_cn_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["tid"]', resp.json()["data"]["tid"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        