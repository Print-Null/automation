
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


@allure.feature('B客户的快递员确认包裹信息后揽收快件')
class Test_kit_ka_courier_ticket_pickups_confirm(object):

    @pytest.mark.parametrize("parameter",['{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_ka_courier_ticket_pickups_0_0_["data"]["not_collected_parcels"][#headers#]["user_order_id"]$\', \'src_province_code\': \'TH04\', \'src_district_code\': \'TH040106\', \'src_city_code\': \'TH0401\', \'src_country_code\': \'TH\', \'src_postal_code\': \'12000\', \'dst_detail_address\': \'$[python]"揽件时收件人地址修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'TH2001\', \'dst_province_code\': \'TH20\', \'dst_postal_code\': \'20000\', \'dst_district_code\': \'TH200101\', \'dst_home_phone\': \'\', \'dst_name\': \'$[python]"收件人名字修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_phone\': \'$[python]random.choice(["0136","0137"])+str(random.randint(1000000,99999999))$\', \'src_phone\': \'$[python]random.choice(["0140","0141"])+str(random.randint(1000000,99999999))$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[python]"寄件人名字修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[python]"揽件时寄件人地址修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': True, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_ka_courier_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-US\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_ka_courier_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_ka_courier_new_device_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/courier/v1/ticket/pickups/$app_ka_ticket_pickup_list_0_0_["data"]["list"][0]["id"]$/confirm'])
    @pytest.mark.run(order=16)
    def test_test_kit_ka_courier_ticket_pickups_confirm(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'width\': \'$[python]random.randint(1,40)$\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'user_order_id\': \'$kit_ka_courier_ticket_pickups_0_0_["data"]["not_collected_parcels"][#headers#]["user_order_id"]$\', \'src_province_code\': \'TH04\', \'src_district_code\': \'TH040106\', \'src_city_code\': \'TH0401\', \'src_country_code\': \'TH\', \'src_postal_code\': \'12000\', \'dst_detail_address\': \'$[python]"揽件时收件人地址修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_country_code\': \'TH\', \'dst_city_code\': \'TH2001\', \'dst_province_code\': \'TH20\', \'dst_postal_code\': \'20000\', \'dst_district_code\': \'TH200101\', \'dst_home_phone\': \'\', \'dst_name\': \'$[python]"收件人名字修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'dst_phone\': \'$[python]random.choice(["0136","0137"])+str(random.randint(1000000,99999999))$\', \'src_phone\': \'$[python]random.choice(["0140","0141"])+str(random.randint(1000000,99999999))$\', \'height\': \'$[python]random.randint(1,40)$\', \'insure_declare_value\': 0, \'src_name\': \'$[python]"寄件人名字修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'length\': \'$[python]random.randint(1,40)$\', \'src_detail_address\': \'$[python]"揽件时寄件人地址修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'call_duration\': 0, \'insured\': False, \'freight_insure_enabled\': True, \'express_category\': 1, \'cod_enabled\': False, \'total_amount\': 4500, \'cod_amount\': 0, \'settlement_category\': 1, \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\'}']
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_ka_courier_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-US\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_ka_courier_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_ka_courier_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                
        _address = ['/api/courier/v1/ticket/pickups/$app_ka_ticket_pickup_list_0_0_["data"]["list"][0]["id"]$/confirm']
            
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
        
        RedisBase().set('kit_ka_courier_ticket_pickups_confirm_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["parcel_info"]["pno"]', resp.json()["data"]["parcel_info"]["pno"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/16_kit_ka_courier_ticket_pickups_confirm.json")
        with open("../data/jsonschema/16_kit_ka_courier_ticket_pickups_confirm.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        