
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


@allure.feature('网点经理->待处理列表展示')
class Test_backyard_overtime_car_api_auditList_getList(object):

    @pytest.mark.parametrize("parameter",["{'audit_show_type': 2, 'audit_state_type': 1, 'page_num': 1}"])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json\', \'BY-PLATFORM\': \'FB_ANDROID\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-US\', \'Content-Type\': \'application/json\', \'BY-PLATFORM\': \'FB_ANDROID\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Content-Type\': \'application/json\', \'BY-PLATFORM\': \'FB_ANDROID\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/_/auditList/getList'])
    @pytest.mark.run(order=58)
    def test_test_backyard_overtime_car_api_auditList_getList(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'audit_show_type': 2, 'audit_state_type': 1, 'page_num': 1}"]
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json\', \'BY-PLATFORM\': \'FB_ANDROID\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-US\', \'Content-Type\': \'application/json\', \'BY-PLATFORM\': \'FB_ANDROID\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Content-Type\': \'application/json\', \'BY-PLATFORM\': \'FB_ANDROID\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/_/auditList/getList']
        
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
        
        RedisBase().set('backyard_overtime_car_api_auditList_getList_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["dataList"][0]["id"]', resp.json()["data"]["dataList"][0]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        
        # logging.info("jsonschema文件path:../data/jsonschema/58backyard_overtime_car_api_auditList_getList.json")
        # with open("../data/jsonschema/58backyard_overtime_car_api_auditList_getList.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        