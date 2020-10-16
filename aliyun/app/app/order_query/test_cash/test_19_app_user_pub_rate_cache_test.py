
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


@allure.feature('C客户查询运费')
class Test_app_user_pub_rate(object):

    @pytest.mark.parametrize("parameter",['{\'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_city_code\': \'TH2501\', \'src_city_name\': \'เมืองลพบุรี\', \'src_detail_address\': \'\', \'src_postal_code\': \'15000\', \'src_district_name\': \'ทะเลชุบศร\', \'src_province_name\': \'ลพบุรี\', \'dst_country_code\': \'TH\', \'dst_detail_address\': \'\', \'dst_province_code\': \'TH25\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'dst_province_name\': \'ปราจีนบุรี\', \'client_id\': \'$app_user_login_0_0_0_["data"]["profile"]["id"]$\', \'src_district_code\': \'TH070101\', \'dst_region_en\': \'Na Mueang, Mueang Prachinburi, Prachin Buri\', \'dst_postal_code\': \'25000\', \'width\': \'$[python]random.randint(1,40)$\', \'insured\': 0, \'customer_type_category\': 1, \'dst_city_name\': \'เมืองปราจีนบุรี\', \'length\': \'$[python]random.randint(1,40)$\', \'height\': \'$[python]random.randint(1,40)$\', \'dst_district_code\': \'TH250101\', \'src_country_code\': \'TH\', \'dst_district_name\': \'หน้าเมือง\', \'src_province_code\': \'TH07\', \'src_region_en\': \'Thale Chup Son, Mueang Lopburi, Lopburi\', \'src_city_code\': \'TH0701\', \'insure_declare_value\': 0}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/pub/v1/rate'])
    @pytest.mark.run(order=19)
    def test_test_app_user_pub_rate(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'weight\': \'$[python]random.randrange(10,15001,10)$\', \'dst_city_code\': \'TH2501\', \'src_city_name\': \'เมืองลพบุรี\', \'src_detail_address\': \'\', \'src_postal_code\': \'15000\', \'src_district_name\': \'ทะเลชุบศร\', \'src_province_name\': \'ลพบุรี\', \'dst_country_code\': \'TH\', \'dst_detail_address\': \'\', \'dst_province_code\': \'TH25\', \'article_category\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'dst_province_name\': \'ปราจีนบุรี\', \'client_id\': \'$app_user_login_0_0_0_["data"]["profile"]["id"]$\', \'src_district_code\': \'TH070101\', \'dst_region_en\': \'Na Mueang, Mueang Prachinburi, Prachin Buri\', \'dst_postal_code\': \'25000\', \'width\': \'$[python]random.randint(1,40)$\', \'insured\': 0, \'customer_type_category\': 1, \'dst_city_name\': \'เมืองปราจีนบุรี\', \'length\': \'$[python]random.randint(1,40)$\', \'height\': \'$[python]random.randint(1,40)$\', \'dst_district_code\': \'TH250101\', \'src_country_code\': \'TH\', \'dst_district_name\': \'หน้าเมือง\', \'src_province_code\': \'TH07\', \'src_region_en\': \'Thale Chup Son, Mueang Lopburi, Lopburi\', \'src_city_code\': \'TH0701\', \'insure_declare_value\': 0}']
        
        _headers = ['{\'Accept-Language\': \'zh-Hans-CN\', \'content-type\': \'application/json\', \'X-FLE-SESSION-ID\': \'$app_user_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'en-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}', '{\'Accept-Language\': \'th-CN\', \'content-type\': \'application/json\', \'X-KA-SESSION-ID\': \'$app_ka_login_0_0_0_["data"]["sessionid"]$\'}']
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
        
        logging.info("jsonschema文件path:../data/jsonschema/19_app_user_pub_rate.json")
        with open("../data/jsonschema/19_app_user_pub_rate.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        