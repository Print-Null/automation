
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


@allure.feature('MS-10000登录-线路管理-新建常规线路')
class Test_ms_van_line(object):

    @pytest.mark.parametrize("parameter",['{\'area\': \'\', \'driver\': \'$[config]driver$\', \'driver_phone\': \'$[config]driver_phone$\', \'fleet_id\': \'$fleetId$\', \'mode\': \'$[config]mode$\', \'name\': \'$[python]"YR"+str(int(round(time.time()*1000)))$\', \'period\': \'$[config]period$\', \'plate_id\': \'$ms_fleet_van_0_0_["data"]["items"][0]["id"]$\', \'plate_type\': \'$ms_fleet_van_0_0_["data"]["items"][0]["type"]$\', \'price\': \'$[config]price$\', \'sorting_no\': \'$[config]sorting_no$\', \'type\': \'$[config]type$\', \'time_tables\': [{\'estimate_end_time\': \'$[config]estimate_end_time_1$\', \'estimate_start_time\': \'$[config]estimate_start_time_1$\', \'order_no\': 1, \'running_mileage\': \'$[config]running_mileage_1$\', \'store_id\': \'$[config]store_id_1$\'}, {\'estimate_end_time\': \'$[config]estimate_end_time_2$\', \'estimate_start_time\': \'$[config]estimate_start_time_2$\', \'order_no\': 2, \'running_mileage\': \'$[config]running_mileage_2$\', \'store_id\': \'$[config]store_id_2$\'}]}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_2_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/van/line'])
    @pytest.mark.run(order=20)
    def test_test_ms_van_line(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'area\': \'\', \'driver\': \'$[config]driver$\', \'driver_phone\': \'$[config]driver_phone$\', \'fleet_id\': \'$fleetId$\', \'mode\': \'$[config]mode$\', \'name\': \'$[python]"YR"+str(int(round(time.time()*1000)))$\', \'period\': \'$[config]period$\', \'plate_id\': \'$ms_fleet_van_0_0_["data"]["items"][0]["id"]$\', \'plate_type\': \'$ms_fleet_van_0_0_["data"]["items"][0]["type"]$\', \'price\': \'$[config]price$\', \'sorting_no\': \'$[config]sorting_no$\', \'type\': \'$[config]type$\', \'time_tables\': [{\'estimate_end_time\': \'$[config]estimate_end_time_1$\', \'estimate_start_time\': \'$[config]estimate_start_time_1$\', \'order_no\': 1, \'running_mileage\': \'$[config]running_mileage_1$\', \'store_id\': \'$[config]store_id_1$\'}, {\'estimate_end_time\': \'$[config]estimate_end_time_2$\', \'estimate_start_time\': \'$[config]estimate_start_time_2$\', \'order_no\': 2, \'running_mileage\': \'$[config]running_mileage_2$\', \'store_id\': \'$[config]store_id_2$\'}]}']
        parameter_new = baseTest.parameter_parser(parameter)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_2_2_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/fleet/van/line']
        #redis里取plate_type也需要数据类型的转换
        # print(parameter_new) #str
        # print(type(parameter_new["plate_type"])) #str
        # # parameter_new["type"] = eval(parameter_new["type"])
        parameter_new["plate_type"] = eval(parameter_new["plate_type"])
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
        
        # logging.info("jsonschema文件path:../data/jsonschema/20_new_conventional_line.json")
        # with open("../data/jsonschema/20_new_conventional_line.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        