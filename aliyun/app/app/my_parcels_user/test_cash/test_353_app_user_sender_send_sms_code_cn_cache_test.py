
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


@allure.feature('APP端C客户获取短信验证码')
class Test_app_user_sender_send_sms_code_cn(object):

    @pytest.mark.parametrize("parameter",["{'version': '$[config]app_version$', 'os': 'ios', 'clientsd': '$[config]user_clientsd$', 'clientid': '$[config]app_clientid$', 'image_code': '6666', 'mobile': '$[config]user_sender_phone$', 'type': 2}"])
    @pytest.mark.parametrize("headers",["{'content-type': 'application/json', 'Accept-Language': 'en-US'}"])
    @pytest.mark.parametrize("address",['/api/user/v1/auth/send_sms_code'])
    @pytest.mark.run(order=353)
    def test_test_app_user_sender_send_sms_code_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'version': '$[config]app_version$', 'os': 'ios', 'clientsd': '$[config]user_clientsd$', 'clientid': '$[config]app_clientid$', 'image_code': '6666', 'mobile': '$[config]user_sender_phone$', 'type': 2}"]
        
        _headers = ["{'content-type': 'application/json', 'Accept-Language': 'en-US'}"]
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
                
        _address = ['/api/user/v1/auth/send_sms_code']
            
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
        
        logging.info("jsonschema文件path:../data/jsonschema/3_app_user_sender_send_sms_code_cn.json")
        with open("../data/jsonschema/3_app_user_sender_send_sms_code_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        