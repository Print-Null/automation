import hashlib
import sys,os

from common.readconfig import ReadConfig

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


@allure.feature('作废订单')
class Test_open_v1_orders_cancel(object):

    @pytest.mark.parametrize("parameter",['{\'mchId\': \'$[config]merchant_id$\', \'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\'}'])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'ZH-CN', 'content-type': 'application/x-www-form-urlencoded', 'Charset': 'UTF-8'}"])
    @pytest.mark.parametrize("address",['/open/v1/orders/$open_v1_orders_0_0_0_["data"]["pno"]$/cancel'])
    @pytest.mark.run(order=10)
    def test_test_open_v1_orders_cancel(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'mchId\': \'$[config]merchant_id$\', \'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\'}']
        
        _headers = ["{'Accept-Language': 'ZH-CN', 'content-type': 'application/x-www-form-urlencoded', 'Charset': 'UTF-8'}"]
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        parameter_new = self.create_sign(parameter_new)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                
        _address = ['/open/v1/orders/$open_v1_orders_0_0_0_["data"]["pno"]$/cancel']
            
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
        
        assert_that(resp.json()["code"]).is_equal_to(1)

    def create_sign(self, parameter_new: str):
        # 拿到配置文件中对应环境的key
        read_config_object = ReadConfig()
        redis_object = RedisBase()
        env = redis_object.get("runenv_py")
        if env is False:
            env = "trunk"
        else:
            env = redis_object.get("runenv_py")
        key = read_config_object.get_config(env, "key")

        parameter_dict = ast.literal_eval(parameter_new)
        argument_list = []
        for k, v in parameter_dict.items():
            if v != "" and k != "sign":
                argument_list.append(k)
        argument_list.sort()
        sha_string_list = []
        for i in argument_list:
            sha_string_list.append(i)
            sha_string_list.append("=")
            sha_string_list.append(str(parameter_dict[i]))
            sha_string_list.append("&")
        sha_string = "".join(sha_string_list)
        string_sign_temp = sha_string + "key=" + key
        sha256 = hashlib.sha256()
        sha256.update(string_sign_temp.encode("utf-8"))
        sign = sha256.hexdigest().upper()
        parameter_new = parameter_new.replace("sha256", sign)
        return parameter_new