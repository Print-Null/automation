
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


@allure.feature('C客户新建寄/收件人地址信息')
class Test_app_user_add_address(object):

    @pytest.mark.parametrize("parameter",['{\'district_code\': \'TH010201\', \'dst_home_phone\': \'\', \'detail_address\': \'$[python]"自动化测试地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'address_type\': 1, \'name\': \'$[python]"自动化"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'postal_code\': \'10600\', \'dst_default\': False, \'province_code\': \'TH01\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'src_default\': False, \'city_code\': \'TH0102\'}', '{\'district_code\': \'TH013201\', \'dst_home_phone\': \'\', \'detail_address\': \'$[python]"自动化测试寄件人地址新增"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'address_type\': 1, \'name\': \'$[python]"自动化"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'postal_code\': \'10200\', \'dst_default\': False, \'province_code\': \'TH01\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'src_default\': True, \'city_code\': \'TH0132\'}', '{\'name\': \'$[python]"自动化"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'src_default\': False, \'dst_default\': False, \'detail_address\': \'$[python]"自动化测试地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'province_code\': \'TH10\', \'dst_home_phone\': \'\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'city_code\': \'TH1001\', \'postal_code\': \'18000\', \'district_code\': \'TH100101\', \'address_type\': 2}', '{\'postal_code\': \'10500\', \'dst_home_phone\': \'\', \'dst_default\': True, \'country_code\': \'TH\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'city_code\': \'TH0125\', \'district_code\': \'TH012501\', \'name\': \'$[python]"收件人"+chr(random.randint(65,91))+chr(random.randint(97,123))+str(random.randint(1,100))$\', \'detail_address\': \'$[python]"自动化测试收件人地址新增"+chr(random.randint(65,91))+chr(random.randint(97,123))+str(random.randint(1,100))$\', \'src_default\': False, \'address_type\': 2, \'province_code\': \'TH01\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/user/v1/addrbooks'])
    @pytest.mark.run(order=8)
    def test_test_app_user_add_address(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'district_code\': \'TH010201\', \'dst_home_phone\': \'\', \'detail_address\': \'$[python]"自动化测试地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'address_type\': 1, \'name\': \'$[python]"自动化"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'postal_code\': \'10600\', \'dst_default\': False, \'province_code\': \'TH01\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'src_default\': False, \'city_code\': \'TH0102\'}', '{\'district_code\': \'TH013201\', \'dst_home_phone\': \'\', \'detail_address\': \'$[python]"自动化测试寄件人地址新增"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'address_type\': 1, \'name\': \'$[python]"自动化"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'postal_code\': \'10200\', \'dst_default\': False, \'province_code\': \'TH01\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'src_default\': True, \'city_code\': \'TH0132\'}', '{\'name\': \'$[python]"自动化"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'src_default\': False, \'dst_default\': False, \'detail_address\': \'$[python]"自动化测试地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'province_code\': \'TH10\', \'dst_home_phone\': \'\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'city_code\': \'TH1001\', \'postal_code\': \'18000\', \'district_code\': \'TH100101\', \'address_type\': 2}', '{\'postal_code\': \'10500\', \'dst_home_phone\': \'\', \'dst_default\': True, \'country_code\': \'TH\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'city_code\': \'TH0125\', \'district_code\': \'TH012501\', \'name\': \'$[python]"收件人"+chr(random.randint(65,91))+chr(random.randint(97,123))+str(random.randint(1,100))$\', \'detail_address\': \'$[python]"自动化测试收件人地址新增"+chr(random.randint(65,91))+chr(random.randint(97,123))+str(random.randint(1,100))$\', \'src_default\': False, \'address_type\': 2, \'province_code\': \'TH01\'}']
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
        
        _address = ['/api/user/v1/addrbooks']
            
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
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        