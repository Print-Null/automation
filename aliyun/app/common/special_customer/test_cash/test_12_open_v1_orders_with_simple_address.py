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


@allure.feature('v1_orderWithSimpleAddr')
class Test_open_v1_orders_with_simple_address(object):

    @pytest.mark.parametrize("parameter",['{\'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'mchId\': \'$[config]merchant_id$\', \'mchPno\': \'$[python]str(random.randint(100000000,999999999))$\', \'warehouseNo\': \'\', \'srcName\': \'$[python]"open order simple sender"+str(random.randint(1,99999))$\', \'srcProvinceName\': \'Phranakh\', \'srcDetailAddress\': \'998/15  กะ  Pkhon Si\', \'srcPostalCode\': \'13000\', \'srcPhone\': \'$[python]"0141"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order simple receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0142"+str(random.randint(100000,999999))$\', \'dstProvinceName\': \'นครนายก\', \'dstDetailAddress\': \'998/15    เมืองนครนายก\', \'dstPostalCode\': \'26000\', \'insureDeclareValue\': 0, \'insured\': 0, \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'expressCategory\': 1, \'weight\': \'$[python]random.randint(1,50000)$\', \'remark\': \'อย่าโยน\', \'codEnabled\': 1, \'codAmount\': \'$[python]random.randrange(100,5000001,100)$\', \'dstDistrictName\': \'\'}', '{\'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'mchId\': \'$[config]merchant_id$\', \'mchPno\': \'$[python]str(random.randint(100000000,999999999))$\', \'warehouseNo\': \'\', \'srcName\': \'$[python]"open order simple sender"+str(random.randint(1,99999))$\', \'srcProvinceName\': \'Phranakh\', \'srcDetailAddress\': \'998/15  กะ  Pkhon Si\', \'srcPostalCode\': \'13000\', \'srcPhone\': \'$[python]"0143"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order simple receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0144"+str(random.randint(100000,999999))$\', \'dstProvinceName\': \'นครนายก\', \'dstDetailAddress\': \'998/15    เมืองนครนายก\', \'dstPostalCode\': \'26000\', \'insureDeclareValue\': \'$[python]random.randrange(100,5000001,100)$\', \'insured\': 1, \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'expressCategory\': 1, \'weight\': \'$[python]random.randint(1,50000)$\', \'remark\': \'อย่าโยน\', \'codEnabled\': 0, \'codAmount\': 0}'])
    @pytest.mark.parametrize("headers",["{'content-type': 'application/x-www-form-urlencoded', 'Charset': 'UTF-8', 'Accept-Language': 'ZH-CN'}"])
    @pytest.mark.parametrize("address",['/open/v1/ordersWithSimpleAddr'])
    @pytest.mark.run(order=12)
    def test_test_open_v1_orders_with_simple_address(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'mchId\': \'$[config]merchant_id$\', \'mchPno\': \'$[python]str(random.randint(100000000,999999999))$\', \'warehouseNo\': \'\', \'srcName\': \'$[python]"open order simple sender"+str(random.randint(1,99999))$\', \'srcProvinceName\': \'Phranakh\', \'srcDetailAddress\': \'998/15  กะ  Pkhon Si\', \'srcPostalCode\': \'13000\', \'srcPhone\': \'$[python]"0141"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order simple receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0142"+str(random.randint(100000,999999))$\', \'dstProvinceName\': \'นครนายก\', \'dstDetailAddress\': \'998/15    เมืองนครนายก\', \'dstPostalCode\': \'26000\', \'insureDeclareValue\': 0, \'insured\': 0, \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'expressCategory\': 1, \'weight\': \'$[python]random.randint(1,50000)$\', \'remark\': \'อย่าโยน\', \'codEnabled\': 1, \'codAmount\': \'$[python]random.randrange(100,5000001,100)$\', \'dstDistrictName\': \'\'}', '{\'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'mchId\': \'$[config]merchant_id$\', \'mchPno\': \'$[python]str(random.randint(100000000,999999999))$\', \'warehouseNo\': \'\', \'srcName\': \'$[python]"open order simple sender"+str(random.randint(1,99999))$\', \'srcProvinceName\': \'Phranakh\', \'srcDetailAddress\': \'998/15  กะ  Pkhon Si\', \'srcPostalCode\': \'13000\', \'srcPhone\': \'$[python]"0143"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order simple receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0144"+str(random.randint(100000,999999))$\', \'dstProvinceName\': \'นครนายก\', \'dstDetailAddress\': \'998/15    เมืองนครนายก\', \'dstPostalCode\': \'26000\', \'insureDeclareValue\': \'$[python]random.randrange(100,5000001,100)$\', \'insured\': 1, \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5,6,7,9,10,99])$\', \'expressCategory\': 1, \'weight\': \'$[python]random.randint(1,50000)$\', \'remark\': \'อย่าโยน\', \'codEnabled\': 0, \'codAmount\': 0}']
        
        _headers = ["{'content-type': 'application/x-www-form-urlencoded', 'Charset': 'UTF-8', 'Accept-Language': 'ZH-CN'}"]
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
                
        _address = ['/open/v1/ordersWithSimpleAddr']
            
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