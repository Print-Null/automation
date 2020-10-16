
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


@allure.feature('仓管员-发件出仓-输入运单号')
class Test_kit_v1_parcels(object):

    @pytest.mark.parametrize("parameter",['{\'check_or_not\': True, \'exist_dst\': True, \'next_store_id\': \'$[config]store_id_2$\', \'proof_id\': \'$ms_van_proof_0_0_0_["data"]["id"]$\', \'routed_at\': 1594989796, \'routed_at_device\': 1594989796, \'routed_at_ntp\': 1594989795, \'shipment_switch\': True, \'skipped_enabled\': False, \'transportion_category\': 1, \'van_line_id\': \'$ms_van_line_0_0_["data"]["items"][0]["id"]$\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/parcels/$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$/shipment_warehouse_scan?isFromScanner=false'])
    @pytest.mark.run(order=68)
    def test_test_kit_v1_parcels(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'check_or_not\': True, \'exist_dst\': True, \'next_store_id\': \'$[config]store_id_2$\', \'proof_id\': \'$ms_van_proof_0_0_0_["data"]["id"]$\', \'routed_at\': 1594989796, \'routed_at_device\': 1594989796, \'routed_at_ntp\': 1594989795, \'shipment_switch\': True, \'skipped_enabled\': False, \'transportion_category\': 1, \'van_line_id\': \'$ms_van_line_0_0_["data"]["items"][0]["id"]$\'}']
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/courier/v1/parcels/$kit_pickups_parcel_0_0_0_["data"]["parcel_info"]["pno"]$/shipment_warehouse_scan?isFromScanner=false']
            
        host = 'ms_host'
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
        