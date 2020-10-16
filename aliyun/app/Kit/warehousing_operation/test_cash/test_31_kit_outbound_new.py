
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


@allure.feature('仓管员-车辆出港-封车')
class Test_kit_outbound_new(object):

    @pytest.mark.parametrize("parameter",['{\'fleet_bound_images\': [{\'sealing_number\': \'$[python]random.choice(["P","V","A"])+str(random.randint(0000000000,9999999999))$\'}], \'outbound_autograph_image\': {\'image_key\': \'$kit_fleet_autograph_#headers#_0_["data"]["object_key"]$\', \'image_name\': \'$kit_fleet_autograph_#headers#_0_["data"]["object_key"]$\'}, \'outbound_image\': {\'image_key\': \'fleetOutbound/1595596630-630ad43d97d5429893d4079a581bf11c.jpg\', \'image_name\': \'1595596630-630ad43d97d5429893d4079a581bf11c.jpg\'}, \'signer_content\': \'$[config]signer_content$\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/fleet/proof/outbound/new/$ms_van_proof_0_#headers#_0_["data"]["id"]$'])
    @pytest.mark.run(order=31)
    def test_test_kit_outbound_new(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'fleet_bound_images\': [{\'sealing_number\': \'$[python]random.choice(["P","V","A"])+str(random.randint(0000000000,9999999999))$\'}], \'outbound_autograph_image\': {\'image_key\': \'$kit_fleet_autograph_#headers#_0_["data"]["object_key"]$\', \'image_name\': \'$kit_fleet_autograph_#headers#_0_["data"]["object_key"]$\'}, \'outbound_image\': {\'image_key\': \'fleetOutbound/1595596630-630ad43d97d5429893d4079a581bf11c.jpg\', \'image_name\': \'1595596630-630ad43d97d5429893d4079a581bf11c.jpg\'}, \'signer_content\': \'$[config]signer_content$\'}']
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/courier/v1/fleet/proof/outbound/new/$ms_van_proof_0_#headers#_0_["data"]["id"]$']
            
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

        # 存储封车条号
        RedisBase().set('sealing_number', parameter_new["fleet_bound_images"][0]["sealing_number"], ex=6000)
        print("本次的封车条号是：{0}".format(parameter_new["fleet_bound_images"][0]["sealing_number"]))

        # logging.info("jsonschema文件path:../data/jsonschema/31_vehicle_closure.json")
        # with open("../data/jsonschema/31_vehicle_closure.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        