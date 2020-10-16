
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


@allure.feature('C客户的快递员确认包裹信息后揽收快件')
class Test_kit_user_sender_courier_ticket_pickups_confirm_cn(object):

    @pytest.mark.parametrize("parameter",['{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["not_collected_parcels"][0]["user_order_id"]$\', \'src_province_code\': \'$[config]src_province_code$\', \'src_district_code\': \'$[config]src_district_code$\', \'src_city_code\': \'$[config]src_city_code$\', \'src_country_code\': \'TH\', \'src_postal_code\': \'$[config]src_postal_code$\', \'dst_detail_address\': \'$[config]dst_detail_address$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'$[config]dst_city_code$\', \'dst_province_code\': \'$[config]dst_province_code$\', \'dst_postal_code\': \'$[config]dst_postal_code$\', \'dst_district_code\': \'$[config]dst_district_code$\', \'dst_home_phone\': \'\', \'dst_name\': \'$[config]dst_name$\', \'dst_phone\': \'$[config]dst_phone$\', \'src_phone\': \'$[config]src_phone$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[config]src_name$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[config]src_detail_address$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': False, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}', '{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["not_collected_parcels"][1]["user_order_id"]$\', \'src_province_code\': \'$[config]src_province_code$\', \'src_district_code\': \'$[config]src_district_code$\', \'src_city_code\': \'$[config]src_city_code$\', \'src_country_code\': \'TH\', \'src_postal_code\': \'$[config]src_postal_code$\', \'dst_detail_address\': \'$[config]dst_detail_address$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'$[config]dst_city_code$\', \'dst_province_code\': \'$[config]dst_province_code$\', \'dst_postal_code\': \'$[config]dst_postal_code$\', \'dst_district_code\': \'$[config]dst_district_code$\', \'dst_home_phone\': \'\', \'dst_name\': \'$[config]dst_name$\', \'dst_phone\': \'$[config]dst_phone$\', \'src_phone\': \'$[config]src_phone$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[config]src_name$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[config]src_detail_address$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': False, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}', '{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["not_collected_parcels"][2]["user_order_id"]$\', \'src_province_code\': \'$[config]src_province_code$\', \'src_district_code\': \'$[config]src_district_code$\', \'src_city_code\': \'$[config]src_city_code$\', \'src_country_code\': \'TH\', \'src_postal_code\': \'$[config]src_postal_code$\', \'dst_detail_address\': \'$[config]dst_detail_address$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'$[config]dst_city_code$\', \'dst_province_code\': \'$[config]dst_province_code$\', \'dst_postal_code\': \'$[config]dst_postal_code$\', \'dst_district_code\': \'$[config]dst_district_code$\', \'dst_home_phone\': \'\', \'dst_name\': \'$[config]dst_name$\', \'dst_phone\': \'$[config]dst_phone$\', \'src_phone\': \'$[config]src_phone$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[config]src_name$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[config]src_detail_address$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': False, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_user_sender_courier_new_device_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/courier/v1/ticket/pickups/$app_user_sender_ticket_pickup_list_cn_0_0_["data"]["list"][0]["id"]$/confirm'])
    @pytest.mark.run(order=9)
    def test_test_kit_user_sender_courier_ticket_pickups_confirm_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["not_collected_parcels"][0]["user_order_id"]$\', \'src_province_code\': \'$[config]src_province_code$\', \'src_district_code\': \'$[config]src_district_code$\', \'src_city_code\': \'$[config]src_city_code$\', \'src_country_code\': \'TH\', \'src_postal_code\': \'$[config]src_postal_code$\', \'dst_detail_address\': \'$[config]dst_detail_address$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'$[config]dst_city_code$\', \'dst_province_code\': \'$[config]dst_province_code$\', \'dst_postal_code\': \'$[config]dst_postal_code$\', \'dst_district_code\': \'$[config]dst_district_code$\', \'dst_home_phone\': \'\', \'dst_name\': \'$[config]dst_name$\', \'dst_phone\': \'$[config]dst_phone$\', \'src_phone\': \'$[config]src_phone$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[config]src_name$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[config]src_detail_address$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': False, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}', '{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["not_collected_parcels"][1]["user_order_id"]$\', \'src_province_code\': \'$[config]src_province_code$\', \'src_district_code\': \'$[config]src_district_code$\', \'src_city_code\': \'$[config]src_city_code$\', \'src_country_code\': \'TH\', \'src_postal_code\': \'$[config]src_postal_code$\', \'dst_detail_address\': \'$[config]dst_detail_address$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'$[config]dst_city_code$\', \'dst_province_code\': \'$[config]dst_province_code$\', \'dst_postal_code\': \'$[config]dst_postal_code$\', \'dst_district_code\': \'$[config]dst_district_code$\', \'dst_home_phone\': \'\', \'dst_name\': \'$[config]dst_name$\', \'dst_phone\': \'$[config]dst_phone$\', \'src_phone\': \'$[config]src_phone$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[config]src_name$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[config]src_detail_address$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': False, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}', '{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["not_collected_parcels"][2]["user_order_id"]$\', \'src_province_code\': \'$[config]src_province_code$\', \'src_district_code\': \'$[config]src_district_code$\', \'src_city_code\': \'$[config]src_city_code$\', \'src_country_code\': \'TH\', \'src_postal_code\': \'$[config]src_postal_code$\', \'dst_detail_address\': \'$[config]dst_detail_address$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'$[config]dst_city_code$\', \'dst_province_code\': \'$[config]dst_province_code$\', \'dst_postal_code\': \'$[config]dst_postal_code$\', \'dst_district_code\': \'$[config]dst_district_code$\', \'dst_home_phone\': \'\', \'dst_name\': \'$[config]dst_name$\', \'dst_phone\': \'$[config]dst_phone$\', \'src_phone\': \'$[config]src_phone$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[config]src_name$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[config]src_detail_address$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': False, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}']
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_user_sender_courier_new_device_login_cn_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['/api/courier/v1/ticket/pickups/$app_user_sender_ticket_pickup_list_cn_0_0_["data"]["list"][0]["id"]$/confirm']
            
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
        
        RedisBase().set('kit_user_sender_courier_ticket_pickups_confirm_cn_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["parcel_info"]["pno"]', resp.json()["data"]["parcel_info"]["pno"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/9_kit_user_sender_courier_ticket_pickups_confirm_cn.json")
        with open("../data/jsonschema/9_kit_user_sender_courier_ticket_pickups_confirm_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        