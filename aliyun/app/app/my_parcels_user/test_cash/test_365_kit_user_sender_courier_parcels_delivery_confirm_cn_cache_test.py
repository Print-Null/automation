
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


@allure.feature('kit运单妥投')
class Test_kit_user_sender_courier_parcels_delivery_confirm_cn(object):

    @pytest.mark.parametrize("parameter",["{'signer_category': 0, 'sign_image_key': 'deliveryPickupsMarkUpload/1554113259-2ee455ae43ac41208ae7a6396f462e15', 'signer_content': '$[config]user_dst_name$', 'call_duration': 200}"])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_user_sender_courier_new_device_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/courier/v1/ticket/parcels/$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][1]["pno"]$/delivery_confirm'])
    @pytest.mark.run(order=365)
    def test_test_kit_user_sender_courier_parcels_delivery_confirm_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'signer_category': 0, 'sign_image_key': 'deliveryPickupsMarkUpload/1554113259-2ee455ae43ac41208ae7a6396f462e15', 'signer_content': '$[config]user_dst_name$', 'call_duration': 200}"]
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_user_sender_courier_new_device_login_cn_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['/api/courier/v1/ticket/parcels/$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][1]["pno"]$/delivery_confirm']
            
        host = 'kit_host'
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
        
        logging.info("jsonschema文件path:../data/jsonschema/15_kit_user_sender_courier_parcels_delivery_confirm_cn.json")
        with open("../data/jsonschema/15_kit_user_sender_courier_parcels_delivery_confirm_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        