
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


@allure.feature('APP端C客户的收件人登入')
class Test_app_user_receiver_login_cn(object):

    @pytest.mark.parametrize("parameter",["{'version': '$[config]app_version$', 'os': 'ios', 'clientsd': '$[config]user_clientsd$', 'clientid': '$[config]app_clientid$', 'sms_code': '$[config]user_textCode$', 'mobile': '$[config]user_receiver_phone$', 'bc': 'enterprise', 'deviceinfo': {'device_model': '$[config]app_device_model$', 'os_version': '$[config]app_os_version$', 'net_work': 'WiFi', 'idfa': '$[config]app_idfa$'}}"])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-Hans-CN', 'content-type': 'application/json'}"])
    @pytest.mark.parametrize("address",['/api/user/v1/auth/new_device_login'])
    @pytest.mark.run(order=28)
    def test_test_app_user_receiver_login_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'version': '$[config]app_version$', 'os': 'ios', 'clientsd': '$[config]user_clientsd$', 'clientid': '$[config]app_clientid$', 'sms_code': '$[config]user_textCode$', 'mobile': '$[config]user_receiver_phone$', 'bc': 'enterprise', 'deviceinfo': {'device_model': '$[config]app_device_model$', 'os_version': '$[config]app_os_version$', 'net_work': 'WiFi', 'idfa': '$[config]app_idfa$'}}"]
        
        _headers = ["{'Accept-Language': 'zh-Hans-CN', 'content-type': 'application/json'}"]
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
                
        _address = ['/api/user/v1/auth/new_device_login']
            
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
        
        RedisBase().set('app_user_receiver_login_cn_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        
        RedisBase().set('app_user_receiver_login_cn_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["tid"]', resp.json()["data"]["tid"], ex=6000)
        
        RedisBase().set('app_user_receiver_login_cn_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["profile"]["id"]', resp.json()["data"]["profile"]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        logging.info("jsonschema文件path:../data/jsonschema/28_app_user_receiver_login_cn.json")
        with open("../data/jsonschema/28_app_user_receiver_login_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        