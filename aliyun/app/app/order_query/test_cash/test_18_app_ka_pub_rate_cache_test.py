
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


@allure.feature('B客户查询运费')
class Test_app_ka_pub_rate(object):

    @pytest.mark.parametrize("parameter",['{\'dst_district_name\': \'สมเด็จเจ้าพระยา\', \'src_district_code\': \'TH010101\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'src_district_name\': \'คลองตัน\', \'insure_declare_value\': 0, \'dst_district_code\': \'TH010204\', \'width\': \'$[python]random.randint(1,40)$\', \'length\': \'$[python]random.randint(1,40)$\', \'height\': \'$[python]random.randint(1,40)$\', \'src_province_code\': \'TH01\', \'dst_region_en\': \'Somdet Chao Phraya, Khlong San, Bangkok\', \'dst_country_code\': \'TH\', \'dst_province_name\': \'กรุงเทพ\', \'src_city_code\': \'TH0101\', \'src_province_name\': \'กรุงเทพ\', \'dst_postal_code\': \'10600\', \'src_detail_address\': \'\', \'dst_province_code\': \'TH01\', \'src_postal_code\': \'10110\', \'customer_type_category\': 2, \'src_country_code\': \'TH\', \'dst_city_code\': \'TH0102\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_detail_address\': \'\', \'src_region_en\': \'Khlong Tan, Khlong Toei, Bangkok\', \'src_city_name\': \'คลองเตย\', \'insured\': 0, \'dst_city_name\': \'คลองสาน\', \'client_id\': \'$app_ka_login_0_0_0_["data"]["profile"]["id"]$\'}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/pub/v1/rate'])
    @pytest.mark.run(order=18)
    def test_test_app_ka_pub_rate(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'dst_district_name\': \'สมเด็จเจ้าพระยา\', \'src_district_code\': \'TH010101\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'src_district_name\': \'คลองตัน\', \'insure_declare_value\': 0, \'dst_district_code\': \'TH010204\', \'width\': \'$[python]random.randint(1,40)$\', \'length\': \'$[python]random.randint(1,40)$\', \'height\': \'$[python]random.randint(1,40)$\', \'src_province_code\': \'TH01\', \'dst_region_en\': \'Somdet Chao Phraya, Khlong San, Bangkok\', \'dst_country_code\': \'TH\', \'dst_province_name\': \'กรุงเทพ\', \'src_city_code\': \'TH0101\', \'src_province_name\': \'กรุงเทพ\', \'dst_postal_code\': \'10600\', \'src_detail_address\': \'\', \'dst_province_code\': \'TH01\', \'src_postal_code\': \'10110\', \'customer_type_category\': 2, \'src_country_code\': \'TH\', \'dst_city_code\': \'TH0102\', \'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_detail_address\': \'\', \'src_region_en\': \'Khlong Tan, Khlong Toei, Bangkok\', \'src_city_name\': \'คลองเตย\', \'insured\': 0, \'dst_city_name\': \'คลองสาน\', \'client_id\': \'$app_ka_login_0_0_0_["data"]["profile"]["id"]$\'}']
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['/api/pub/v1/rate']
            
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
        
        logging.info("jsonschema文件path:../data/jsonschema/18_app_ka_pub_rate.json")
        with open("../data/jsonschema/18_app_ka_pub_rate.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        