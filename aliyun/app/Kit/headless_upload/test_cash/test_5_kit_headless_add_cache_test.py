
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


@allure.feature('新增无头件包裹')
class Test_kit_headless_add(object):

    @pytest.mark.parametrize("parameter",['{\'direction_category\': 1, \'direction_store_id\': \'$[config]direction_store_id$\', \'height\': \'$[python]random.randint(1,30)$\', \'length\': \'$[python]random.randint(1,40)$\', \'parcel_describe\': \'$[config]parcel_describe$\', \'parcel_discover_date\': \'$[config]parcel_discover_date$\', \'parcel_headless_category\': 1, \'parcel_image_url\': [\'$kit_headless_upload_photos_0_0_["data"]["object_key"]$\'], \'weight\': \'$[python]random.randint(100,1500)$\', \'width\': \'$[python]random.randint(1,40)$\'}', '{\'direction_category\': 2, \'direction_store_id\': \'$[config]direction_store_id$\', \'height\': \'$[python]random.randint(1,30)$\', \'length\': \'$[python]random.randint(1,40)$\', \'parcel_describe\': \'$[config]parcel_describe$\', \'parcel_discover_date\': \'$[config]parcel_discover_date$\', \'parcel_headless_category\': 1, \'parcel_image_url\': [\'$kit_headless_upload_photos_1_0_["data"]["object_key"]$\'], \'weight\': \'$[python]random.randint(100,1500)$\', \'width\': \'$[python]random.randint(1,40)$\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_2_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/headless/add'])
    @pytest.mark.run(order=5)
    def test_test_kit_headless_add(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'direction_category\': 1, \'direction_store_id\': \'$[config]direction_store_id$\', \'height\': \'$[python]random.randint(1,30)$\', \'length\': \'$[python]random.randint(1,40)$\', \'parcel_describe\': \'$[config]parcel_describe$\', \'parcel_discover_date\': \'$[config]parcel_discover_date$\', \'parcel_headless_category\': 1, \'parcel_image_url\': [\'$kit_headless_upload_photos_0_0_["data"]["object_key"]$\'], \'weight\': \'$[python]random.randint(100,1500)$\', \'width\': \'$[python]random.randint(1,40)$\'}', '{\'direction_category\': 2, \'direction_store_id\': \'$[config]direction_store_id$\', \'height\': \'$[python]random.randint(1,30)$\', \'length\': \'$[python]random.randint(1,40)$\', \'parcel_describe\': \'$[config]parcel_describe$\', \'parcel_discover_date\': \'$[config]parcel_discover_date$\', \'parcel_headless_category\': 1, \'parcel_image_url\': [\'$kit_headless_upload_photos_1_0_["data"]["object_key"]$\'], \'weight\': \'$[python]random.randint(100,1500)$\', \'width\': \'$[python]random.randint(1,40)$\'}']
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_0_2_0_["data"]["sessionid"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/courier/v1/headless/add']
            
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
        
        # logging.info("jsonschema文件path:../data/jsonschema/5_add_headless_packages.json")
        # with open("../data/jsonschema/5_add_headless_packages.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        