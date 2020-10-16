
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


@allure.feature('B客户修改某个订单下的包裹信息')
class Test_app_ka_orders_update(object):

    @pytest.mark.parametrize("parameter",['{\'request_id\': \'$app_ka_address_recommend_0_0_0_["data"]["request_id"]$\', \'dst_detail_address\': \'$[python]"自动化B客户修改收件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_district_code\': \'TH070101\', \'upcountry_amount\': 0, \'insure_amount\': 500, \'skipping_tips\': [], \'cod_enabled\': 0, \'src_name\': \'$app_ka_orders_order_detail_0_0_["data"]["src_name"]$\', \'src_phone\': \'$app_ka_orders_order_detail_0_0_["data"]["src_phone"]$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_country_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_country_code"]$\', \'dst_name\': \'$[python]"自动化B客户修改收件人名字"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'estimate_parcel_amount\': 4000, \'express_category\': 2, \'estimate_total_amount\': 5000, \'freight_insure_enabled\': True, \'src_city_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_city_code"]$\', \'src_province_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_province_code"]$\', \'src_postal_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_postal_code"]$\', \'price_policy\': 1, \'insured\': 1, \'src_district_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_district_code"]$\', \'height\': \'$[python]random.randint(1,40)$\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'id\': \'$app_ka_ticket_orders_list_0_0_["data"][0]["id"]$\', \'dst_postal_code\': \'15000\', \'dst_country_code\': \'TH\', \'upcountry\': 0, \'insure_declare_value\': 100000, \'dst_phone\': \'$[python]random.choice(["180","181"])+str(random.randint(1000000,99999999))$\', \'dst_city_code\': \'TH0701\', \'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'src_detail_address\': \'$app_ka_orders_order_detail_0_0_["data"]["src_detail_address"]$\', \'dst_province_code\': \'TH07\', \'cod_amount\': 0, \'addr_core_id\': \'\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/orders/update/$app_ka_ticket_orders_list_0_0_["data"][0]["id"]$'])
    @pytest.mark.run(order=45)
    def test_test_app_ka_orders_update(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'request_id\': \'$app_ka_address_recommend_0_0_0_["data"]["request_id"]$\', \'dst_detail_address\': \'$[python]"自动化B客户修改收件地址"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_district_code\': \'TH070101\', \'upcountry_amount\': 0, \'insure_amount\': 500, \'skipping_tips\': [], \'cod_enabled\': 0, \'src_name\': \'$app_ka_orders_order_detail_0_0_["data"]["src_name"]$\', \'src_phone\': \'$app_ka_orders_order_detail_0_0_["data"]["src_phone"]$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_country_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_country_code"]$\', \'dst_name\': \'$[python]"自动化B客户修改收件人名字"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'estimate_parcel_amount\': 4000, \'express_category\': 2, \'estimate_total_amount\': 5000, \'freight_insure_enabled\': True, \'src_city_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_city_code"]$\', \'src_province_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_province_code"]$\', \'src_postal_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_postal_code"]$\', \'price_policy\': 1, \'insured\': 1, \'src_district_code\': \'$app_ka_orders_order_detail_0_0_["data"]["src_district_code"]$\', \'height\': \'$[python]random.randint(1,40)$\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'id\': \'$app_ka_ticket_orders_list_0_0_["data"][0]["id"]$\', \'dst_postal_code\': \'15000\', \'dst_country_code\': \'TH\', \'upcountry\': 0, \'insure_declare_value\': 100000, \'dst_phone\': \'$[python]random.choice(["180","181"])+str(random.randint(1000000,99999999))$\', \'dst_city_code\': \'TH0701\', \'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'src_detail_address\': \'$app_ka_orders_order_detail_0_0_["data"]["src_detail_address"]$\', \'dst_province_code\': \'TH07\', \'cod_amount\': 0, \'addr_core_id\': \'\'}']
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
        
        _address = ['/api/ka/v1/orders/update/$app_ka_ticket_orders_list_0_0_["data"][0]["id"]$']
            
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
        