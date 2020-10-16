
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


@allure.feature('单边->申请FD加班车')
class Test_backyard_overtime_car_fleet_addFleet_FD_unilateral(object):

    @pytest.mark.parametrize("parameter",['{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][0]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][1]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][2]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][3]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][4]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][5]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][6]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][7]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'BY-PLATFORM\': \'FB_ANDROID\'}'])
    @pytest.mark.parametrize("address",['api/_/fleet/addFleet'])
    @pytest.mark.run(order=60)
    def test_test_backyard_overtime_car_fleet_addFleet_FD_unilateral(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][0]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][1]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][2]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][3]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][4]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][5]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][6]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}', '{\'audit_type\': 2, \'car_type\': \'$backyard_overtime_car_fleet_getCarType_0_0_0_["data"]["dataList"]["car_type"][7]["type"]$\', \'capacity\': 44, \'arrive_time\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d 23:00\')$", \'start_store\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'end_store\': \'$backyard_overtime_car_hc_personInfo_1_0_["data"]["store_id"]$\', \'reason\': \'FD理由\', \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'fd_courier_phone\': 1111111111, \'fd_courier_plate\': 123, \'province_code\': \'TH05\'}']
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'BY-PLATFORM\': \'FB_ANDROID\'}']
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
                
        _address = ['api/_/fleet/addFleet']
        
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
        