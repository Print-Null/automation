
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


@allure.feature('寄件人创建订单任务')
class Test_app_ka_sender_order_create_cn(object):

    @pytest.mark.parametrize("parameter",["{'src_lng': 116.4107459038496, 'skipping_tips': [], 'estimate_total_amount': 2500, 'src_postal_code': '$[config]ka_src_postal_code$', 'src_phone': '$[config]ka_src_phone$', 'src_name': '$[config]ka_src_name$', 'src_province_code': '$[config]ka_src_province_code$', 'src_detail_address': '$[config]ka_src_detail_address$', 'src_district_code': '$[config]ka_src_district_code$', 'src_city_code': '$[config]ka_src_city_code$', 'src_country_code': 'TH', 'ka_warehouse_id': '$[config]ka_warehouse_id$', 'src_lat': 40.03024666518223, 'insured': 0, 'insure_declare_value': 0, 'order_list': [{'height': '$[python]random.randint(1,40)$', 'length': '$[python]random.randint(1,40)$', 'express_category': 1, 'dst_name': '$[config]ka_dst_name$', 'dst_province_code': '$[config]ka_dst_province_code$', 'dst_phone': '$[config]ka_dst_phone$', 'dst_district_code': '$[config]ka_dst_district_code$', 'dst_postal_code': '$[config]ka_dst_postal_code$', 'dst_city_code': '$[config]ka_dst_city_code$', 'dst_detail_address': '$[config]ka_dst_detail_address$', 'dst_country_code': 'TH', 'width': '$[python]random.randint(1,40)$', 'insured': 0, 'cod_amount': 0, 'article_category': '$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$', 'insure_declare_value': 0, 'dst_home_phone': '', 'weight': '$[python]random.randrange(10,15001,10)$', 'cod_enabled': 0, 'request_id': '', 'freight_insure_enabled': False, 'estimate_total_amount': 2500}, {'height': '$[python]random.randint(1,40)$', 'length': '$[python]random.randint(1,40)$', 'express_category': 1, 'dst_name': '$[config]ka_dst_name$', 'dst_province_code': '$[config]ka_dst_province_code$', 'dst_phone': '$[config]ka_dst_phone$', 'dst_district_code': '$[config]ka_dst_district_code$', 'dst_postal_code': '$[config]ka_dst_postal_code$', 'dst_city_code': '$[config]ka_dst_city_code$', 'dst_detail_address': '$[config]ka_dst_detail_address$', 'dst_country_code': 'TH', 'width': '$[python]random.randint(1,40)$', 'insured': 0, 'cod_amount': 0, 'article_category': '$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$', 'insure_declare_value': 0, 'dst_home_phone': '', 'weight': '$[python]random.randrange(10,15001,10)$', 'cod_enabled': 0, 'request_id': '', 'freight_insure_enabled': False, 'estimate_total_amount': 2500}, {'height': '$[python]random.randint(1,40)$', 'length': '$[python]random.randint(1,40)$', 'express_category': 1, 'dst_name': '$[config]ka_dst_name$', 'dst_province_code': '$[config]ka_dst_province_code$', 'dst_phone': '$[config]ka_dst_phone$', 'dst_district_code': '$[config]ka_dst_district_code$', 'dst_postal_code': '$[config]ka_dst_postal_code$', 'dst_city_code': '$[config]ka_dst_city_code$', 'dst_detail_address': '$[config]ka_dst_detail_address$', 'dst_country_code': 'TH', 'width': '$[python]random.randint(1,40)$', 'insured': 0, 'cod_amount': 0, 'article_category': '$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$', 'insure_declare_value': 0, 'dst_home_phone': '', 'weight': '$[python]random.randrange(10,15001,10)$', 'cod_enabled': 0, 'request_id': '', 'freight_insure_enabled': False, 'estimate_total_amount': 2500}], 'remark': 'M+号箱x1,'}"])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_sender_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/orders'])
    @pytest.mark.run(order=315)
    def test_test_app_ka_sender_order_create_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'src_lng': 116.4107459038496, 'skipping_tips': [], 'estimate_total_amount': 2500, 'src_postal_code': '$[config]ka_src_postal_code$', 'src_phone': '$[config]ka_src_phone$', 'src_name': '$[config]ka_src_name$', 'src_province_code': '$[config]ka_src_province_code$', 'src_detail_address': '$[config]ka_src_detail_address$', 'src_district_code': '$[config]ka_src_district_code$', 'src_city_code': '$[config]ka_src_city_code$', 'src_country_code': 'TH', 'ka_warehouse_id': '$[config]ka_warehouse_id$', 'src_lat': 40.03024666518223, 'insured': 0, 'insure_declare_value': 0, 'order_list': [{'height': '$[python]random.randint(1,40)$', 'length': '$[python]random.randint(1,40)$', 'express_category': 1, 'dst_name': '$[config]ka_dst_name$', 'dst_province_code': '$[config]ka_dst_province_code$', 'dst_phone': '$[config]ka_dst_phone$', 'dst_district_code': '$[config]ka_dst_district_code$', 'dst_postal_code': '$[config]ka_dst_postal_code$', 'dst_city_code': '$[config]ka_dst_city_code$', 'dst_detail_address': '$[config]ka_dst_detail_address$', 'dst_country_code': 'TH', 'width': '$[python]random.randint(1,40)$', 'insured': 0, 'cod_amount': 0, 'article_category': '$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$', 'insure_declare_value': 0, 'dst_home_phone': '', 'weight': '$[python]random.randrange(10,15001,10)$', 'cod_enabled': 0, 'request_id': '', 'freight_insure_enabled': False, 'estimate_total_amount': 2500}, {'height': '$[python]random.randint(1,40)$', 'length': '$[python]random.randint(1,40)$', 'express_category': 1, 'dst_name': '$[config]ka_dst_name$', 'dst_province_code': '$[config]ka_dst_province_code$', 'dst_phone': '$[config]ka_dst_phone$', 'dst_district_code': '$[config]ka_dst_district_code$', 'dst_postal_code': '$[config]ka_dst_postal_code$', 'dst_city_code': '$[config]ka_dst_city_code$', 'dst_detail_address': '$[config]ka_dst_detail_address$', 'dst_country_code': 'TH', 'width': '$[python]random.randint(1,40)$', 'insured': 0, 'cod_amount': 0, 'article_category': '$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$', 'insure_declare_value': 0, 'dst_home_phone': '', 'weight': '$[python]random.randrange(10,15001,10)$', 'cod_enabled': 0, 'request_id': '', 'freight_insure_enabled': False, 'estimate_total_amount': 2500}, {'height': '$[python]random.randint(1,40)$', 'length': '$[python]random.randint(1,40)$', 'express_category': 1, 'dst_name': '$[config]ka_dst_name$', 'dst_province_code': '$[config]ka_dst_province_code$', 'dst_phone': '$[config]ka_dst_phone$', 'dst_district_code': '$[config]ka_dst_district_code$', 'dst_postal_code': '$[config]ka_dst_postal_code$', 'dst_city_code': '$[config]ka_dst_city_code$', 'dst_detail_address': '$[config]ka_dst_detail_address$', 'dst_country_code': 'TH', 'width': '$[python]random.randint(1,40)$', 'insured': 0, 'cod_amount': 0, 'article_category': '$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$', 'insure_declare_value': 0, 'dst_home_phone': '', 'weight': '$[python]random.randrange(10,15001,10)$', 'cod_enabled': 0, 'request_id': '', 'freight_insure_enabled': False, 'estimate_total_amount': 2500}], 'remark': 'M+号箱x1,'}"]
        
        _headers = ['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_sender_login_cn_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['/api/ka/v1/orders']
            
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
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/5_app_ka_sender_order_create_cn.json")
        with open("../data/jsonschema/5_app_ka_sender_order_create_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        