
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


@allure.feature('C客户保存收件人和包裹信息')
class Test_app_user_address_recommend(object):

    @pytest.mark.parametrize("parameter",['{\'from_channel\': \'10\', \'detail_address\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["detail_address"]$\', \'district_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["district_code"]$\', \'province_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["province_code"]$\', \'city_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["city_code"]$\', \'postal_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["postal_code"]$\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/user/v1/address/recommend/addressRecommend'])
    @pytest.mark.run(order=14)
    def test_test_app_user_address_recommend(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'from_channel\': \'10\', \'detail_address\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["detail_address"]$\', \'district_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["district_code"]$\', \'province_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["province_code"]$\', \'city_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["city_code"]$\', \'postal_code\': \'$app_user_get_addrbooks_0_1_["data"]["user_addrbooks"][0]["postal_code"]$\'}']
        parameter_new = baseTest.parameter_parser(parameter)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/user/v1/address/recommend/addressRecommend']
            
        host = 'app_host'
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
        
        RedisBase().set('app_user_address_recommend_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["request_id"]', resp.json()["data"]["request_id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        