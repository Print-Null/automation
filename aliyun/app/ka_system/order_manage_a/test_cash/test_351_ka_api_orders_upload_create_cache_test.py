
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


@allure.feature('大客户导入订单')
class Test_ka_api_orders_upload_create(object):

    @pytest.mark.parametrize("parameter",['{\'src_name\': \'$[python]"order import"+str(random.randint(1,100000))$\', \'src_phone\': \'$[python]"0199"+str(random.randint(100000,999999))$\', \'src_district_code\': \'TH010103\', \'src_detail_address\': \'$[python]"order import detail address"+str(random.randint(1,1000000))$\', \'src_postal_code\': \'10260\', \'disData\': \'พระโขนง-คลองเตย-กรุงเทพ-10260\', \'file_name\': \'$[config]excel_name$\', \'object_key\': \'$[config]object_key$\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'th\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['/ka/api/orders/upload/create'])
    @pytest.mark.run(order=351)
    def test_test_ka_api_orders_upload_create(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'src_name\': \'$[python]"order import"+str(random.randint(1,100000))$\', \'src_phone\': \'$[python]"0199"+str(random.randint(100000,999999))$\', \'src_district_code\': \'TH010103\', \'src_detail_address\': \'$[python]"order import detail address"+str(random.randint(1,1000000))$\', \'src_postal_code\': \'10260\', \'disData\': \'พระโขนง-คลองเตย-กรุงเทพ-10260\', \'file_name\': \'$[config]excel_name$\', \'object_key\': \'$[config]object_key$\'}']
        
        _headers = ['{\'content-type\': \'application/json;charset=UTF-8\', \'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'th\', \'X-KA-SESSION-ID\': \'$ka_api_auth_signin_0_0_0_["data"]["session_id"]$\'}']
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
                
        _address = ['/ka/api/orders/upload/create']
            
        host = 'ka_system_host'
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
        