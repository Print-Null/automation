
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


@allure.feature('大客户查看未发货的订单详情')
class Test_ka_api_orders_detail(object):

    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['/ka/api/orders/$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["id"]$/detail/'])
    @pytest.mark.run(order=14)
    def test_test_ka_api_orders_detail(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/ka/api/orders/$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["id"]$/detail/']
            
        host = 'ka_system_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        resp = requests.get(url=url, headers=headers_new, verify=False, timeout=120)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        