
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


@allure.feature('查询公司名称')
class Test_query_company_name(object):

    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'en-US\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/fleet'])
    @pytest.mark.run(order=10)
    def test_test_query_company_name(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'en-US\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}', '{\'Accept-Language\': \'th-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_login_10000_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/fleet']
        
        host = 'host_10000'
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
        # 从返回的结果里取有车辆的公司id存入redis
        for item in resp.json()["data"]["items"]:
            if item["van_count"] > 0:
                RedisBase().set('query_company_name_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][1]["id"]', item["id"], ex=6000)
                break
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        # logging.info("jsonschema文件path:../data/jsonschema/10query_company_name.json")
        # with open("../data/jsonschema/10query_company_name.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        