
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


@allure.feature('仓管员-悬浮按钮-拨打收件人手机号')
class Test_kit_ticket_hover_button_phone_contact(object):

    @pytest.mark.parametrize("parameter",['{\'form\': {\'call_duration\': 0, \'call_type\': 2, \'calling_channel\': 2, \'diabolo_duration\': 0, \'phone\': \'$kit_v1_parcels_storekeeper_0_0_["data"]["dst_phone"]$\', \'start_time\': 1597127832}, \'pno\': \'$kit_pickups_parcel_1_0_0_["data"]["parcel_info"]["pno"]$\', \'report_at\': 1597127833}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_storekeeper_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/ticket/hover_button_phone_contact'])
    @pytest.mark.run(order=431)
    def test_test_kit_ticket_hover_button_phone_contact(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'form\': {\'call_duration\': 0, \'call_type\': 2, \'calling_channel\': 2, \'diabolo_duration\': 0, \'phone\': \'$kit_v1_parcels_storekeeper_0_0_["data"]["dst_phone"]$\', \'start_time\': 1597127832}, \'pno\': \'$kit_pickups_parcel_1_0_0_["data"]["parcel_info"]["pno"]$\', \'report_at\': 1597127833}']
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_storekeeper_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/courier/v1/ticket/hover_button_phone_contact']
            
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
        