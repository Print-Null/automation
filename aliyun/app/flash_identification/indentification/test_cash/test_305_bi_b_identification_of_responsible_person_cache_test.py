
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


@allure.feature('bi普通客服，闪速认定操作b来源责任人认定')
class Test_bi_b_identification_of_responsible_person(object):

    @pytest.mark.parametrize("parameter",["{}"])
    @pytest.mark.parametrize("headers",["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_bi_usr_PHPSESSID$'}"])
    @pytest.mark.parametrize("address",['parcelloseapi/duty?$test_1_1_iframe_0$&$test_1_1_iframe_2$&$test_1_1_iframe_3$&$test_1_1_iframe_1$&task_id=$bi_qery_list_task_id$&unline=1&duty_type=7&duty_staff[0][duty_staff_type]=1&remark=单件有发无到，到件网点3小时内上报（3小时自卸车到件算起）发件网点和下一站网点双方责任&penaltyBase=1&link_type=1&flashout_staff_id='])
    @pytest.mark.run(order=305)
    def test_test_bi_b_identification_of_responsible_person(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{}"]
        
        _headers = ["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_bi_usr_PHPSESSID$'}"]
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
                
        _address = ['parcelloseapi/duty?$test_1_1_iframe_0$&$test_1_1_iframe_2$&$test_1_1_iframe_3$&$test_1_1_iframe_1$&task_id=$bi_qery_list_task_id$&unline=1&duty_type=7&duty_staff[0][duty_staff_type]=1&remark=单件有发无到，到件网点3小时内上报（3小时自卸车到件算起）发件网点和下一站网点双方责任&penaltyBase=1&link_type=1&flashout_staff_id=']
            
        host = 'fbi_host_domain'
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
            assert_that(resp.json()["msg"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("success")
        