
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


@allure.feature('bi普通客服，闪速认定操作b来源无需追责')
class Test_bi_b_no_accountability(object):

    @pytest.mark.parametrize("parameter",["{}"])
    @pytest.mark.parametrize("headers",["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_bi_usr_PHPSESSID$'}"])
    @pytest.mark.parametrize("address",['parcelloseapi/not_lose?$test_1_1_iframe_0$&$test_1_1_iframe_2$&fbid=$[config]indentifi_bi_usr$&$test_1_1_iframe_1$&remark=a来源无需追责&task_id=$bi_qery_list_task_id$'])
    @pytest.mark.run(order=243)
    def test_test_bi_b_no_accountability(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{}"]
        
        _headers = ["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_bi_usr_PHPSESSID$'}"]
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
                
        _address = ['parcelloseapi/not_lose?$test_1_1_iframe_0$&$test_1_1_iframe_2$&fbid=$[config]indentifi_bi_usr$&$test_1_1_iframe_1$&remark=a来源无需追责&task_id=$bi_qery_list_task_id$']
            
        host = 'fbi_host_domain'
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
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("success")
        