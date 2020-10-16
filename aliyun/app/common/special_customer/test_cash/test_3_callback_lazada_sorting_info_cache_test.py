
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


@allure.feature('lazada_sorting_info')
class Test_callback_lazada_sorting_info(object):

    @pytest.mark.parametrize("parameter",['{\'req\': {\'shipment\': {\'con_no\': \'$callback_lazada_con_no_0_0_0_["res"]["shipment"]["con_no"]$\'}}}', '{\'req\': {\'shipment\': {\'con_no\': \'$callback_lazada_con_no_1_0_0_["res"]["shipment"]["con_no"]$\'}}}'])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$'}"])
    @pytest.mark.parametrize("address",['/callback/lazada/sorting_info'])
    @pytest.mark.run(order=3)
    def test_test_callback_lazada_sorting_info(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'req\': {\'shipment\': {\'con_no\': \'$callback_lazada_con_no_0_0_0_["res"]["shipment"]["con_no"]$\'}}}', '{\'req\': {\'shipment\': {\'con_no\': \'$callback_lazada_con_no_1_0_0_["res"]["shipment"]["con_no"]$\'}}}']
        
        _headers = ["{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$'}"]
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
                
        _address = ['/callback/lazada/sorting_info']
            
        host = 'common_host'
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
        
        assert_that(resp.json()["res"]["shipment"]["status_code"]).is_equal_to('000')
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        