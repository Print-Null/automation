
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


@allure.feature('lazada_confirm')
class Test_callback_lazada_confirm_with_pre_order(object):

    @pytest.mark.parametrize("parameter",['{\'req\': {\'shipment\': {\'app_id\': \'MERCHANT\', \'con_no\': \'$callback_lazada_pre_order_0_0_0_["res"]["shipment"]["con_no"]$\', \'s_email\': \'Jason_Sandra@Mark.com\', \'s_name\': \'$[python]"Automation sender"+str(random.randint(1,99999))$\', \'s_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'r_email\': \'Tammy_Molly@Christopher.com\', \'r_name\': \'$[python]"Automation receiver"+str(random.randint(1,99999))$\', \'r_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'service_code\': \'2D\', \'tot_pkg\': 1, \'ref_no\': \'93d37265-6dd6-a3c9-882d-29ff2018aac2\', \'special_note\': \'12\', \'package\': [{\'p_name\': \'$[python]"item"+str(random.randint(100000000,999999999))$\', \'p_desc\': \'$[python]"regression-"+str(random.randint(100,999))$\', \'quantity\': 1, \'length\': 10000000000000, \'width\': 200000000000, \'height\': 3000000000, \'n_weight\': 4000000000000}], \'location_type\': \'\', \'g_weight\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_amount\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_type\': \'CASH\', \'merchant_id\': \'$[python]str(random.randint(1000,9999999))$\'}}}', '{\'req\': {\'shipment\': {\'app_id\': \'LEX\', \'con_no\': \'$callback_lazada_pre_order_1_0_0_["res"]["shipment"]["con_no"]$\', \'s_email\': \'Jason_Sandra@Mark.com\', \'s_name\': \'$[python]"Automation sender"+str(random.randint(1,99999))$\', \'s_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'r_email\': \'Tammy_Molly@Christopher.com\', \'r_name\': \'$[python]"Automation receiver"+str(random.randint(1,99999))$\', \'r_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'service_code\': \'2D\', \'tot_pkg\': 1, \'ref_no\': \'93d37265-6dd6-a3c9-882d-29ff2018aac2\', \'special_note\': \'12\', \'package\': [{\'p_name\': \'$[python]"item"+str(random.randint(100000000,999999999))$\', \'p_desc\': \'$[python]"regression-"+str(random.randint(100,999))$\', \'quantity\': 1, \'length\': 10000000000000, \'width\': 200000000000, \'height\': 3000000000, \'n_weight\': 4000000000000}], \'location_type\': \'\', \'g_weight\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_amount\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_type\': \'CASH\', \'merchant_id\': \'$[python]str(random.randint(1000,9999999))$\'}}}'])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$'}"])
    @pytest.mark.parametrize("address",['/callback/lazada/confirm'])
    @pytest.mark.run(order=6)
    def test_test_callback_lazada_confirm_with_pre_order(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'req\': {\'shipment\': {\'app_id\': \'MERCHANT\', \'con_no\': \'$callback_lazada_pre_order_0_0_0_["res"]["shipment"]["con_no"]$\', \'s_email\': \'Jason_Sandra@Mark.com\', \'s_name\': \'$[python]"Automation sender"+str(random.randint(1,99999))$\', \'s_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'r_email\': \'Tammy_Molly@Christopher.com\', \'r_name\': \'$[python]"Automation receiver"+str(random.randint(1,99999))$\', \'r_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'service_code\': \'2D\', \'tot_pkg\': 1, \'ref_no\': \'93d37265-6dd6-a3c9-882d-29ff2018aac2\', \'special_note\': \'12\', \'package\': [{\'p_name\': \'$[python]"item"+str(random.randint(100000000,999999999))$\', \'p_desc\': \'$[python]"regression-"+str(random.randint(100,999))$\', \'quantity\': 1, \'length\': 10000000000000, \'width\': 200000000000, \'height\': 3000000000, \'n_weight\': 4000000000000}], \'location_type\': \'\', \'g_weight\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_amount\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_type\': \'CASH\', \'merchant_id\': \'$[python]str(random.randint(1000,9999999))$\'}}}', '{\'req\': {\'shipment\': {\'app_id\': \'LEX\', \'con_no\': \'$callback_lazada_pre_order_1_0_0_["res"]["shipment"]["con_no"]$\', \'s_email\': \'Jason_Sandra@Mark.com\', \'s_name\': \'$[python]"Automation sender"+str(random.randint(1,99999))$\', \'s_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'r_email\': \'Tammy_Molly@Christopher.com\', \'r_name\': \'$[python]"Automation receiver"+str(random.randint(1,99999))$\', \'r_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'service_code\': \'2D\', \'tot_pkg\': 1, \'ref_no\': \'93d37265-6dd6-a3c9-882d-29ff2018aac2\', \'special_note\': \'12\', \'package\': [{\'p_name\': \'$[python]"item"+str(random.randint(100000000,999999999))$\', \'p_desc\': \'$[python]"regression-"+str(random.randint(100,999))$\', \'quantity\': 1, \'length\': 10000000000000, \'width\': 200000000000, \'height\': 3000000000, \'n_weight\': 4000000000000}], \'location_type\': \'\', \'g_weight\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_amount\': \'$[python]round(random.uniform(1,50000),2)$\', \'cod_type\': \'CASH\', \'merchant_id\': \'$[python]str(random.randint(1000,9999999))$\'}}}']
        
        _headers = ["{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$'}"]
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
                
        _address = ['/callback/lazada/confirm']
            
        host = 'common_host'
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
        
        assert_that(resp.json()["res"]["shipment"]["status_code"]).is_equal_to('000')
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        