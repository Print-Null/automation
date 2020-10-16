
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


@allure.feature('kit快递员查看完成揽收的订单包裹信息')
class Test_kit_user_sender_courier_ticket_pickups_cn(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'en-US\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_user_sender_courier_new_device_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/courier/v1/ticket/pickups/$app_user_sender_ticket_pickup_list_cn_0_0_["data"]["list"][0]["id"]$'])
    @pytest.mark.run(order=361)
    def test_test_kit_user_sender_courier_ticket_pickups_cn(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'en-US\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_user_sender_courier_new_device_login_cn_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/courier/v1/ticket/pickups/$app_user_sender_ticket_pickup_list_cn_0_0_["data"]["list"][0]["id"]$']
            
        host = 'kit_host'
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
        
        RedisBase().set('kit_user_sender_courier_ticket_pickups_cn_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["collected_parcels"][0]["pno"]', resp.json()["data"]["collected_parcels"][0]["pno"], ex=6000)
        
        RedisBase().set('kit_user_sender_courier_ticket_pickups_cn_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["collected_parcels"][1]["pno"]', resp.json()["data"]["collected_parcels"][1]["pno"], ex=6000)
        
        RedisBase().set('kit_user_sender_courier_ticket_pickups_cn_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["collected_parcels"][2]["pno"]', resp.json()["data"]["collected_parcels"][2]["pno"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/11_kit_user_sender_courier_ticket_pickups_cn.json")
        with open("../data/jsonschema/11_kit_user_sender_courier_ticket_pickups_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        