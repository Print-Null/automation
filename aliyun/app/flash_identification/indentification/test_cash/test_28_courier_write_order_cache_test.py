
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


@allure.feature('快递员填单')
class Test_courier_write_order(object):

    @pytest.mark.parametrize("parameter",["{'article_category': 99, 'call_duration': 0, 'client_id': 'CA0546', 'cod_amount': 0, 'cod_enabled': False, 'customer_type_category': 2, 'dst_city_code': 'TH0502', 'dst_country_code': 'TH', 'dst_detail_address': '2', 'dst_district_code': 'TH050201', 'dst_name': '2', 'dst_phone': '1346999281', 'dst_postal_code': '13130', 'dst_province_code': 'TH05', 'express_category': 1, 'freight_insure_enabled': False, 'height': 1, 'insure_declare_value': 0, 'insured': False, 'length': 1, 'settlement_category': 1, 'skipping_tips': [], 'src_city_code': 'TH1101', 'src_country_code': 'TH', 'src_detail_address': '1', 'src_district_code': 'TH110101', 'src_name': '1', 'src_phone': '1232311232', 'src_postal_code': '26000', 'src_province_code': 'TH11', 'total_amount': 4000, 'weight': 2000, 'width': 1}"])
    @pytest.mark.parametrize("headers",['{\'X-FLE-SESSION-ID\': \'$courier_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Language\': \'zh-CN\', \'By-Platform\': \'RB_KIT\', \'X-DEVICE-ID\': \'8673510346528821571665712622\', \'Content-Type\': \'application/json\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/ticket/pickups/parcel'])
    @pytest.mark.run(order=28)
    def test_test_courier_write_order(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'article_category': 99, 'call_duration': 0, 'client_id': 'CA0546', 'cod_amount': 0, 'cod_enabled': False, 'customer_type_category': 2, 'dst_city_code': 'TH0502', 'dst_country_code': 'TH', 'dst_detail_address': '2', 'dst_district_code': 'TH050201', 'dst_name': '2', 'dst_phone': '1346999281', 'dst_postal_code': '13130', 'dst_province_code': 'TH05', 'express_category': 1, 'freight_insure_enabled': False, 'height': 1, 'insure_declare_value': 0, 'insured': False, 'length': 1, 'settlement_category': 1, 'skipping_tips': [], 'src_city_code': 'TH1101', 'src_country_code': 'TH', 'src_detail_address': '1', 'src_district_code': 'TH110101', 'src_name': '1', 'src_phone': '1232311232', 'src_postal_code': '26000', 'src_province_code': 'TH11', 'total_amount': 4000, 'weight': 2000, 'width': 1}"]
        
        _headers = ['{\'X-FLE-SESSION-ID\': \'$courier_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Language\': \'zh-CN\', \'By-Platform\': \'RB_KIT\', \'X-DEVICE-ID\': \'8673510346528821571665712622\', \'Content-Type\': \'application/json\'}']
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
                
        _address = ['api/courier/v1/ticket/pickups/parcel']
            
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
        
        RedisBase().set('courier_write_order_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["parcel_info"]["pno"]', resp.json()["data"]["parcel_info"]["pno"], ex=6000)
        
        RedisBase().set('courier_write_order_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["ticket_pickup_id"]', resp.json()["data"]["ticket_pickup_id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        