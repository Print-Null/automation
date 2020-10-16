
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


@allure.feature('待完成-派件、speed/pri')
class Test_kit_ticket_unfinished_list(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/ticket/simplified_list?abnormal_state=2'])
    @pytest.mark.run(order=304)
    def test_test_kit_ticket_unfinished_list(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['api/courier/v1/ticket/simplified_list?abnormal_state=2']
            
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
        assert_that(resp.json()["data"]["unfinished"]).is_equal_to(2)
        # assert_that(str(resp.json()["data"]["delivery"][0]["pno"])).is_equal_to(RedisBase().get('kit_pickups_parcel_1_0_0_["data"]["parcel_info"]["pno"]'))
        # assert_that(str(resp.json()["data"]["delivery"][0]["speed_enabled"]).lower()).is_equal_to("true")
        # assert_that(str(resp.json()["data"]["delivery"][1]["pno"])).is_equal_to(RedisBase().get('kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]'))
        # assert_that(str(resp.json()["data"]["delivery"][1]["speed_enabled"]).lower()).is_equal_to("false")

        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")

        