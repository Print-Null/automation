
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


@allure.feature('网点经理->加班车申请（中控审批界面）->系统报价')
class Test_manager_backyard_overtime_car_ms_approve_price_matching(object):

    @pytest.mark.parametrize("parameter",['{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve/price_matching'])
    @pytest.mark.run(order=79)
    def test_test_manager_backyard_overtime_car_ms_approve_price_matching(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_1_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_2_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_3_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_4_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_5_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_6_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}', '{\'car_type\': \'[int]$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["car_type"]$\', \'single_line\': \'[int]2\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["start_store"]$\', \'estimate_end_time\': \'1399\', \'estimate_start_time\': \'1401\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1039\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1415\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$manager_backyard_overtime_car_ms_api_fleet_line_approve_1_0_7_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}']
        
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
                
        _address = ['ms/api/fleet/line/approve/price_matching']
        
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
        