
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


@allure.feature('B客户新建仓库地址信息')
class Test_app_ka_add_warehouse(object):

    @pytest.mark.parametrize("parameter",['{\'phone\': \'$[python]random.choice(["130","131"])+str(random.randint(1000000,99999999))$\', \'city_code\': \'TH0101\', \'src_name\': \'$[python]"自动化仓库姓名"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'province_code\': \'TH01\', \'country_code\': \'TH\', \'district_code\': \'TH010101\', \'detail_address\': \'$[python]"自动化仓库地址新增"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'warehouse_no\': \' \', \'name\': \'$[python]"自动化仓库名称"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'postal_code\': \'10110\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/warehouse'])
    @pytest.mark.run(order=19)
    def test_test_app_ka_add_warehouse(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'phone\': \'$[python]random.choice(["130","131"])+str(random.randint(1000000,99999999))$\', \'city_code\': \'TH0101\', \'src_name\': \'$[python]"自动化仓库姓名"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'province_code\': \'TH01\', \'country_code\': \'TH\', \'district_code\': \'TH010101\', \'detail_address\': \'$[python]"自动化仓库地址新增"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'warehouse_no\': \' \', \'name\': \'$[python]"自动化仓库名称"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'postal_code\': \'10110\'}']
        parameter_new = baseTest.parameter_parser(parameter)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/ka/v1/warehouse']
            
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
        