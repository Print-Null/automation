
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


@allure.feature('新建常规线路')
class Test_new_general_line(object):

    @pytest.mark.parametrize("parameter",['{\'name\': \'auto$[python]str(time.time()).split(".")[0]$\', \'area\': \'\', \'type\': 0, \'mode\': 1, \'period\': [1, 2, 3, 4, 5, 6, 7], \'price\': 2200, \'fleet_id\': \'$get_plate_number_0_0_["data"]["items"][0]["fleet_id"]$\', \'plate_id\': \'$get_plate_number_0_0_["data"]["items"][0]["id"]$\', \'plate_type\': 100, \'driver\': \'autotest\', \'driver_phone\': \'1111111111\', \'time_tables\': [{\'order_no\': 1, \'store_id\': \'$id_1$\', \'estimate_end_time\': \'960\', \'estimate_start_time\': \'990\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$id_2$\', \'running_mileage\': \'111\', \'estimate_start_time\': None, \'estimate_end_time\': \'1086\'}], \'sorting_no\': \'B\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'th-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/van/line'])
    @pytest.mark.run(order=13)
    def test_test_new_general_line(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'name\': \'auto$[python]str(time.time()).split(".")[0]$\', \'area\': \'\', \'type\': 0, \'mode\': 1, \'period\': [1, 2, 3, 4, 5, 6, 7], \'price\': 2200, \'fleet_id\': \'$get_plate_number_0_0_["data"]["items"][0]["fleet_id"]$\', \'plate_id\': \'$get_plate_number_0_0_["data"]["items"][0]["id"]$\', \'plate_type\': 100, \'driver\': \'autotest\', \'driver_phone\': \'1111111111\', \'time_tables\': [{\'order_no\': 1, \'store_id\': \'$id_1$\', \'estimate_end_time\': \'960\', \'estimate_start_time\': \'990\', \'running_mileage\': \'\'}, {\'order_no\': 2, \'store_id\': \'$id_2$\', \'running_mileage\': \'111\', \'estimate_start_time\': None, \'estimate_end_time\': \'1086\'}], \'sorting_no\': \'B\'}']
        
        _headers = ['{\'Accept-Language\': \'th-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}']
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
                
        _address = ['ms/api/fleet/van/line']
        
        host = 'host_10000'
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
        
        # logging.info("jsonschema文件path:../data/jsonschema/13new_general_line.json")
        # with open("../data/jsonschema/13new_general_line.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        