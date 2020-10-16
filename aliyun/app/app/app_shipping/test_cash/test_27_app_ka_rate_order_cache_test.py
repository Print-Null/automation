
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


@allure.feature('B客户包裹价格估算')
class Test_app_ka_rate_order(object):

    @pytest.mark.parametrize("parameter",['{\'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'cod_amount\': 0, \'src_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["phone"]$\', \'src_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["province_code"]$\', \'material_caregory\': 0, \'clientsd\': \'$[config]ka_clientsd$\', \'insured\': 0, \'cod_enabled\': 0, \'dst_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["detail_address"]$\', \'os\': \'ios\', \'dst_home_phone\': \'\', \'clientid\': \'$[config]app_clientid$\', \'dst_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["postal_code"]$\', \'version\': \'$[config]app_version$\', \'dst_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["phone"]$\', \'src_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["district_code"]$\', \'dst_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["province_code"]$\', \'freight_insure_enabled\': True, \'src_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["name"]$\', \'client_grade\': 0, \'length\': \'$[python]random.randint(0,40)$\', \'src_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["postal_code"]$\', \'dst_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["district_code"]$\', \'src_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["city_code"]$\', \'dst_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["city_code"]$\', \'src_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["detail_address"]$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_country_code\': \'TH\', \'width\': \'$[python]random.randint(0,40)$\', \'height\': \'$[python]random.randint(0,40)$\', \'dst_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["name"]$\', \'src_country_code\': \'TH\', \'express_category\': \'$[python]random.randint(1,2)$\'}', '{\'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'cod_amount\': 10000, \'src_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["phone"]$\', \'src_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["province_code"]$\', \'material_caregory\': 0, \'clientsd\': \'$[config]ka_clientsd$\', \'insured\': 1, \'cod_enabled\': 1, \'dst_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["detail_address"]$\', \'os\': \'ios\', \'dst_home_phone\': \'\', \'clientid\': \'$[config]app_clientid$\', \'dst_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["postal_code"]$\', \'version\': \'$[config]app_version$\', \'dst_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["phone"]$\', \'src_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["district_code"]$\', \'dst_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["province_code"]$\', \'freight_insure_enabled\': True, \'src_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["name"]$\', \'client_grade\': 0, \'length\': \'$[python]random.randint(0,40)$\', \'src_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["postal_code"]$\', \'insure_declare_value\': 500000, \'dst_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["district_code"]$\', \'src_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["city_code"]$\', \'dst_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["city_code"]$\', \'src_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["detail_address"]$\', \'insure_amount\': 800, \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_country_code\': \'TH\', \'width\': \'$[python]random.randint(0,40)$\', \'height\': \'$[python]random.randint(0,40)$\', \'dst_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["name"]$\', \'src_country_code\': \'TH\', \'express_category\': \'$[python]random.randint(1,2)$\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/rate/order'])
    @pytest.mark.run(order=27)
    def test_test_app_ka_rate_order(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'cod_amount\': 0, \'src_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["phone"]$\', \'src_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["province_code"]$\', \'material_caregory\': 0, \'clientsd\': \'$[config]ka_clientsd$\', \'insured\': 0, \'cod_enabled\': 0, \'dst_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["detail_address"]$\', \'os\': \'ios\', \'dst_home_phone\': \'\', \'clientid\': \'$[config]app_clientid$\', \'dst_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["postal_code"]$\', \'version\': \'$[config]app_version$\', \'dst_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["phone"]$\', \'src_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["district_code"]$\', \'dst_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["province_code"]$\', \'freight_insure_enabled\': True, \'src_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["name"]$\', \'client_grade\': 0, \'length\': \'$[python]random.randint(0,40)$\', \'src_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["postal_code"]$\', \'dst_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["district_code"]$\', \'src_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["city_code"]$\', \'dst_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["city_code"]$\', \'src_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["detail_address"]$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_country_code\': \'TH\', \'width\': \'$[python]random.randint(0,40)$\', \'height\': \'$[python]random.randint(0,40)$\', \'dst_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["name"]$\', \'src_country_code\': \'TH\', \'express_category\': \'$[python]random.randint(1,2)$\'}', '{\'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'cod_amount\': 10000, \'src_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["phone"]$\', \'src_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["province_code"]$\', \'material_caregory\': 0, \'clientsd\': \'$[config]ka_clientsd$\', \'insured\': 1, \'cod_enabled\': 1, \'dst_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["detail_address"]$\', \'os\': \'ios\', \'dst_home_phone\': \'\', \'clientid\': \'$[config]app_clientid$\', \'dst_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["postal_code"]$\', \'version\': \'$[config]app_version$\', \'dst_phone\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["phone"]$\', \'src_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["district_code"]$\', \'dst_province_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["province_code"]$\', \'freight_insure_enabled\': True, \'src_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["name"]$\', \'client_grade\': 0, \'length\': \'$[python]random.randint(0,40)$\', \'src_postal_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["postal_code"]$\', \'insure_declare_value\': 500000, \'dst_district_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["district_code"]$\', \'src_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["city_code"]$\', \'dst_city_code\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["city_code"]$\', \'src_detail_address\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["detail_address"]$\', \'insure_amount\': 800, \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_country_code\': \'TH\', \'width\': \'$[python]random.randint(0,40)$\', \'height\': \'$[python]random.randint(0,40)$\', \'dst_name\': \'$app_ka_get_addrbooks_0_0_["data"]["user_addrbooks"][1]["name"]$\', \'src_country_code\': \'TH\', \'express_category\': \'$[python]random.randint(1,2)$\'}']
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
        
        _address = ['/api/ka/v1/rate/order']
            
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
        