
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


@allure.feature('经理->单条申请，同意->FD')
class Test_backyard_overtime_car_fleet_updateFleet_FD(object):

    @pytest.mark.parametrize("parameter",['{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_0_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_1_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_2_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_3_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_4_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_5_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_6_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_7_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'BY-PLATFORM\': \'FB_ANDROID\'}'])
    @pytest.mark.parametrize("address",['api/_/fleet/updateFleet'])
    @pytest.mark.run(order=31)
    def test_test_backyard_overtime_car_fleet_updateFleet_FD(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_0_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_1_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_2_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_3_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_4_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_5_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_6_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}', '{\'status\': 2, \'audit_id\': \'$backyard_overtime_car_auditlist_detail_FD_7_0_0_["data"]["head"]["id"]$\', \'reject_reason\': \'1\'}']
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'BY-PLATFORM\': \'FB_ANDROID\'}']
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
                
        _address = ['api/_/fleet/updateFleet']
        
        host = 'backyard_host'
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
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        