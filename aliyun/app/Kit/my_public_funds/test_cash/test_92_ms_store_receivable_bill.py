
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


@allure.feature('ms-财务人员登录-快递员回款-1')
class Test_ms_store_receivable_bill(object):

    @pytest.mark.parametrize("parameter",["{}"])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_3_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_3_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_3_2_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/store/receivable_bill?closed=0&staffInfoId=$warehouse_keeper_login$&pageSize=20&pageNum=1&startTime=$kit_my_public_funds_lists_uncleared_#headers#_0_["data"]["items"][0]["business_date_text"]$&endTime=$kit_my_public_funds_lists_uncleared_#headers#_0_["data"]["items"][0]["business_date_text"]$'])
    @pytest.mark.run(order=92)
    def test_test_ms_store_receivable_bill(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{}"]
        
        _headers = ['{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_3_0_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_3_1_0_["data"]["session_id"]$\'}', '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-MS-SESSION-ID\': \'$ms_auth_signin_3_2_0_["data"]["session_id"]$\'}']
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
                
        _address = ['ms/api/store/receivable_bill?closed=0&staffInfoId=$[config]warehouse_keeper_login$&pageSize=20&pageNum=1&startTime=$kit_my_public_funds_lists_uncleared_#headers#_0_["data"]["items"][0]["business_date_text"]$&endTime=$kit_my_public_funds_lists_uncleared_#headers#_0_["data"]["items"][0]["business_date_text"]$']
            
        host = 'ms_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        if "application/json" in str(headers).lower():
            resp = requests.get(url = url, json = parameter_new, headers = headers_new, timeout = 120, verify = False)
        else:
            resp = requests.get(url = url, data = parameter_new, headers = headers_new, timeout = 120, verify = False)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("请求参数日志信息：")
        logging.info(parameter_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())

        # RedisBase().set('ms_store_receivable_bill_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["items"][0]["id"]', resp.json()["data"]["items"][0]["id"], ex=6000)
        RedisBase().set('ms_store_receivable_bill_' + str(_headers.index(headers)) + '_["data"]["items"][0]["id"]', resp.json()["data"]["items"][0]["id"], ex=6000)

        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")

        # logging.info("jsonschema文件path:../data/jsonschema/43_payment_collection_by_courier_1.json")
        # with open("../data/jsonschema/43_payment_collection_by_courier_1.json", "r", encoding="utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance=resp.json(), schema=shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()