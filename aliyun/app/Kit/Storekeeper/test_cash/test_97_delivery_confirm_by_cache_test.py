
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


@allure.feature('确认妥投接口')
class Test_delivery_confirm_by(object):

    @pytest.mark.parametrize("parameter",["{'call_duration': 0, 'continue_payment_flag': False, 'other_image_key': 'deliveryConfirmOther/1587116862-78d4d55fbb92493e91050149d966d461.jpg', 'payment_category': 1, 'signer_category': 0, 'signer_content': '确认妥投'}"])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'th-CN\', \'By-Platform\': \'RB_KIT\', \'Content-Type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\', \'X-DEVICE-ID\': \'8673510346528821571665712622\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/ticket/parcels/$courier_pno_number34$/delivery_confirm'])
    @pytest.mark.run(order=97)
    def test_test_delivery_confirm_by(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'call_duration': 0, 'continue_payment_flag': False, 'other_image_key': 'deliveryConfirmOther/1587116862-78d4d55fbb92493e91050149d966d461.jpg', 'payment_category': 1, 'signer_category': 0, 'signer_content': '确认妥投'}"]
        
        _headers = ['{\'Accept-Language\': \'th-CN\', \'By-Platform\': \'RB_KIT\', \'Content-Type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\', \'X-DEVICE-ID\': \'8673510346528821571665712622\'}']
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
                
        _address = ['api/courier/v1/ticket/parcels/$courier_pno_number34$/delivery_confirm']
        
        host = 'host'
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
        
        # logging.info("jsonschema文件path:../data/jsonschema/97delivery_confirm_by.json")
        # with open("../data/jsonschema/97delivery_confirm_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        #