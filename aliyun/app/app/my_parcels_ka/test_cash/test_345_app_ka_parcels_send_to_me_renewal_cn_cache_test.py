
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


@allure.feature('B客户在寄给我的并且选择运送中的包裹点击改约派送时间')
class Test_app_ka_parcels_send_to_me_renewal_cn(object):

    @pytest.mark.parametrize("parameter",['{\'remark\': \'$[python]random.choice(["家里没人","有事外出","电话关机","电话没信号","需要雇人搬运","约定时间无法到达","货物太重"])$\', \'delivery_date\': \'$[python]str(datetime.date.today()+datetime.timedelta(days=1))$\'}'])
    @pytest.mark.parametrize("headers",['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_receiver_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['/api/ka/v1/parcels/renewal/$kit_ka_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][2]["pno"]$'])
    @pytest.mark.run(order=345)
    def test_test_app_ka_parcels_send_to_me_renewal_cn(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'remark\': \'$[python]random.choice(["家里没人","有事外出","电话关机","电话没信号","需要雇人搬运","约定时间无法到达","货物太重"])$\', \'delivery_date\': \'$[python]str(datetime.date.today()+datetime.timedelta(days=1))$\'}']
        
        _headers = ['{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_receiver_login_cn_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['/api/ka/v1/parcels/renewal/$kit_ka_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][2]["pno"]$']
            
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
        
        logging.info("jsonschema文件path:../data/jsonschema/35_app_ka_parcels_send_to_me_renewal_cn.json")
        with open("../data/jsonschema/35_app_ka_parcels_send_to_me_renewal_cn.json", "r", encoding = "utf-8") as f:
            shcema = json.load(f)
            res = validate(instance = resp.json(), schema = shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
        