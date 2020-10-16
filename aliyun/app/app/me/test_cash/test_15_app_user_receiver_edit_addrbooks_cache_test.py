
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


@allure.feature('C客户修改收件地址信息')
class Test_app_user_receiver_edit_addrbooks(object):

    @pytest.mark.parametrize("parameter",['{\'district_code\': \'TH010201\', \'dst_home_phone\': \'\', \'detail_address\': \'$[python]"自动化测试收件地址修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'address_type\': 1, \'name\': \'$[python]"自动化收件人修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'postal_code\': \'10600\', \'dst_default\': False, \'province_code\': \'TH01\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'src_default\': True, \'city_code\': \'TH0102\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/user/v1/addrbooks/$app_user_receiver_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["id"]$'])
    @pytest.mark.run(order=15)
    def test_test_app_user_receiver_edit_addrbooks(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'district_code\': \'TH010201\', \'dst_home_phone\': \'\', \'detail_address\': \'$[python]"自动化测试收件地址修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'address_type\': 1, \'name\': \'$[python]"自动化收件人修改"+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(1,100))$\', \'country_code\': \'TH\', \'postal_code\': \'10600\', \'dst_default\': False, \'province_code\': \'TH01\', \'phone\': \'$[python]random.randint(10000000000,99999999999)$\', \'src_default\': True, \'city_code\': \'TH0102\'}']
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['/api/user/v1/addrbooks/$app_user_receiver_get_addrbooks_0_0_["data"]["user_addrbooks"][0]["id"]$']
            
        host = 'app_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        if "application/json" in str(headers).lower():
            resp = requests.patch(url = url, json = parameter_new, headers = headers_new, timeout = 120, verify = False)
        else:
            resp = requests.patch(url = url, data = parameter_new, headers = headers_new, timeout = 120, verify = False)
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
        
        logging.info("jsonschema文件path:../data/jsonschema/15_app_user_receiver_edit_addrbooks.json")
        with open("../data/jsonschema/15_app_user_receiver_edit_addrbooks.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        