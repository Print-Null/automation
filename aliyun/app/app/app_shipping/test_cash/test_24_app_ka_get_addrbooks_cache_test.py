
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


@allure.feature('B客户获取地址簿信息')
class Test_app_ka_get_addrbooks(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/addrbooks_v2?currentPage=1&typeCode=1'])
    @pytest.mark.run(order=24)
    def test_test_app_ka_get_addrbooks(self,headers,address):
        baseTest = BaseTestCase()
    
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/ka/v1/addrbooks_v2?currentPage=1&typeCode=1']
            
        host = 'app_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        resp = requests.get(url=url, headers=headers_new,verify=False, timeout=120)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][0]["detail_address"]', resp.json()["data"]["user_addrbooks"][0]["detail_address"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][0]["postal_code"]', resp.json()["data"]["user_addrbooks"][0]["postal_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][0]["district_code"]', resp.json()["data"]["user_addrbooks"][0]["district_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][0]["city_code"]', resp.json()["data"]["user_addrbooks"][0]["city_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][0]["province_code"]', resp.json()["data"]["user_addrbooks"][0]["province_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][0]["phone"]', resp.json()["data"]["user_addrbooks"][0]["phone"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][0]["name"]', resp.json()["data"]["user_addrbooks"][0]["name"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][1]["detail_address"]', resp.json()["data"]["user_addrbooks"][1]["detail_address"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][1]["postal_code"]', resp.json()["data"]["user_addrbooks"][1]["postal_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][1]["district_code"]', resp.json()["data"]["user_addrbooks"][1]["district_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][1]["city_code"]', resp.json()["data"]["user_addrbooks"][1]["city_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][1]["province_code"]', resp.json()["data"]["user_addrbooks"][1]["province_code"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][1]["phone"]', resp.json()["data"]["user_addrbooks"][1]["phone"], ex=6000)
        
        RedisBase().set('app_ka_get_addrbooks_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["user_addrbooks"][1]["name"]', resp.json()["data"]["user_addrbooks"][1]["name"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        