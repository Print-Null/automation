
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


@allure.feature('网点经理->加班车申请（中控审批界面）->审批通过')
class Test_manager_backyard_overtime_car_ms_api_fleet_line_approve_pass_FD_7(object):

    @pytest.mark.parametrize("parameter",['{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_7_["data"]["car_type"]$\', \'fleet_id\': \'$backyard_overtime_car_ms_approve_van_info_query_FD_0_0_0_["data"][6]["line_van_query_dto"]["fleet_id"]$\', \'plan_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'single_line\': 2, \'plan_back_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'system_quote\': None, \'abnormal_cost\': None, \'final_cost\': 5500, \'line_cost\': 2200, \'line_back_cost\': 3300, \'line_name\': \'FDC1-$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["car_type_text"]$-LT1-3421-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:30")$\', \'line_back_name\': \'FDC2-$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["car_type_text"]$-3421-LT1-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:30")$\', \'driver\': \'autoTest\', \'driver_phone\': \'1111111111\', \'province_code\': \'$backyard_overtime_car_ms_approve_van_info_query_FD_0_0_0_["data"][6]["line_van_query_dto"]["province_code"]$\', \'plate_name\': \'$[python]random.randint(100000000,9999999999)$\', \'audit_type\': 2, \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["start_store"]$\', \'estimate_end_time\': \'861\', \'estimate_start_time\': \'921\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'981\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["end_store"]$\', \'estimate_end_time\': \'1041\', \'estimate_start_time\': \'1101\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1162\'}]}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve/$manager_backyard_overtime_car_ms_fleet_line_approve_FD_0_0_["data"]["items"][-8]["id"]$/pass'])
    @pytest.mark.run(order=99)
    def test_test_manager_backyard_overtime_car_ms_api_fleet_line_approve_pass_FD_7(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_7_["data"]["car_type"]$\', \'fleet_id\': \'$backyard_overtime_car_ms_approve_van_info_query_FD_0_0_0_["data"][6]["line_van_query_dto"]["fleet_id"]$\', \'plan_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'single_line\': 2, \'plan_back_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'system_quote\': None, \'abnormal_cost\': None, \'final_cost\': 5500, \'line_cost\': 2200, \'line_back_cost\': 3300, \'line_name\': \'FDC1-$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["car_type_text"]$-LT1-3421-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:30")$\', \'line_back_name\': \'FDC2-$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["car_type_text"]$-3421-LT1-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:30")$\', \'driver\': \'autoTest\', \'driver_phone\': \'1111111111\', \'province_code\': \'$backyard_overtime_car_ms_approve_van_info_query_FD_0_0_0_["data"][6]["line_van_query_dto"]["province_code"]$\', \'plate_name\': \'$[python]random.randint(100000000,9999999999)$\', \'audit_type\': 2, \'fd_courier_id\': \'$[config]courier$\', \'fd_courier_name\': \'autoTest\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["start_store"]$\', \'estimate_end_time\': \'861\', \'estimate_start_time\': \'921\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'981\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["end_store"]$\', \'estimate_end_time\': \'1041\', \'estimate_start_time\': \'1101\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_FD_0_6_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1162\'}]}']
        
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
                
        _address = ['ms/api/fleet/line/approve/$manager_backyard_overtime_car_ms_fleet_line_approve_FD_0_0_["data"]["items"][-8]["id"]$/pass']
        
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
        