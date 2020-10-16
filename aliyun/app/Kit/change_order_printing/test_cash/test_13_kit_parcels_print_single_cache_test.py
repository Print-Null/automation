
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


@allure.feature('快递员-换单打印-修改订单信息-提交')
class Test_kit_parcels_print_single(object):

    @pytest.mark.parametrize("parameter",['{\'dst_city_code\': \'TH0101\', \'dst_country_code\': \'TH\', \'dst_detail_address\': \'$[config]modified_recipient_address$\', \'dst_district_code\': \'TH010101\', \'dst_name\': \'$[config]modified_recipient_name$\', \'dst_phone\': \'$[config]modified_recipient_phone$\', \'dst_postal_code\': \'10110\', \'dst_province_code\': \'TH01\', \'pkg_code\': \'\', \'pno\': \'$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$\', \'src_city_code\': \'TH0101\', \'src_country_code\': \'TH\', \'src_detail_address\': \'$[config]modified_send_address$\', \'src_district_code\': \'TH010101\', \'src_name\': \'$[config]modified_send_name$\', \'src_phone\': \'$[config]modified_send_phone$\', \'src_postal_code\': \'10110\', \'src_province_code\': \'TH01\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_2_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/parcels/print_single'])
    @pytest.mark.run(order=13)
    def test_test_kit_parcels_print_single(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'dst_city_code\': \'TH0101\', \'dst_country_code\': \'TH\', \'dst_detail_address\': \'$[config]modified_recipient_address$\', \'dst_district_code\': \'TH010101\', \'dst_name\': \'$[config]modified_recipient_name$\', \'dst_phone\': \'$[config]modified_recipient_phone$\', \'dst_postal_code\': \'10110\', \'dst_province_code\': \'TH01\', \'pkg_code\': \'\', \'pno\': \'$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$\', \'src_city_code\': \'TH0101\', \'src_country_code\': \'TH\', \'src_detail_address\': \'$[config]modified_send_address$\', \'src_district_code\': \'TH010101\', \'src_name\': \'$[config]modified_send_name$\', \'src_phone\': \'$[config]modified_send_phone$\', \'src_postal_code\': \'10110\', \'src_province_code\': \'TH01\'}']
        
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
                
        _address = ['api/courier/v1/parcels/print_single']
            
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
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        # logging.info("jsonschema文件path:../data/jsonschema/13_courier_change_order_commit.json")
        # with open("../data/jsonschema/13_courier_change_order_commit.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        