
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


@allure.feature('lazada客户下单')
class Test_callback_lazada_order(object):

    @pytest.mark.parametrize("parameter",['{\'req\': {\'shipment\': {\'con_no\': \'$[python]"FLA"+str(random.randint(100000000000,999999999999))$\', \'s_zipcode\': \'13000\', \'s_address\': \'$[python]"lazada automation order adderess"+str(random.randint(100000,9999999))$\', \'s_email\': \'$[python]"lazada_email"+str(random.randint(1,99999))+"@sender.com"$\', \'s_name\': \'$[python]"lazada sender"+str(random.randint(1,99999))$\', \'s_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'s_district\': \' อุทัย/ Uthai\', \'s_province\': \' พระนครศรีอยุธยา/ Phra Nakhon Si Ayutthaya\', \'s_subdistrict\': \'-\', \'r_zipcode\': \'94160\', \'r_address\': \'$[python]"lazada order receiver adderess"+str(random.randint(1000,9999999))$\', \'r_email\': \'$[python]"lazada_email"+str(random.randint(1,99999))+"@receiver.com"$\', \'r_name\': \'$[python]"lazada receiver"+str(random.randint(1,99999))$\', \'r_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'r_district\': \' ยะรัง/ Yarang\', \'r_province\': \' ปัตตานี/ Pattani\', \'r_subdistrict\': \'-\', \'service_code\': \'2D\', \'tot_pkg\': \'$[python]random.randint(1,10000)$\', \'ref_no\': \'fd1d2817-bef2-aa92-0e7af7ad20\', \'special_note\': \'12\', \'package\': [{\'p_name\': \'$[python]"item"+str(random.randint(100000000,999999999))$\', \'p_desc\': \'$[python]"regression-"+str(random.randint(100,999))$\', \'quantity\': 1, \'length\': \'200000000000000.00\', \'width\': \'300000000000.00\', \'height\': \'1000000000000000.00\', \'n_weight\': \'400000000000000.00\'}], \'location_type\': \'\', \'g_weight\': \'$[python]str(round(random.uniform(1,50000),3))$\', \'cod_amount\': \'$[python]str(round(random.uniform(1,50000),3))$\', \'cod_type\': \'CASH\', \'merchant_id\': \'$[python]str(random.randint(1000,9999999))$\'}}}'])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$', 'app_id': 'MERCHANT'}", "{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$', 'app_id': 'LEX'}"])
    @pytest.mark.parametrize("address",['/callback/lazada/order'])
    @pytest.mark.run(order=7)
    def test_test_callback_lazada_order(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'req\': {\'shipment\': {\'con_no\': \'$[python]"FLA"+str(random.randint(100000000000,999999999999))$\', \'s_zipcode\': \'13000\', \'s_address\': \'$[python]"lazada automation order adderess"+str(random.randint(100000,9999999))$\', \'s_email\': \'$[python]"lazada_email"+str(random.randint(1,99999))+"@sender.com"$\', \'s_name\': \'$[python]"lazada sender"+str(random.randint(1,99999))$\', \'s_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'s_district\': \' อุทัย/ Uthai\', \'s_province\': \' พระนครศรีอยุธยา/ Phra Nakhon Si Ayutthaya\', \'s_subdistrict\': \'-\', \'r_zipcode\': \'94160\', \'r_address\': \'$[python]"lazada order receiver adderess"+str(random.randint(1000,9999999))$\', \'r_email\': \'$[python]"lazada_email"+str(random.randint(1,99999))+"@receiver.com"$\', \'r_name\': \'$[python]"lazada receiver"+str(random.randint(1,99999))$\', \'r_mobile1\': \'$[python]"0"+str(random.randint(100000000,999999999))$\', \'r_district\': \' ยะรัง/ Yarang\', \'r_province\': \' ปัตตานี/ Pattani\', \'r_subdistrict\': \'-\', \'service_code\': \'2D\', \'tot_pkg\': \'$[python]random.randint(1,10000)$\', \'ref_no\': \'fd1d2817-bef2-aa92-0e7af7ad20\', \'special_note\': \'12\', \'package\': [{\'p_name\': \'$[python]"item"+str(random.randint(100000000,999999999))$\', \'p_desc\': \'$[python]"regression-"+str(random.randint(100,999))$\', \'quantity\': 1, \'length\': \'200000000000000.00\', \'width\': \'300000000000.00\', \'height\': \'1000000000000000.00\', \'n_weight\': \'400000000000000.00\'}], \'location_type\': \'\', \'g_weight\': \'$[python]str(round(random.uniform(1,50000),3))$\', \'cod_amount\': \'$[python]str(round(random.uniform(1,50000),3))$\', \'cod_type\': \'CASH\', \'merchant_id\': \'$[python]str(random.randint(1000,9999999))$\'}}}']
        
        _headers = ["{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$', 'app_id': 'MERCHANT'}", "{'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'app_key': '$[config]app_key$', 'app_id': 'LEX'}"]
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
                
        _address = ['/callback/lazada/order']
            
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
        
        RedisBase().set('callback_lazada_order_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["res"]["shipment"]["con_no"]', resp.json()["res"]["shipment"]["con_no"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["res"]["shipment"]["status_code"]).is_equal_to('000')
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["res"]["shipment"]["status_desc"]).is_equal_to("Success Requisition")
        