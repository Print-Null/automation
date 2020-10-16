import sys, os

from common.readconfig import ReadConfig

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")
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


@allure.feature('快递员登入')
class Test_courier_login(object):
    def setup(self):
        self.redisObj = RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.host = ReadConfig().get_config(self.runenv_py, "host")
        self.indentifi_kit_usr = ReadConfig().get_config(self.runenv_py, "indentifi_kit_usr")
        self.indentifi_kit_pwd = ReadConfig().get_config(self.runenv_py, "indentifi_kit_pwd")
        self.login_version = ReadConfig().get_config(self.runenv_py, "login_version")
        self.indentifi_kit_warehouse_usr = ReadConfig().get_config(self.runenv_py, "indentifi_kit_warehouse_usr")
        self.indentifi_kit_warehouse_pwd = ReadConfig().get_config(self.runenv_py, "indentifi_kit_warehouse_pwd")

    @pytest.mark.run(order=89)
    def test_test_courier_login(self):
        url = self.host + "api/courier/v1/auth/new_device_login"
        header = {
            "content-type": "application/json",
            "Accept-Language": "zh-CN"
        }

        data_kuaidi = {
            "login": self.indentifi_kit_usr,
            "password": self.indentifi_kit_pwd,
            "clientid": "8698940239062391583120286987",
            "clientsd": "1583120286995",
            "os": "android",
            "version": self.login_version
        }
        resp = requests.post(url=url, headers=header, json=data_kuaidi)
        logging.info(resp.text)
        logging.info(url)
        logging.info(data_kuaidi)
        logging.info(header)
        # courier_login_0_0_0_["data"]["sessionid"]
        RedisBase().set('courier_login_0_0_0_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        data_kuaidi = {
            "login": self.indentifi_kit_warehouse_usr,
            "password": self.indentifi_kit_warehouse_pwd,
            "clientid": "8698940239062391583120286987",
            "clientsd": "1583120286995",
            "os": "android",
            "version": self.login_version
        }
        resp = requests.post(url=url, headers=header, json=data_kuaidi)
        logging.info(resp.text)
        logging.info(url)
        logging.info(data_kuaidi)
        logging.info(header)
        # warehouse_login_0_0_0_["data"]["sessionid"]
        RedisBase().set('warehouse_login_0_0_0_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)



        # baseTest = BaseTestCase()
        #
        # _parameter = [
        #     "{'login': '$[config]indentifi_kit_usr$', 'password': '$[config]indentifi_kit_pwd$', 'clientid': '8698940239062391583120286987', 'clientsd': '1583120286995', 'os': 'android', 'version': '$[config]login_version$'}"]
        # parameter_new = baseTest.parameter_parser(parameter)
        # address_new = baseTest.parameter_parser(address)
        # if '[int]' in parameter_new:
        #     parameter_new = ast.literal_eval(parameter_new)
        #     for key in parameter_new:
        #         if '[int]' in str(parameter_new[key]):
        #             parameter_new[key] = int(parameter_new[key][5:])
        # else:
        #     parameter_new = ast.literal_eval(parameter_new)
        #
        # _headers = ["{'content-type': 'application/json', 'Accept-Language': 'zh-CN'}"]
        # headers_new = baseTest.parameter_parser(headers)
        # headers_new = ast.literal_eval(headers_new)
        #
        # _address = ['api/courier/v1/auth/new_device_login']
        #
        # host = 'host'
        # host = baseTest.get_host(host)
        # url_data = host + address_new
        # url = baseTest.parameter_parser(url_data)
        # logging.info("url日志信息:")
        # logging.info(url)
        # if "application/json" in str(headers).lower():
        #     resp = requests.post(url=url, json=parameter_new, headers=headers_new, timeout=120, verify=False)
        # else:
        #     resp = requests.post(url=url, data=parameter_new, headers=headers_new, timeout=120, verify=False)
        # logging.info("请求头是：")
        # logging.info(headers_new)
        # logging.info("请求参数日志信息：")
        # logging.info(parameter_new)
        # logging.info("响应结果日志信息：")
        # logging.info(resp.json())
        #
        # RedisBase().set(
        #     'courier_login_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(
        #         _address.index(address)) + '_["data"]["sessionid"]', resp.json()["data"]["sessionid"], ex=6000)
        #
        # assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        #
        # assert_that(resp.status_code).is_equal_to(200)
        #
        # assert_that(resp.json()["code"]).is_equal_to(1)
        #
        # if "zh" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        # elif "th" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        # elif "en" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
