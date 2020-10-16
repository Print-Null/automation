
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


@allure.feature('B客户查看我的包裹中我发送的其他的订单')
class Test_app_ka_sender_parcels_parcel_info_list3_cn(object):

    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_sender_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/parcels/parcel_info_list/0/3'])
    @pytest.mark.run(order=328)
    def test_test_app_ka_sender_parcels_parcel_info_list3_cn(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_sender_login_cn_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/ka/v1/parcels/parcel_info_list/0/3']
            
        host = 'app_host'
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
        
        RedisBase().set('app_ka_sender_parcels_parcel_info_list3_cn_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["parcel_info_simples"][0]["pno"]', resp.json()["data"]["parcel_info_simples"][0]["pno"], ex=6000)
        
        RedisBase().set('app_ka_sender_parcels_parcel_info_list3_cn_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["parcel_info_simples"][0]["dst_name"]', resp.json()["data"]["parcel_info_simples"][0]["dst_name"], ex=6000)
        
        RedisBase().set('app_ka_sender_parcels_parcel_info_list3_cn_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["parcel_info_simples"][0]["dst_phone"]', resp.json()["data"]["parcel_info_simples"][0]["dst_phone"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/18_app_ka_sender_parcels_parcel_info_list3_cn.json")
        with open("../data/jsonschema/18_app_ka_sender_parcels_parcel_info_list3_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        