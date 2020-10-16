
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
import random
logging.basicConfig(level=logging.INFO)


@allure.feature('集包-手动输入集包号')
class Test_kit_message_pickupReward(object):

    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/pack/valid/search/$[python]"P"+str(random.randint(0000000000,9999999999))$?isFromScanner=false'])
    @pytest.mark.run(order=55)
    def test_test_kit_message_pickupReward(self,headers,address):
        baseTest = BaseTestCase()
    
        address_new = baseTest.parameter_parser(address)
        # RedisBase().set('pack_no',address_new.split("/")[6].split("?")[0], ex=6000)

        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['api/courier/v1/pack/valid/search/$[python]"P"+str(random.randint(0000000000,9999999999))$?isFromScanner=false']

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

        # pack_no=RedisBase().get("pack_no")
        #存储集包号
        RedisBase().set('kit_valid_search_'   + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_[pack_no]',address_new.split("/")[6].split("?")[0], ex=6000)
        print("本次存储的随机集包号是：{0}".format(address_new.split("/")[6].split("?")[0]))

        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)

        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
