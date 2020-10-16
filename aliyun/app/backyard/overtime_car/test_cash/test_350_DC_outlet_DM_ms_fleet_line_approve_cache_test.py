
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


@allure.feature('ms后台加班车审批列表->查询展示')
class Test_DC_outlet_DM_ms_fleet_line_approve(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$DC_outlet_DM_central_control_login_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=100&pageNum=1&startTime=$[python]datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")$&endTime=$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:59:59")$'])
    @pytest.mark.run(order=350)
    def test_test_DC_outlet_DM_ms_fleet_line_approve(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$DC_outlet_DM_central_control_login_0_0_0_["data"]["session_id"]$\', \'Accept\': \'application/json, text/plain, */*\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=100&pageNum=1&startTime=$[python]datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")$&endTime=$[python]datetime.datetime.now().strftime("%Y-%m-%d 23:59:59")$']
        
        host = 'ms_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        resp = requests.get(url=url, headers=headers_new, verify=False, timeout=120)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-1]["id"]', resp.json()["data"]["items"][-1]["id"], ex=6000)
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-2]["id"]', resp.json()["data"]["items"][-2]["id"], ex=6000)
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-3]["id"]', resp.json()["data"]["items"][-3]["id"], ex=6000)
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-4]["id"]', resp.json()["data"]["items"][-4]["id"], ex=6000)
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-5]["id"]', resp.json()["data"]["items"][-5]["id"], ex=6000)
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-6]["id"]', resp.json()["data"]["items"][-6]["id"], ex=6000)
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-7]["id"]', resp.json()["data"]["items"][-7]["id"], ex=6000)
        
        RedisBase().set('DC_outlet_DM_ms_fleet_line_approve_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][-8]["id"]', resp.json()["data"]["items"][-8]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        