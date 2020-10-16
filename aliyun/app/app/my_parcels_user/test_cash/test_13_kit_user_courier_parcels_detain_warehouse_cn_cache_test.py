
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


@allure.feature('快递员确认取消寄件')
class Test_kit_user_courier_parcels_detain_warehouse_cn(object):

    @pytest.mark.parametrize("parameter",["{'detained_marker_category': 15, 'from_scanner': False, 'image_keys': ['parcelManualImport/1596098096-79ece17d5fbd4cb7bdb30ed2f8b2f0b8.jpg'], 'parcel_scan_manual_import_category': 99, 'skipped_enabled': False}"])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_get_user_warehouse_id_and_login_cn_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/courier/v1/parcels/$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][0]["pno"]$/detain_warehouse?isFromScanner=false'])
    @pytest.mark.run(order=13)
    def test_test_kit_user_courier_parcels_detain_warehouse_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'detained_marker_category': 15, 'from_scanner': False, 'image_keys': ['parcelManualImport/1596098096-79ece17d5fbd4cb7bdb30ed2f8b2f0b8.jpg'], 'parcel_scan_manual_import_category': 99, 'skipped_enabled': False}"]
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'content-type\': \'application/json; charset=UTF-8\', \'X-FLE-SESSION-ID\': \'$kit_get_user_warehouse_id_and_login_cn_["data"]["sessionid"]$\'}']
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
                
        _address = ['/api/courier/v1/parcels/$kit_user_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][0]["pno"]$/detain_warehouse?isFromScanner=false']
            
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
        
        logging.info("jsonschema文件path:../data/jsonschema/13_kit_user_courier_parcels_detain_warehouse_cn.json")
        with open("../data/jsonschema/13_kit_user_courier_parcels_detain_warehouse_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        