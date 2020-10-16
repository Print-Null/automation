
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


@allure.feature('单边->经理->FD单条申请，审批详情页面')
class Test_backyard_overtime_car_auditlist_detail_FD_unilateral(object):

    @pytest.mark.parametrize("parameter",['{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][0]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][1]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][2]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][3]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][4]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][5]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][6]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][7]["id"]$\', \'type\': 12, \'isCommit\': 2}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-BY-SESSION-ID\': \'$backyard_overtime_car_manager_auth_new_device_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'BY-PLATFORM\': \'FB_ANDROID\'}'])
    @pytest.mark.parametrize("address",['api/_/auditlist/detail'])
    @pytest.mark.run(order=62)
    def test_test_backyard_overtime_car_auditlist_detail_FD_unilateral(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][0]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][1]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][2]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][3]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][4]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][5]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][6]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$backyard_overtime_car_api_auditList_getList_FD_unilateral_0_0_0_["data"]["dataList"][7]["id"]$\', \'type\': 12, \'isCommit\': 2}']
        
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
                
        _address = ['api/_/auditlist/detail']
        
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
        
        RedisBase().set('backyard_overtime_car_auditlist_detail_FD_unilateral_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["head"]["id"]', resp.json()["data"]["head"]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        