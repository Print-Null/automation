
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


@allure.feature('C客户在寄件人地址簿中按关键字搜索寄/收件人信息')
class Test_app_user_search_addrbooks(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/user/v1/addrbooks_v2/list?currentPage=1&keyWord=$app_user_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["detail_address"]$&typeCode=1', '/api/user/v1/addrbooks_v2/list?currentPage=1&keyWord=$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["detail_address"]$&typeCode=2'])
    @pytest.mark.run(order=10)
    def test_test_app_user_search_addrbooks(self,headers,address):
        baseTest = BaseTestCase()
    
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/user/v1/addrbooks_v2/list?currentPage=1&keyWord=$app_user_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["detail_address"]$&typeCode=1', '/api/user/v1/addrbooks_v2/list?currentPage=1&keyWord=$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["detail_address"]$&typeCode=2']
            
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
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        