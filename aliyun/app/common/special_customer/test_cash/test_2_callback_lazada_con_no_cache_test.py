
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


@allure.feature('lazada_con_no')
class Test_callback_lazada_con_no(object):

    @pytest.mark.parametrize("parameter",["{'req': {'shipment': {'s_zipcode': '58120', 's_address': '89/78 IIII คอนโด ซอยทองหล่อ 90, เพชรบูรณ์/ Phetchabun, วิเชียรบุรี/ Wichian Buri, 67180', 's_district': 'แม่ลาน้อย/ Mae La Noi', 's_province': 'แม่ฮ่องสอน/ Mae Hong Son', 's_subdistrict': '-', 'r_zipcode': '67180', 'r_address': '71/41 ABC คอนโด ซอยลาดพร้าว 20, แม่ฮ่องสอน/ Mae Hong Son, แม่ลาน้อย/ Mae La Noi, 67180', 'r_district': 'วิเชียรบุรี/ Wichian Buri', 'r_subdistrict': '-', 'r_province': 'เพชรบูรณ์/ Phetchabun'}}}", "{'req': {'shipment': {'s_zipcode': '58120', 's_address': '89/78 IIII คอนโด , เพชรบูรณ์/ Phetchabun, วิเชียรบุรี/ Wichian Buri, 67180', 's_district': 'แม่ลาน้อย/ Mae La Noi', 's_province': 'แม่ฮ่องสอน/ Mae Hong Son', 's_subdistrict': '-', 'r_zipcode': '67180', 'r_address': '71/41 ABC คอนโด , แม่ฮ่องสอน/ Mae Hong Son, แม่ลาน้อย/ Mae La Noi, 67180', 'r_district': 'วิเชียรบุรี/ Wichian Buri', 'r_subdistrict': '-', 'r_province': 'เพชรบูรณ์/ Phetchabun'}}}"])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$'}"])
    @pytest.mark.parametrize("address",['/callback/lazada/con_no'])
    @pytest.mark.run(order=2)
    def test_test_callback_lazada_con_no(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'req': {'shipment': {'s_zipcode': '58120', 's_address': '89/78 IIII คอนโด ซอยทองหล่อ 90, เพชรบูรณ์/ Phetchabun, วิเชียรบุรี/ Wichian Buri, 67180', 's_district': 'แม่ลาน้อย/ Mae La Noi', 's_province': 'แม่ฮ่องสอน/ Mae Hong Son', 's_subdistrict': '-', 'r_zipcode': '67180', 'r_address': '71/41 ABC คอนโด ซอยลาดพร้าว 20, แม่ฮ่องสอน/ Mae Hong Son, แม่ลาน้อย/ Mae La Noi, 67180', 'r_district': 'วิเชียรบุรี/ Wichian Buri', 'r_subdistrict': '-', 'r_province': 'เพชรบูรณ์/ Phetchabun'}}}", "{'req': {'shipment': {'s_zipcode': '58120', 's_address': '89/78 IIII คอนโด , เพชรบูรณ์/ Phetchabun, วิเชียรบุรี/ Wichian Buri, 67180', 's_district': 'แม่ลาน้อย/ Mae La Noi', 's_province': 'แม่ฮ่องสอน/ Mae Hong Son', 's_subdistrict': '-', 'r_zipcode': '67180', 'r_address': '71/41 ABC คอนโด , แม่ฮ่องสอน/ Mae Hong Son, แม่ลาน้อย/ Mae La Noi, 67180', 'r_district': 'วิเชียรบุรี/ Wichian Buri', 'r_subdistrict': '-', 'r_province': 'เพชรบูรณ์/ Phetchabun'}}}"]
        
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
                
        _address = ['/callback/lazada/con_no']
            
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
        
        RedisBase().set('callback_lazada_con_no_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["res"]["shipment"]["con_no"]', resp.json()["res"]["shipment"]["con_no"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["res"]["shipment"]["status_code"]).is_equal_to('000')
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        