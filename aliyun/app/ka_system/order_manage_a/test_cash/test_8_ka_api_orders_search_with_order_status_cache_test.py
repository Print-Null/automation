
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


@allure.feature('大客户在订单管理的未发货下按订单状态筛选订单')
class Test_ka_api_orders_search_with_order_status(object):

    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['/ka/api/orders?state=0&pageSize=20&pageNum=1&startTime=&startCreatedTime=$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()-datetime.timedelta(hours=datetime.datetime.now().hour,minutes=datetime.datetime.now().minute,seconds=datetime.datetime.now().second,microseconds=datetime.datetime.now().microsecond)),"%Y-%m-%d %H:%M:%S"))))$&endCreatedTime=$[python]str(int(time.time()))$&endTime=', '/ka/api/orders?state=1&pageSize=20&pageNum=1&startTime=&startCreatedTime=$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()-datetime.timedelta(hours=datetime.datetime.now().hour,minutes=datetime.datetime.now().minute,seconds=datetime.datetime.now().second,microseconds=datetime.datetime.now().microsecond)),"%Y-%m-%d %H:%M:%S"))))$&endCreatedTime=$[python]str(int(time.time()))$&endTime='])
    @pytest.mark.run(order=8)
    def test_test_ka_api_orders_search_with_order_status(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/ka/api/orders?state=0&pageSize=20&pageNum=1&startTime=&startCreatedTime=$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()-datetime.timedelta(hours=datetime.datetime.now().hour,minutes=datetime.datetime.now().minute,seconds=datetime.datetime.now().second,microseconds=datetime.datetime.now().microsecond)),"%Y-%m-%d %H:%M:%S"))))$&endCreatedTime=$[python]str(int(time.time()))$&endTime=', '/ka/api/orders?state=1&pageSize=20&pageNum=1&startTime=&startCreatedTime=$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()-datetime.timedelta(hours=datetime.datetime.now().hour,minutes=datetime.datetime.now().minute,seconds=datetime.datetime.now().second,microseconds=datetime.datetime.now().microsecond)),"%Y-%m-%d %H:%M:%S"))))$&endCreatedTime=$[python]str(int(time.time()))$&endTime=']
            
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
        