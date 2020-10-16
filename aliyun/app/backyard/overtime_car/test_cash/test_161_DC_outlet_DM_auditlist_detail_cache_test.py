
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


@allure.feature('DM加班车DM->单条申请详情页')
class Test_DC_outlet_DM_auditlist_detail(object):

    @pytest.mark.parametrize("parameter",['{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][0]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][1]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][2]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][3]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][4]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][5]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][6]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][7]["id"]$\', \'type\': 12, \'isCommit\': 2}'])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-BY-SESSION-ID\': \'$DC_outlet_DM_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'BY-PLATFORM\': \'FB_ANDROID\'}'])
    @pytest.mark.parametrize("address",['api/_/auditlist/detail'])
    @pytest.mark.run(order=161)
    def test_test_DC_outlet_DM_auditlist_detail(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][0]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][1]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][2]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][3]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][4]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][5]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][6]["id"]$\', \'type\': 12, \'isCommit\': 2}', '{\'id\': \'$DC_outlet_DM_auditList_getList_0_0_0_["data"]["dataList"][7]["id"]$\', \'type\': 12, \'isCommit\': 2}']
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-BY-SESSION-ID\': \'$DC_outlet_DM_login_0_0_0_["data"]["sessionid"]$\', \'Accept-Accept\': \'application/json, text/plain, */*\', \'BY-PLATFORM\': \'FB_ANDROID\'}']
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
                
        _address = ['api/_/auditlist/detail']
        
        host = 'backyard_host'
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
        
        RedisBase().set('DC_outlet_DM_auditlist_detail_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["head"]["id"]', resp.json()["data"]["head"]["id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("请求成功!")
        