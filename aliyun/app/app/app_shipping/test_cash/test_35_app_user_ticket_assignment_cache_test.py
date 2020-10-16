
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


@allure.feature('C客户呼叫快递员并分配')
class Test_app_user_ticket_assignment(object):

    @pytest.mark.parametrize("parameter",['{\'src_postal_code\': \'$app_maps_place_detail_0_0_0_["data"][0]["postal_code"]$\', \'src_name\': \'$[python]"C客户自动化快递员"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'src_phone\': \'$[python]random.choice(["134","135"])+str(random.randint(1000000,99999999))$\', \'src_city_code\': \'TH0141\', \'src_detail_address\': \'$app_maps_place_detail_0_0_0_["data"][0]["detail_address"]$\', \'src_district_code\': \'TH014101\', \'src_lng\': \'$app_maps_place_detail_0_0_0_["data"][0]["lng"]$\', \'estimate_parcel_number\': \'$[python]random.randint(1,500)$\', \'src_lat\': \'$app_maps_place_detail_0_0_0_["data"][0]["lat"]$\', \'src_country_code\': \'TH\', \'remark\': \'带文件袋 M号箱x1,\', \'src_province_code\': \'TH01\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/user/v1/ticket/assignment'])
    @pytest.mark.run(order=35)
    def test_test_app_user_ticket_assignment(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'src_postal_code\': \'$app_maps_place_detail_0_0_0_["data"][0]["postal_code"]$\', \'src_name\': \'$[python]"C客户自动化快递员"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'src_phone\': \'$[python]random.choice(["134","135"])+str(random.randint(1000000,99999999))$\', \'src_city_code\': \'TH0141\', \'src_detail_address\': \'$app_maps_place_detail_0_0_0_["data"][0]["detail_address"]$\', \'src_district_code\': \'TH014101\', \'src_lng\': \'$app_maps_place_detail_0_0_0_["data"][0]["lng"]$\', \'estimate_parcel_number\': \'$[python]random.randint(1,500)$\', \'src_lat\': \'$app_maps_place_detail_0_0_0_["data"][0]["lat"]$\', \'src_country_code\': \'TH\', \'remark\': \'带文件袋 M号箱x1,\', \'src_province_code\': \'TH01\'}']
        parameter_new = baseTest.parameter_parser(parameter)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/user/v1/ticket/assignment']
            
        host = 'app_host'
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
        