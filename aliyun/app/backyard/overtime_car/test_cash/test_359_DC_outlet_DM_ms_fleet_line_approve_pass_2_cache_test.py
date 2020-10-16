
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


@allure.feature('加班车申请（中控审批界面）->审批通过')
class Test_DC_outlet_DM_ms_fleet_line_approve_pass_2(object):

    @pytest.mark.parametrize("parameter",['{\'car_type\': \'[int]$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["car_type"]$\', \'fleet_id\': \'$DC_outlet_DM_ms_van_info_query_0_0_0_["data"][2]["line_van_query_dto"]["fleet_id"]$\', \'plan_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'single_line\': 2, \'plan_back_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'system_quote\': None, \'abnormal_cost\': None, \'final_cost\': 3300, \'line_cost\': 1100, \'line_back_cost\': 2200, \'line_name\': \'DD1-$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["car_type_text"]$-LT1-3421-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:10")$\', \'line_back_name\': \'DD2-$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["car_type_text"]$-3421-LT1-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:40")$\', \'driver\': \'autoname\', \'driver_phone\': \'1111111111\', \'province_code\': \'$DC_outlet_DM_ms_van_info_query_0_0_0_["data"][2]["line_van_query_dto"]["province_code"]$\', \'plate_name\': \'$[python]random.randint(100000000,9999999999)$\', \'audit_type\': 1, \'fd_courier_id\': \'None\', \'fd_courier_name\': \'None\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["start_store"]$\', \'estimate_end_time\': \'1380\', \'estimate_start_time\': \'1390\'}, {\'order_no\': 2, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1400\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1420\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$DC_outlet_DM_central_control_login_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve/$DC_outlet_DM_ms_fleet_line_approve_0_0_["data"]["items"][-3]["id"]$/pass'])
    @pytest.mark.run(order=359)
    def test_test_DC_outlet_DM_ms_fleet_line_approve_pass_2(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'car_type\': \'[int]$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["car_type"]$\', \'fleet_id\': \'$DC_outlet_DM_ms_van_info_query_0_0_0_["data"][2]["line_van_query_dto"]["fleet_id"]$\', \'plan_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'single_line\': 2, \'plan_back_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'system_quote\': None, \'abnormal_cost\': None, \'final_cost\': 3300, \'line_cost\': 1100, \'line_back_cost\': 2200, \'line_name\': \'DD1-$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["car_type_text"]$-LT1-3421-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:10")$\', \'line_back_name\': \'DD2-$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["car_type_text"]$-3421-LT1-$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:40")$\', \'driver\': \'autoname\', \'driver_phone\': \'1111111111\', \'province_code\': \'$DC_outlet_DM_ms_van_info_query_0_0_0_["data"][2]["line_van_query_dto"]["province_code"]$\', \'plate_name\': \'$[python]random.randint(100000000,9999999999)$\', \'audit_type\': 1, \'fd_courier_id\': \'None\', \'fd_courier_name\': \'None\', \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["start_store"]$\', \'estimate_end_time\': \'1380\', \'estimate_start_time\': \'1390\'}, {\'order_no\': 2, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["end_store"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1400\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["end_store"]$\', \'estimate_end_time\': \'1410\', \'estimate_start_time\': \'1420\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$DC_outlet_DM_ms_api_fleet_line_approve_0_2_["data"]["start_store"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1430\'}]}']
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$DC_outlet_DM_central_control_login_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}']
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
                
        _address = ['ms/api/fleet/line/approve/$DC_outlet_DM_ms_fleet_line_approve_0_0_["data"]["items"][-3]["id"]$/pass']
        
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
        