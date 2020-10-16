
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


@allure.feature('B客户在我的包裹中搜索指定的包裹')
class Test_app_ka_parcels_send_to_me_parcel_info_list_search_cn(object):

    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_receiver_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list1_cn_0_0_["data"]["parcel_info_simples"][0]["pno"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list1_cn_0_0_["data"]["parcel_info_simples"][0]["src_name"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list1_cn_0_0_["data"]["parcel_info_simples"][0]["src_phone"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list2_cn_0_0_["data"]["parcel_info_simples"][0]["pno"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list2_cn_0_0_["data"]["parcel_info_simples"][0]["src_name"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list2_cn_0_0_["data"]["parcel_info_simples"][0]["src_phone"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list3_cn_0_0_["data"]["parcel_info_simples"][0]["pno"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list3_cn_0_0_["data"]["parcel_info_simples"][0]["src_name"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list3_cn_0_0_["data"]["parcel_info_simples"][0]["src_phone"]$'])
    @pytest.mark.run(order=342)
    def test_test_app_ka_parcels_send_to_me_parcel_info_list_search_cn(self,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = []
        address_new = baseTest.parameter_parser(address)
        
        _headers = ['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_receiver_login_cn_0_0_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list1_cn_0_0_["data"]["parcel_info_simples"][0]["pno"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list1_cn_0_0_["data"]["parcel_info_simples"][0]["src_name"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list1_cn_0_0_["data"]["parcel_info_simples"][0]["src_phone"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list2_cn_0_0_["data"]["parcel_info_simples"][0]["pno"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list2_cn_0_0_["data"]["parcel_info_simples"][0]["src_name"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list2_cn_0_0_["data"]["parcel_info_simples"][0]["src_phone"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list3_cn_0_0_["data"]["parcel_info_simples"][0]["pno"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list3_cn_0_0_["data"]["parcel_info_simples"][0]["src_name"]$', '/api/ka/v1/parcels/send_to_me_parcel_info_list/search?preciseMatching=$app_ka_parcels_send_to_me_parcel_info_list3_cn_0_0_["data"]["parcel_info_simples"][0]["src_phone"]$']
            
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
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        logging.info("jsonschema文件path:../data/jsonschema/32_app_ka_parcels_send_to_me_parcel_info_list_search_cn.json")
        with open("../data/jsonschema/32_app_ka_parcels_send_to_me_parcel_info_list_search_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        