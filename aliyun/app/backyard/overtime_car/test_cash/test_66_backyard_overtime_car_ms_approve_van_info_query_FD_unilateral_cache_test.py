
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


@allure.feature('单边->FD加班车申请（中控审批界面）->车牌号模糊查询')
class Test_backyard_overtime_car_ms_approve_van_info_query_FD_unilateral(object):

    @pytest.mark.parametrize("parameter",["{'plate_name': '3', 'province_code': 'TH01', 'fuzzy': True}"])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve/van_info_query'])
    @pytest.mark.run(order=66)
    def test_test_backyard_overtime_car_ms_approve_van_info_query_FD_unilateral(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'plate_name': '3', 'province_code': 'TH01', 'fuzzy': True}"]
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}']
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
                
        _address = ['ms/api/fleet/line/approve/van_info_query']
        
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
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][0]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][0]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][0]["line_van_query_dto"]["province_code"]', resp.json()["data"][0]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][0]["plate_name"]', resp.json()["data"][0]["plate_name"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][1]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][1]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][1]["line_van_query_dto"]["province_code"]', resp.json()["data"][1]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][1]["plate_name"]', resp.json()["data"][1]["plate_name"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][2]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][2]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][2]["line_van_query_dto"]["province_code"]', resp.json()["data"][2]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][2]["plate_name"]', resp.json()["data"][2]["plate_name"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][3]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][3]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][3]["line_van_query_dto"]["province_code"]', resp.json()["data"][3]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][3]["plate_name"]', resp.json()["data"][3]["plate_name"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][4]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][4]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][4]["line_van_query_dto"]["province_code"]', resp.json()["data"][4]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][4]["plate_name"]', resp.json()["data"][4]["plate_name"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][5]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][5]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][5]["line_van_query_dto"]["province_code"]', resp.json()["data"][5]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][5]["plate_name"]', resp.json()["data"][5]["plate_name"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][6]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][6]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][6]["line_van_query_dto"]["province_code"]', resp.json()["data"][6]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][6]["plate_name"]', resp.json()["data"][6]["plate_name"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][7]["line_van_query_dto"]["fleet_id"]', resp.json()["data"][7]["line_van_query_dto"]["fleet_id"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][7]["line_van_query_dto"]["province_code"]', resp.json()["data"][7]["line_van_query_dto"]["province_code"], ex=6000)
        
        RedisBase().set('backyard_overtime_car_ms_approve_van_info_query_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"][7]["plate_name"]', resp.json()["data"][7]["plate_name"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        