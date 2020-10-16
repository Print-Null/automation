
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


@allure.feature('大客户修改未发货订单')
class Test_ka_api_orders_edit(object):

    @pytest.mark.parametrize("parameter",['{\'id\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["id"]$\', \'pno\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["pno"]$\', \'src_name\': \'$[python]"sender modify"+str(random.randint(1,99999999))$\', \'src_phone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'src_country_code\': \'TH\', \'src_country_name\': \'Thailand\', \'src_province_code\': \'TH01\', \'src_province_name\': \'กรุงเทพ\', \'src_city_code\': \'TH0101\', \'src_city_name\': \'คลองเตย\', \'src_district_code\': \'TH010103\', \'src_district_name\': \'พระโขนง\', \'src_detail_address\': \'$[python]"sender detail address modify"+str(random.randint(1,99999999))$\', \'src_postal_code\': \'10260\', \'dst_name\': \'$[python]"receiver modify"+str(random.randint(1,99999999))$\', \'dst_phone\': \'$[python]"0158"+str(random.randint(100000,999999))$\', \'dst_home_phone\': \'\', \'dst_country_code\': \'TH\', \'dst_country_name\': \'Thailand\', \'dst_province_code\': \'TH01\', \'dst_province_name\': \'กรุงเทพ\', \'dst_city_code\': \'TH0121\', \'dst_city_name\': \'บางซื่อ\', \'dst_district_code\': \'TH012101\', \'dst_district_name\': \'บางซื่อ\', \'dst_postal_code\': \'10800\', \'dst_detail_address\': \'$[python]"receiver detail address modify"+str(random.randint(1,99999999))$\', \'cod_amount\': \'$[python]random.randrange(100,5000001,100)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'length\': \'$[python]str(random.randint(1,40))$\', \'width\': \'$[python]str(random.randint(1,40))$\', \'height\': \'$[python]str(random.randint(1,40))$\', \'price_policy\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,11,99])$\', \'article_category_text\': \'水果\', \'out_trade_no\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["out_trade_no"]$\', \'insured\': True, \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'remark_first\': \'已打印订单修改\', \'remark_second\': None, \'remark_third\': \'\', \'return_receipt_enabled\': False, \'return_receipt_no\': \'\', \'freight_insure_enabled\': False, \'estimate_freight_insure_amount\': 0, \'express_category\': 1, \'theoretical_finish_at_text\': None, \'speed_cut_time_text\': None, \'upcountry_amount\': 0, \'skipping_tips\': []}', '{\'id\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][1]["id"]$\', \'pno\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][1]["pno"]$\', \'src_name\': \'$[python]"sender modify"+str(random.randint(1,99999999))$\', \'src_phone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'src_country_code\': \'TH\', \'src_country_name\': \'Thailand\', \'src_province_code\': \'TH01\', \'src_province_name\': \'กรุงเทพ\', \'src_city_code\': \'TH0101\', \'src_city_name\': \'คลองเตย\', \'src_district_code\': \'TH010103\', \'src_district_name\': \'พระโขนง\', \'src_detail_address\': \'$[python]"sender detail address modify"+str(random.randint(1,99999999))$\', \'src_postal_code\': \'10260\', \'dst_name\': \'$[python]"receiver modify"+str(random.randint(1,99999999))$\', \'dst_phone\': \'$[python]"0158"+str(random.randint(100000,999999))$\', \'dst_home_phone\': \'\', \'dst_country_code\': \'TH\', \'dst_country_name\': \'Thailand\', \'dst_province_code\': \'TH01\', \'dst_province_name\': \'กรุงเทพ\', \'dst_city_code\': \'TH0121\', \'dst_city_name\': \'บางซื่อ\', \'dst_district_code\': \'TH012101\', \'dst_district_name\': \'บางซื่อ\', \'dst_postal_code\': \'10800\', \'dst_detail_address\': \'$[python]"receiver detail address modify"+str(random.randint(1,99999999))$\', \'cod_amount\': \'$[python]random.randrange(100,5000001,100)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'length\': \'$[python]str(random.randint(1,40))$\', \'width\': \'$[python]str(random.randint(1,40))$\', \'height\': \'$[python]str(random.randint(1,40))$\', \'price_policy\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,11,99])$\', \'article_category_text\': \'其他\', \'out_trade_no\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][1]["out_trade_no"]$\', \'insured\': True, \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'remark_first\': \'待打印订单修改\', \'remark_second\': None, \'remark_third\': \'\', \'return_receipt_enabled\': False, \'return_receipt_no\': \'\', \'freight_insure_enabled\': True, \'estimate_freight_insure_amount\': 0, \'express_category\': 2, \'theoretical_finish_at_text\': None, \'speed_cut_time_text\': None, \'upcountry_amount\': 0, \'skipping_tips\': []}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept-Language\': \'th\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['/ka/api/orders/edit'])
    @pytest.mark.run(order=355)
    def test_test_ka_api_orders_edit(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'id\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["id"]$\', \'pno\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["pno"]$\', \'src_name\': \'$[python]"sender modify"+str(random.randint(1,99999999))$\', \'src_phone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'src_country_code\': \'TH\', \'src_country_name\': \'Thailand\', \'src_province_code\': \'TH01\', \'src_province_name\': \'กรุงเทพ\', \'src_city_code\': \'TH0101\', \'src_city_name\': \'คลองเตย\', \'src_district_code\': \'TH010103\', \'src_district_name\': \'พระโขนง\', \'src_detail_address\': \'$[python]"sender detail address modify"+str(random.randint(1,99999999))$\', \'src_postal_code\': \'10260\', \'dst_name\': \'$[python]"receiver modify"+str(random.randint(1,99999999))$\', \'dst_phone\': \'$[python]"0158"+str(random.randint(100000,999999))$\', \'dst_home_phone\': \'\', \'dst_country_code\': \'TH\', \'dst_country_name\': \'Thailand\', \'dst_province_code\': \'TH01\', \'dst_province_name\': \'กรุงเทพ\', \'dst_city_code\': \'TH0121\', \'dst_city_name\': \'บางซื่อ\', \'dst_district_code\': \'TH012101\', \'dst_district_name\': \'บางซื่อ\', \'dst_postal_code\': \'10800\', \'dst_detail_address\': \'$[python]"receiver detail address modify"+str(random.randint(1,99999999))$\', \'cod_amount\': \'$[python]random.randrange(100,5000001,100)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'length\': \'$[python]str(random.randint(1,40))$\', \'width\': \'$[python]str(random.randint(1,40))$\', \'height\': \'$[python]str(random.randint(1,40))$\', \'price_policy\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,11,99])$\', \'article_category_text\': \'水果\', \'out_trade_no\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][0]["out_trade_no"]$\', \'insured\': True, \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'remark_first\': \'已打印订单修改\', \'remark_second\': None, \'remark_third\': \'\', \'return_receipt_enabled\': False, \'return_receipt_no\': \'\', \'freight_insure_enabled\': False, \'estimate_freight_insure_amount\': 0, \'express_category\': 1, \'theoretical_finish_at_text\': None, \'speed_cut_time_text\': None, \'upcountry_amount\': 0, \'skipping_tips\': []}', '{\'id\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][1]["id"]$\', \'pno\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][1]["pno"]$\', \'src_name\': \'$[python]"sender modify"+str(random.randint(1,99999999))$\', \'src_phone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'src_country_code\': \'TH\', \'src_country_name\': \'Thailand\', \'src_province_code\': \'TH01\', \'src_province_name\': \'กรุงเทพ\', \'src_city_code\': \'TH0101\', \'src_city_name\': \'คลองเตย\', \'src_district_code\': \'TH010103\', \'src_district_name\': \'พระโขนง\', \'src_detail_address\': \'$[python]"sender detail address modify"+str(random.randint(1,99999999))$\', \'src_postal_code\': \'10260\', \'dst_name\': \'$[python]"receiver modify"+str(random.randint(1,99999999))$\', \'dst_phone\': \'$[python]"0158"+str(random.randint(100000,999999))$\', \'dst_home_phone\': \'\', \'dst_country_code\': \'TH\', \'dst_country_name\': \'Thailand\', \'dst_province_code\': \'TH01\', \'dst_province_name\': \'กรุงเทพ\', \'dst_city_code\': \'TH0121\', \'dst_city_name\': \'บางซื่อ\', \'dst_district_code\': \'TH012101\', \'dst_district_name\': \'บางซื่อ\', \'dst_postal_code\': \'10800\', \'dst_detail_address\': \'$[python]"receiver detail address modify"+str(random.randint(1,99999999))$\', \'cod_amount\': \'$[python]random.randrange(100,5000001,100)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'length\': \'$[python]str(random.randint(1,40))$\', \'width\': \'$[python]str(random.randint(1,40))$\', \'height\': \'$[python]str(random.randint(1,40))$\', \'price_policy\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,11,99])$\', \'article_category_text\': \'其他\', \'out_trade_no\': \'$ka_api_orders_search_with_time_0_0_["data"]["items"][1]["out_trade_no"]$\', \'insured\': True, \'insure_declare_value\': \'$[python]random.randrange(100,5000001,100)$\', \'remark_first\': \'待打印订单修改\', \'remark_second\': None, \'remark_third\': \'\', \'return_receipt_enabled\': False, \'return_receipt_no\': \'\', \'freight_insure_enabled\': True, \'estimate_freight_insure_amount\': 0, \'express_category\': 2, \'theoretical_finish_at_text\': None, \'speed_cut_time_text\': None, \'upcountry_amount\': 0, \'skipping_tips\': []}']
        
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
                
        _address = ['/ka/api/orders/edit']
            
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
        