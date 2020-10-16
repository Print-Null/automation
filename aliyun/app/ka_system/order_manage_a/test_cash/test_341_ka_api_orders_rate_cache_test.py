
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


@allure.feature('大客户填写订单是计算保价费')
class Test_ka_api_orders_rate(object):

    @pytest.mark.parametrize("parameter",['{\'out_trade_no\': \'\', \'dst_name\': \'$[python]"rate receiver name"+str(random.randint(1,100000))$\', \'dst_phone\': \'$[python]"0190"+str(random.randint(100000,999999))$\', \'dst_district_code\': \'TH012101\', \'dst_detail_address\': \'$[python]"rate receiver detail address"+str(random.randint(10,999999))$\', \'dst_postal_code\': \'10800\', \'src_name\': \'$[python]"rate sender name"+str(random.randint(1,100000))$\', \'src_phone\': \'$[python]"0191"+str(random.randint(100000,999999))$\', \'src_province_code\': \'TH01\', \'src_city_code\': \'TH0101\', \'src_district_code\': \'TH010103\', \'src_detail_address\': \'$[python]"rate sender detail address"+str(random.randint(10,999999))$\', \'src_postal_code\': \'10260\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'cod_enabled\': True, \'cod_amount\': \'$[python]random.randrange(100,5000001,100)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'process_weight\': \'10\', \'insured\': True, \'ka_warehouse_id\': None, \'src_add\': False, \'src_default\': False, \'dst_add\': False, \'dst_home_phone\': \'\', \'disData\': \'พระโขนง-คลองเตย-กรุงเทพ-10260\', \'dstDisData\': \'บางซื่อ-บางซื่อ-กรุงเทพ-10800\', \'length\': \'$[python]str(random.randint(1,40))$\', \'width\': \'$[python]str(random.randint(1,40))$\', \'height\': \'$[python]str(random.randint(1,40))$\', \'remark_first\': \'\', \'remark_second\': \'\', \'remark_third\': \'\', \'return_receipt_no\': \'\', \'return_receipt_enabled\': False, \'freight_insure_enabled\': True, \'estimate_freight_insure_amount\': \'\', \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'insure_declare_value_input\': \'100\', \'express_category\': \'$[python]random.choice([1,2])$\', \'addr_core_id\': None, \'request_id\': None}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept-Language\': \'th\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['/ka/api/orders/rate'])
    @pytest.mark.run(order=341)
    def test_test_ka_api_orders_rate(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'out_trade_no\': \'\', \'dst_name\': \'$[python]"rate receiver name"+str(random.randint(1,100000))$\', \'dst_phone\': \'$[python]"0190"+str(random.randint(100000,999999))$\', \'dst_district_code\': \'TH012101\', \'dst_detail_address\': \'$[python]"rate receiver detail address"+str(random.randint(10,999999))$\', \'dst_postal_code\': \'10800\', \'src_name\': \'$[python]"rate sender name"+str(random.randint(1,100000))$\', \'src_phone\': \'$[python]"0191"+str(random.randint(100000,999999))$\', \'src_province_code\': \'TH01\', \'src_city_code\': \'TH0101\', \'src_district_code\': \'TH010103\', \'src_detail_address\': \'$[python]"rate sender detail address"+str(random.randint(10,999999))$\', \'src_postal_code\': \'10260\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'cod_enabled\': True, \'cod_amount\': \'$[python]random.randrange(100,5000001,100)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'process_weight\': \'10\', \'insured\': True, \'ka_warehouse_id\': None, \'src_add\': False, \'src_default\': False, \'dst_add\': False, \'dst_home_phone\': \'\', \'disData\': \'พระโขนง-คลองเตย-กรุงเทพ-10260\', \'dstDisData\': \'บางซื่อ-บางซื่อ-กรุงเทพ-10800\', \'length\': \'$[python]str(random.randint(1,40))$\', \'width\': \'$[python]str(random.randint(1,40))$\', \'height\': \'$[python]str(random.randint(1,40))$\', \'remark_first\': \'\', \'remark_second\': \'\', \'remark_third\': \'\', \'return_receipt_no\': \'\', \'return_receipt_enabled\': False, \'freight_insure_enabled\': True, \'estimate_freight_insure_amount\': \'\', \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'insure_declare_value_input\': \'100\', \'express_category\': \'$[python]random.choice([1,2])$\', \'addr_core_id\': None, \'request_id\': None}']
        
        _headers = ['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept-Language\': \'th\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        address_new = baseTest.parameter_parser(address, _headers, headers)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                
        _address = ['/ka/api/orders/rate']
            
        host = 'ka_system_host'
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
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        