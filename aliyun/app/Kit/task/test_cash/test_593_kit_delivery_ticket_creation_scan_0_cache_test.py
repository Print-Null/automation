
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


@allure.feature('交接-订单0')
class Test_kit_delivery_ticket_creation_scan_0(object):

    @pytest.mark.parametrize("parameter",['{\'continue_de_enabled\': False, \'openned\': True, \'from_scanner\': False, \'image_keys\': [\'$kit_parcels_manual_import_0_0_["data"]["object_key"]$\'], \'parcel_scan_manual_import_category\': 99, \'routed_at\': 1593348506, \'routed_at_device\': 1593348506, \'routed_at_ntp\': 1593348503, \'skipped_enabled\': False}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/parcels/$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$/delivery_ticket_creation_scan?isFromScanner=false'])
    @pytest.mark.run(order=593)
    def test_test_kit_delivery_ticket_creation_scan_0(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'continue_de_enabled\': False, \'openned\': True, \'from_scanner\': False, \'image_keys\': [\'$kit_parcels_manual_import_0_0_["data"]["object_key"]$\'], \'parcel_scan_manual_import_category\': 99, \'routed_at\': 1593348506, \'routed_at_device\': 1593348506, \'routed_at_ntp\': 1593348503, \'skipped_enabled\': False}']
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/courier/v1/parcels/$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$/delivery_ticket_creation_scan?isFromScanner=false']
            
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
        