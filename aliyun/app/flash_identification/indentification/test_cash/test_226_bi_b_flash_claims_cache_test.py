
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


@allure.feature('bi普通客服，闪速理赔')
class Test_bi_b_flash_claims(object):

    @pytest.mark.parametrize("parameter",["{}"])
    @pytest.mark.parametrize("headers",["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_bi_usr_PHPSESSID$'}"])
    @pytest.mark.parametrize("address",['api/parcelclaim/saveNegotiationResult?$test_1_1_iframe_0$&$test_1_1_iframe_2$&$test_1_1_iframe_3$&$test_1_1_iframe_1$&task_id=$bi_qery_list_task_id$&neg_type=1&neg_result[money]=5&neg_result[account_name]=自动化收款人姓名&neg_result[phone]=1111111111&neg_result[bank_name]=1&neg_result[account_no]=1111111111111111&neg_result[parcel_value_attach][0][file_name]=努力.jpg&neg_result[parcel_value_attach][0][object_key]=insureDocShowProduct/1594279266-190acc290fa94305886d015583001578.jpg&neg_result[parcel_value_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/insureDocShowProduct/1594279266-190acc290fa94305886d015583001578.jpg&neg_result[claim_attach][0][file_name]=努力.jpg&neg_result[claim_attach][0][object_key]=insureDocClaimF/1594279271-04827e9732444124b2eff3ebba0ddbd9.jpg&neg_result[claim_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/insureDocClaimF/1594279271-04827e9732444124b2eff3ebba0ddbd9.jpg&neg_result[id_card_attach][0][file_name]=努力.jpg&neg_result[id_card_attach][0][object_key]=problematicItem/1594279254-6e3a7e4d3491442faa78a6a6bc2508ab.jpg&neg_result[id_card_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/problematicItem/1594279254-6e3a7e4d3491442faa78a6a6bc2508ab.jpg&neg_result[bank_account_attach][0][file_name]=努力.jpg&neg_result[bank_account_attach][0][object_key]=problematicItem/1594279261-f66909aa9e9c4f18b49a8a47108119de.jpg&neg_result[bank_account_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/problematicItem/1594279261-f66909aa9e9c4f18b49a8a47108119de.jpg&neg_result[other_attach][0][file_name]=努力.jpg&neg_result[other_attach][0][object_key]=problematicItem/1594279277-a1dc0fb6acce4bf68a32d2417803790b.jpg&neg_result[other_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/problematicItem/1594279277-a1dc0fb6acce4bf68a32d2417803790b.jpg&neg_result[remark]=闪速理赔，协商一致，赔偿&neg_result[to_where]=1'])
    @pytest.mark.run(order=226)
    def test_test_bi_b_flash_claims(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{}"]
        
        _headers = ["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_bi_usr_PHPSESSID$'}"]
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
                
        _address = ['api/parcelclaim/saveNegotiationResult?$test_1_1_iframe_0$&$test_1_1_iframe_2$&$test_1_1_iframe_3$&$test_1_1_iframe_1$&task_id=$bi_qery_list_task_id$&neg_type=1&neg_result[money]=5&neg_result[account_name]=自动化收款人姓名&neg_result[phone]=1111111111&neg_result[bank_name]=1&neg_result[account_no]=1111111111111111&neg_result[parcel_value_attach][0][file_name]=努力.jpg&neg_result[parcel_value_attach][0][object_key]=insureDocShowProduct/1594279266-190acc290fa94305886d015583001578.jpg&neg_result[parcel_value_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/insureDocShowProduct/1594279266-190acc290fa94305886d015583001578.jpg&neg_result[claim_attach][0][file_name]=努力.jpg&neg_result[claim_attach][0][object_key]=insureDocClaimF/1594279271-04827e9732444124b2eff3ebba0ddbd9.jpg&neg_result[claim_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/insureDocClaimF/1594279271-04827e9732444124b2eff3ebba0ddbd9.jpg&neg_result[id_card_attach][0][file_name]=努力.jpg&neg_result[id_card_attach][0][object_key]=problematicItem/1594279254-6e3a7e4d3491442faa78a6a6bc2508ab.jpg&neg_result[id_card_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/problematicItem/1594279254-6e3a7e4d3491442faa78a6a6bc2508ab.jpg&neg_result[bank_account_attach][0][file_name]=努力.jpg&neg_result[bank_account_attach][0][object_key]=problematicItem/1594279261-f66909aa9e9c4f18b49a8a47108119de.jpg&neg_result[bank_account_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/problematicItem/1594279261-f66909aa9e9c4f18b49a8a47108119de.jpg&neg_result[other_attach][0][file_name]=努力.jpg&neg_result[other_attach][0][object_key]=problematicItem/1594279277-a1dc0fb6acce4bf68a32d2417803790b.jpg&neg_result[other_attach][0][object_url]=https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/problematicItem/1594279277-a1dc0fb6acce4bf68a32d2417803790b.jpg&neg_result[remark]=闪速理赔，协商一致，赔偿&neg_result[to_where]=1']
            
        host = 'fbi_host_domain'
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
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        