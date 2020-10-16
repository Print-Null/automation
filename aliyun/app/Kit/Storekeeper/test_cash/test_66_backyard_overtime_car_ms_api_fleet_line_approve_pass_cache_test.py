
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
class Test_backyard_overtime_car_ms_api_fleet_line_approve_pass(object):

    @pytest.mark.parametrize("parameter",['{\'car_type\': 200, \'fleet_id\': \'$backyard_overtime_car_ms_approve_van_info_query_0_0_0_["data"][0]["line_van_query_dto"]["fleet_id"]$\', \'plan_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'single_line\': 1, \'system_quote\': None, \'abnormal_cost\': None, \'final_cost\': 2200, \'line_cost\': 2200, \'line_back_cost\': None, \'line_name\': \'DD1-$backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["car_type_text"]$-LT1-3421-$datetime.datetime.now().strftime("%Y%m%d 23:10")$\', \'line_back_name\': \'DD2-$backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["car_type_text"]$-3421-LT1-null null\', \'driver\': \'autoname\', \'driver_phone\': \'111111111\', \'province_code\': \'$backyard_overtime_car_ms_approve_van_info_query_0_0_0_["data"][0]["line_van_query_dto"]["province_code"]$\', \'plate_name\': \'$[python]str(random.randint(100000000,9999999999))$\', \'audit_type\': 1, \'fd_courier_id\': None, \'fd_courier_name\': None, \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'estimate_end_time\': \'1380\', \'estimate_start_time\': \'1390\'}, {\'order_no\': 2, \'store_id\': \'$backyard_overtime_car_hc_personInfo_end_0_0_["data"]["store_id"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1400\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$backyard_overtime_car_hc_personInfo_end_0_0_["data"]["store_id"]$\', \'estimate_end_time\': \'\', \'estimate_start_time\': \'\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'\'}]}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'th-CN\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve/$backyard_overtime_car_ms_fleet_line_approve_0_0_["data"]["items"][-1]["id"]$/pass'])
    @pytest.mark.run(order=66)
    def test_test_backyard_overtime_car_ms_api_fleet_line_approve_pass(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'car_type\': 200, \'fleet_id\': \'$backyard_overtime_car_ms_approve_van_info_query_0_0_0_["data"][0]["line_van_query_dto"]["fleet_id"]$\', \'plan_date\': "$[python]datetime.datetime.now().strftime(\'%Y-%m-%d\')$", \'single_line\': 1, \'system_quote\': None, \'abnormal_cost\': None, \'final_cost\': 2200, \'line_cost\': 2200, \'line_back_cost\': None, \'line_name\': \'DD1-$backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["car_type_text"]$-LT1-3421-$datetime.datetime.now().strftime("%Y%m%d 23:10")$\', \'line_back_name\': \'DD2-$backyard_overtime_car_ms_api_fleet_line_approve_1_0_0_["data"]["car_type_text"]$-3421-LT1-null null\', \'driver\': \'autoname\', \'driver_phone\': \'111111111\', \'province_code\': \'$backyard_overtime_car_ms_approve_van_info_query_0_0_0_["data"][0]["line_van_query_dto"]["province_code"]$\', \'plate_name\': \'$[python]str(random.randint(100000000,9999999999))$\', \'audit_type\': 1, \'fd_courier_id\': None, \'fd_courier_name\': None, \'line_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'estimate_end_time\': \'1380\', \'estimate_start_time\': \'1390\'}, {\'order_no\': 2, \'store_id\': \'$backyard_overtime_car_hc_personInfo_end_0_0_["data"]["store_id"]$\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'1400\'}], \'line_back_timetable_dtolist\': [{\'order_no\': 1, \'store_id\': \'$backyard_overtime_car_hc_personInfo_end_0_0_["data"]["store_id"]$\', \'estimate_end_time\': \'\', \'estimate_start_time\': \'\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$backyard_overtime_car_hc_personInfo_0_0_["data"]["store_id"]$\', \'running_mileage\': \'\', \'estimate_start_time\': \'\', \'estimate_end_time\': \'\'}]}']
        
        _headers = ['{\'Accept-Language\': \'th-CN\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'X-MS-SESSION-ID\': \'$backyard_overtime_car_ms_api_auth_signin_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                
        _address = ['ms/api/fleet/line/approve/$backyard_overtime_car_ms_fleet_line_approve_0_0_["data"]["items"][-1]["id"]$/pass']
        
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
        
        # logging.info("jsonschema文件path:../data/jsonschema/66backyard_overtime_car_ms_api_fleet_line_approve_pass.json")
        # with open("../data/jsonschema/66backyard_overtime_car_ms_api_fleet_line_approve_pass.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        