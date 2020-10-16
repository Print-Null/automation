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


@allure.feature('open_v2下单')
class Test_open_v2_orders(object):

    @pytest.mark.parametrize("parameter",['{\'mchId\': \'$[config]merchant_id$\', \'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'outTradeNo\': \'$[python]str(random.randint(1000000000,9999999999999999999999999))$\', \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5])$\', \'codAmount\': \'$[python]random.randrange(100,5000001,100)$\', \'codEnabled\': 1, \'dstCityName\': \'พระนครศรีอยุธยา\', \'dstDetailAddress\': \'กะ123มัง\', \'dstHomePhone\': \'$[python]"0136"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0135"+str(random.randint(100000,999999))$\', \'dstPostalCode\': \'13000\', \'dstProvinceName\': \'พระนครศรีอยุธยา\', \'expressCategory\': 1, \'insureDeclareValue\': \'$[python]random.randrange(100,5000001,100)$\', \'insured\': 1, \'remark\': \'-\', \'srcCityName\': \'บางคอแหลม\', \'srcDetailAddress\': \'88 หมู่ 8 อาคารหลวงไทยทาวเวอร์ ชั้น 3 ถนนพุทธมณฑลสา\', \'srcName\': \'$[python]"open order sender"+str(random.randint(1,99999))$\', \'srcPhone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'srcPostalCode\': \'10120\', \'srcProvinceName\': \'กรุงเทพ\', \'weight\': \'$[python]random.randint(1,30000)$\'}', '{\'mchId\': \'$[config]merchant_id$\', \'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'outTradeNo\': \'$[python]str(random.randint(1000000000,9999999999999999999999999))$\', \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5])$\', \'codAmount\': 0, \'codEnabled\': 0, \'dstCityName\': \'พระนครศรีอยุธยา\', \'dstDetailAddress\': \'กะ123มัง\', \'dstHomePhone\': \'$[python]"0136"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0135"+str(random.randint(100000,999999))$\', \'dstPostalCode\': \'13000\', \'dstProvinceName\': \'พระนครศรีอยุธยา\', \'expressCategory\': 1, \'insureDeclareValue\': 0, \'insured\': 0, \'remark\': \'-\', \'srcCityName\': \'บางคอแหลม\', \'srcDetailAddress\': \'88 หมู่ 8 อาคารหลวงไทยทาวเวอร์ ชั้น 3 ถนนพุทธมณฑลสา\', \'srcName\': \'$[python]"open order sender"+str(random.randint(1,99999))$\', \'srcPhone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'srcPostalCode\': \'10120\', \'srcProvinceName\': \'กรุงเทพ\', \'weight\': \'$[python]random.randint(1,30000)$\'}'])
    @pytest.mark.parametrize("headers",["{'Accept-Language': 'ZH-CN', 'content-type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive', 'Charset': 'UTF-8'}"])
    @pytest.mark.parametrize("address",['/open/v2/orders'])
    @pytest.mark.run(order=17)
    def test_test_open_v2_orders(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ['{\'mchId\': \'$[config]merchant_id$\', \'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'outTradeNo\': \'$[python]str(random.randint(1000000000,9999999999999999999999999))$\', \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5])$\', \'codAmount\': \'$[python]random.randrange(100,5000001,100)$\', \'codEnabled\': 1, \'dstCityName\': \'พระนครศรีอยุธยา\', \'dstDetailAddress\': \'กะ123มัง\', \'dstHomePhone\': \'$[python]"0136"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0135"+str(random.randint(100000,999999))$\', \'dstPostalCode\': \'13000\', \'dstProvinceName\': \'พระนครศรีอยุธยา\', \'expressCategory\': 1, \'insureDeclareValue\': \'$[python]random.randrange(100,5000001,100)$\', \'insured\': 1, \'remark\': \'-\', \'srcCityName\': \'บางคอแหลม\', \'srcDetailAddress\': \'88 หมู่ 8 อาคารหลวงไทยทาวเวอร์ ชั้น 3 ถนนพุทธมณฑลสา\', \'srcName\': \'$[python]"open order sender"+str(random.randint(1,99999))$\', \'srcPhone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'srcPostalCode\': \'10120\', \'srcProvinceName\': \'กรุงเทพ\', \'weight\': \'$[python]random.randint(1,30000)$\'}', '{\'mchId\': \'$[config]merchant_id$\', \'nonceStr\': \'$[python]str(int(time.mktime(time.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))))$\', \'sign\': \'sha256\', \'outTradeNo\': \'$[python]str(random.randint(1000000000,9999999999999999999999999))$\', \'articleCategory\': \'$[python]random.choice([0,1,2,3,4,5])$\', \'codAmount\': 0, \'codEnabled\': 0, \'dstCityName\': \'พระนครศรีอยุธยา\', \'dstDetailAddress\': \'กะ123มัง\', \'dstHomePhone\': \'$[python]"0136"+str(random.randint(100000,999999))$\', \'dstName\': \'$[python]"open order receiver"+str(random.randint(1,99999))$\', \'dstPhone\': \'$[python]"0135"+str(random.randint(100000,999999))$\', \'dstPostalCode\': \'13000\', \'dstProvinceName\': \'พระนครศรีอยุธยา\', \'expressCategory\': 1, \'insureDeclareValue\': 0, \'insured\': 0, \'remark\': \'-\', \'srcCityName\': \'บางคอแหลม\', \'srcDetailAddress\': \'88 หมู่ 8 อาคารหลวงไทยทาวเวอร์ ชั้น 3 ถนนพุทธมณฑลสา\', \'srcName\': \'$[python]"open order sender"+str(random.randint(1,99999))$\', \'srcPhone\': \'$[python]"0134"+str(random.randint(100000,999999))$\', \'srcPostalCode\': \'10120\', \'srcProvinceName\': \'กรุงเทพ\', \'weight\': \'$[python]random.randint(1,30000)$\'}']
        
        _headers = ["{'Accept-Language': 'ZH-CN', 'content-type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive', 'Charset': 'UTF-8'}"]
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
                
        _address = ['/open/v2/orders']
            
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
        
        RedisBase().set('open_v2_orders_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["pno"]', resp.json()["data"]["pno"], ex=6000)
        
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