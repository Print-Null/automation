
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


@allure.feature('ms-查找岛屿的邮编')
class Test_ms_setting_district(object):

    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_2_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/setting/district?name=&pageSize=20&pageNum=1&upcountry=&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&keyWord=$island_postal_code$'])
    @pytest.mark.run(order=39)
    def test_test_ms_setting_district(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_2_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/setting/district?name=&pageSize=20&pageNum=1&upcountry=&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&keyWord=$island_postal_code$']
            
        host = 'ms_host'
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
        
        RedisBase().set('ms_setting_district_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["postal_code"]', resp.json()["data"]["items"][0]["postal_code"], ex=6000)
        
        RedisBase().set('ms_setting_district_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["code"]', resp.json()["data"]["items"][0]["code"], ex=6000)
        
        RedisBase().set('ms_setting_district_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["city_code"]', resp.json()["data"]["items"][0]["city_code"], ex=6000)
        
        RedisBase().set('ms_setting_district_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["city_name"]', resp.json()["data"]["items"][0]["city_name"], ex=6000)
        
        RedisBase().set('ms_setting_district_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["province_code"]', resp.json()["data"]["items"][0]["province_code"], ex=6000)
        
        RedisBase().set('ms_setting_district_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["province_name"]', resp.json()["data"]["items"][0]["province_name"], ex=6000)
        
        RedisBase().set('ms_setting_district_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["country_code"]', resp.json()["data"]["items"][0]["country_code"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        