
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


@allure.feature('bi网点经理工单列表页面->工单回复未找到')
class Test_ms_work_order_reply_not_found(object):

    @pytest.mark.parametrize("parameter",["{}"])
    @pytest.mark.parametrize("headers",["{'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': '$indentifi_manager_PHPSESSID$'}"])
    @pytest.mark.parametrize("address",['workorder/info_reply_save?order_id=$ms_work_order_list_page_0_0_["data"]["DataList"][0]["order_id"]$&content=自动化未找到&img_arr=[{"bucket_name":"fle-staging-asset-internal","object_key":"workOrder/1594265809-225bacde30694829ad9cb0290d7d7fb5.jpg"}]&seek_status=1'])
    @pytest.mark.run(order=400)
    def test_test_ms_work_order_reply_not_found(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{}"]
        
        _headers = ["{'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': '$indentifi_manager_PHPSESSID$'}"]
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
                
        _address = ['workorder/info_reply_save?order_id=$ms_work_order_list_page_0_0_["data"]["DataList"][0]["order_id"]$&content=自动化未找到&img_arr=[{"bucket_name":"fle-staging-asset-internal","object_key":"workOrder/1594265809-225bacde30694829ad9cb0290d7d7fb5.jpg"}]&seek_status=1']
            
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
        
        assert_that(resp.json()["code"]).is_equal_to(0)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        