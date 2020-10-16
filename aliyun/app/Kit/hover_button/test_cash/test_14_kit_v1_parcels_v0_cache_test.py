
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


@allure.feature('交接-查看快件详情')
class Test_kit_v1_parcels_v0(object):

    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/parcels_v0/$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$'])
    @pytest.mark.run(order=14)
    def test_test_kit_v1_parcels_v0(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['api/courier/v1/parcels_v0/$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$']
            
        host = 'kit_host'
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
        