
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


@allure.feature('揽件收款来源-揽收完成-3')
class Test_kit_message_pickupReward(object):

    @pytest.mark.parametrize("parameter",['{\'addr_core_ids\': [], \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'call_duration\': 0, \'client_id\': \'$kit_v1_address_0_0_["data"][0]["id"]$\', \'cod_amount\': \'$[python]random.randrange(0,500000,100)$\', \'cod_enabled\': True, \'customer_type_category\': 2, \'dst_city_code\': \'TH0101\', \'dst_country_code\': \'TH\', \'dst_detail_address\': \'$[config]recipient_address$\', \'dst_district_code\': \'TH010101\', \'dst_name\': \'$[config]recipient_name$\', \'dst_phone\': \'$[config]recipient_phone$\', \'dst_postal_code\': \'10110\', \'dst_province_code\': \'TH01\', \'express_category\': 1, \'freight_insure_enabled\': False, \'height\': \'$[python]random.randint(1,30)$\', \'insure_declare_value\': 0, \'insured\': False, \'length\': \'$[python]random.randint(1,30)$\', \'request_ids\': [], \'settlement_category\': 1, \'skipping_tips\': [], \'src_city_code\': \'TH0101\', \'src_country_code\': \'TH\', \'src_detail_address\': \'dfsdfe\', \'src_district_code\': \'TH010101\', \'src_name\': \'$[config]send_name$\', \'src_phone\': \'$[config]send_phone$\', \'src_postal_code\': \'10110\', \'src_province_code\': \'TH01\', \'total_amount\': \'$[config]total_amount$\', \'weight\': \'$[python]random.randint(100,5000)$\', \'width\': \'$[python]random.randint(1,50)$\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_2_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/message/pickupReward/$kit_pickups_parcel_0_0_0_["data"]["ticket_pickup_id"]$'])
    @pytest.mark.run(order=29)
    def test_test_kit_message_pickupReward(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'addr_core_ids\': [], \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'call_duration\': 0, \'client_id\': \'$kit_v1_address_0_0_["data"][0]["id"]$\', \'cod_amount\': \'$[python]random.randrange(0,500000,100)$\', \'cod_enabled\': True, \'customer_type_category\': 2, \'dst_city_code\': \'TH0101\', \'dst_country_code\': \'TH\', \'dst_detail_address\': \'$[config]recipient_address$\', \'dst_district_code\': \'TH010101\', \'dst_name\': \'$[config]recipient_name$\', \'dst_phone\': \'$[config]recipient_phone$\', \'dst_postal_code\': \'10110\', \'dst_province_code\': \'TH01\', \'express_category\': 1, \'freight_insure_enabled\': False, \'height\': \'$[python]random.randint(1,30)$\', \'insure_declare_value\': 0, \'insured\': False, \'length\': \'$[python]random.randint(1,30)$\', \'request_ids\': [], \'settlement_category\': 1, \'skipping_tips\': [], \'src_city_code\': \'TH0101\', \'src_country_code\': \'TH\', \'src_detail_address\': \'dfsdfe\', \'src_district_code\': \'TH010101\', \'src_name\': \'$[config]send_name$\', \'src_phone\': \'$[config]send_phone$\', \'src_postal_code\': \'10110\', \'src_province_code\': \'TH01\', \'total_amount\': \'$[config]total_amount$\', \'weight\': \'$[python]random.randint(100,5000)$\', \'width\': \'$[python]random.randint(1,50)$\'}']
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_2_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/courier/v1/message/pickupReward/$kit_pickups_parcel_0_0_0_["data"]["ticket_pickup_id"]$']
            
        host = 'kit_host'
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
            assert_that(resp.json()["msg"]).is_equal_to("成功")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("สำเร็จ")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("success")
        