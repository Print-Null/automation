
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


@allure.feature('C客户包裹价格估算')
class Test_app_user_rate_order(object):

    @pytest.mark.parametrize("parameter",['{\'src_postal_code\': \'10200\', \'dst_district_code\': \'TH012501\', \'freight_insure_enabled\': \'$[python]random.choice(["false","true"])$\', \'dst_postal_code\': \'10500\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_city_code\': \'TH0125\', \'insured\': 0, \'src_district_code\': \'TH013201\', \'length\': \'$[python]random.randint(0,40)$\', \'width\': \'$[python]random.randint(0,40)$\', \'src_detail_address\': \'$[python]"寄件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_detail_address\': \'$[python]"收件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_province_code\': \'TH01\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'src_province_code\': \'TH01\', \'src_city_code\': \'TH0132\', \'dst_country_code\': \'TH\', \'height\': \'$[python]random.randint(0,40)$\', \'src_country_code\': \'TH\', \'express_category\': \'$[python]random.randint(1,2)$\'}', '{\'src_postal_code\': \'10200\', \'dst_district_code\': \'TH012501\', \'freight_insure_enabled\': \'$[python]random.choice(["false","true"])$\', \'dst_postal_code\': \'10500\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_city_code\': \'TH0125\', \'insured\': 1, \'src_district_code\': \'TH013201\', \'length\': \'$[python]random.randint(0,40)$\', \'width\': \'$[python]random.randint(0,40)$\', \'src_detail_address\': \'$[python]"自动化寄件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_detail_address\': \'$[python]"自动化收件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_province_code\': \'TH01\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'src_province_code\': \'TH01\', \'src_city_code\': \'TH0132\', \'dst_country_code\': \'TH\', \'height\': \'$[python]random.randint(0,40)$\', \'src_country_code\': \'TH\', \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'express_category\': \'$[python]random.randint(1,2)$\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/user/v1/rate/order'])
    @pytest.mark.run(order=13)
    def test_test_app_user_rate_order(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'src_postal_code\': \'10200\', \'dst_district_code\': \'TH012501\', \'freight_insure_enabled\': \'$[python]random.choice(["false","true"])$\', \'dst_postal_code\': \'10500\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_city_code\': \'TH0125\', \'insured\': 0, \'src_district_code\': \'TH013201\', \'length\': \'$[python]random.randint(0,40)$\', \'width\': \'$[python]random.randint(0,40)$\', \'src_detail_address\': \'$[python]"寄件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_detail_address\': \'$[python]"收件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_province_code\': \'TH01\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'src_province_code\': \'TH01\', \'src_city_code\': \'TH0132\', \'dst_country_code\': \'TH\', \'height\': \'$[python]random.randint(0,40)$\', \'src_country_code\': \'TH\', \'express_category\': \'$[python]random.randint(1,2)$\'}', '{\'src_postal_code\': \'10200\', \'dst_district_code\': \'TH012501\', \'freight_insure_enabled\': \'$[python]random.choice(["false","true"])$\', \'dst_postal_code\': \'10500\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_city_code\': \'TH0125\', \'insured\': 1, \'src_district_code\': \'TH013201\', \'length\': \'$[python]random.randint(0,40)$\', \'width\': \'$[python]random.randint(0,40)$\', \'src_detail_address\': \'$[python]"自动化寄件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_detail_address\': \'$[python]"自动化收件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_province_code\': \'TH01\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'src_province_code\': \'TH01\', \'src_city_code\': \'TH0132\', \'dst_country_code\': \'TH\', \'height\': \'$[python]random.randint(0,40)$\', \'src_country_code\': \'TH\', \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'express_category\': \'$[python]random.randint(1,2)$\'}']
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
        
        _address = ['/api/user/v1/rate/order']
            
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
        