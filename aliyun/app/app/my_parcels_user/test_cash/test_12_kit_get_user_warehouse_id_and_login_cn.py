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


@allure.feature('获取仓管员ID并登录kit')
class Test_kit_get_user_warehouse_id_and_login_cn(object):

    @pytest.mark.run(order=12)
    def test_test_kit_get_user_warehouse_id_and_login_cn(self):
        readConfigObj = ReadConfig()
        redisObj = RedisBase()
        env = redisObj.get("runenv_py")
        if env is False:
            env = "trunk"
        print("当前环境是：{0}".format(env))
        if env == "trunk":
            # 超级管理员
            ms_account_trunk = readConfigObj.get_config(env, "ms_houtai_login_user")
            ms_password_trunk = readConfigObj.get_config(env, "ms_houtai_login_pwd")
            print("超级管理员账号：%s，密码：%s" % (ms_account_trunk, ms_password_trunk))
            src_postal_code_trunk = readConfigObj.get_config(env, "user_src_postal_code")
            print("寄件人邮编：%s" % src_postal_code_trunk)
            ms_host_trunk = readConfigObj.get_config(env, "ms_host")
            # 超级管理员登录ms
            ms_login_url_trunk = "{0}ms/api/auth/signin".format(ms_host_trunk)
            ms_login_parameter_trunk = {"login": "{0}".format(ms_account_trunk),
                                        "password": "{0}".format(ms_password_trunk)}
            res_login_trunk = requests.post(url=ms_login_url_trunk, json=ms_login_parameter_trunk, verify=False)
            ms_headers_trunk = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                                "X-MS-SESSION-ID": res_login_trunk.json()["data"]["session_id"]}
            # 查询寄件人邮编下的网点
            url_query_website_trunk = "{0}ms/api/setting/district?name=&pageSize=20&pageNum=1&countryCode=&" \
                                      "provinceCode=&cityCode=&districtCode=&storeId=&keyWord=" \
                                      "{1}".format(ms_host_trunk, src_postal_code_trunk)
            req_query_website_trunk = requests.get(url=url_query_website_trunk, headers=ms_headers_trunk, verify=False)
            store_id_trunk = req_query_website_trunk.json()["data"]["items"][0]["store_id"]
            print("寄件人邮编下第一个网点ID：%s" % store_id_trunk)
            # 根据网点ID查询网点下仓管员的ID
            url_get_warehouse_trunk = "{0}ms/api/setting/store/staffs?state=1&positionCategory=2&pageSize=20&pageNum" \
                                      "=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=&" \
                                      "organizationId={1}".format(ms_host_trunk, store_id_trunk)
            req_get_warehouse_trunk = requests.get(url=url_get_warehouse_trunk, headers=ms_headers_trunk, verify=False)
            warehouse_id_trunk = req_get_warehouse_trunk.json()["data"]["items"][0]["id"]
            print("仓管员id：%s" % warehouse_id_trunk)
            # 得到仓管员id后登录kit
            url_kit_login_trunk = "http://192.168.0.228:8080/api/courier/v1/auth/new_device_login"
            header_kit_login_trunk = {"Accept-Language": "zh-CN",
                                      "content-type": "application/json; charset=UTF-8"}
            parameter_kit_login_trunk = {
                "login": "{}".format(warehouse_id_trunk),
                "password": "123456",
                "clientid": "8627020338716801594109392016",
                "clientsd": "1594109392016",
                "os": "android",
                "version": "3.2.5"
            }
            req_kit_login_trunk = requests.post(url=url_kit_login_trunk, headers=header_kit_login_trunk,
                                                json=parameter_kit_login_trunk, verify=False)
            kit_sessionid_trunk = req_kit_login_trunk.json()["data"]["sessionid"]
            print("仓管员登录返回的sessionid：%s" % kit_sessionid_trunk)
            RedisBase().set('kit_get_user_warehouse_id_and_login_cn_["data"]["sessionid"]', kit_sessionid_trunk, ex=6000)
        if env == "training":
            # 超级管理员
            ms_account_training = readConfigObj.get_config(env, "ms_houtai_login_user")
            ms_password_training = readConfigObj.get_config(env, "ms_houtai_login_pwd")
            print("超级管理员账号：%s，密码：%s" % (ms_account_training, ms_password_training))
            src_postal_code_training = readConfigObj.get_config(env, "user_src_postal_code")
            print("寄件人邮编：%s" % src_postal_code_training)
            ms_host_training = readConfigObj.get_config(env, "ms_host")
            # 超级管理员登录ms
            ms_login_url_training = "{0}ms/api/auth/signin".format(ms_host_training)
            ms_login_parameter_training = {"login": "{0}".format(ms_account_training),
                                           "password": "{0}".format(ms_password_training)}
            res_login_training = requests.post(url=ms_login_url_training, json=ms_login_parameter_training,
                                               verify=False)
            ms_headers_training = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                                   "X-MS-SESSION-ID": res_login_training.json()["data"]["session_id"]}
            # 查询寄件人邮编下的网点
            url_query_website_training = "{0}ms/api/setting/district?name=&pageSize=20&pageNum=1&countryCode=&" \
                                         "provinceCode=&cityCode=&districtCode=&storeId=&keyWord=" \
                                         "{1}".format(ms_host_training, src_postal_code_training)
            req_query_website_training = requests.get(url=url_query_website_training, headers=ms_headers_training,
                                                      verify=False)
            store_id_training = req_query_website_training.json()["data"]["items"][0]["store_id"]
            print("寄件人邮编下第一个网点ID：%s" % store_id_training)
            # 根据网点ID查询网点下仓管员的ID
            url_get_warehouse_training = "{0}ms/api/setting/store/staffs?state=1&positionCategory=2&pageSize=20&pageNum" \
                                         "=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&formal=&" \
                                         "organizationId={1}".format(ms_host_training, store_id_training)
            req_get_warehouse_training = requests.get(url=url_get_warehouse_training, headers=ms_headers_training,
                                                      verify=False)
            warehouse_id_training = req_get_warehouse_training.json()["data"]["items"][0]["id"]
            print("仓管员id：%s" % warehouse_id_training)
            # 得到仓管员id后登录kit
            url_kit_login_training = "https://sapi-training.flashexpress.com/api/courier/v1/auth/new_device_login"
            header_kit_login_training = {"Accept-Language": "zh-CN",
                                         "content-type": "application/json; charset=UTF-8"}
            parameter_kit_login_training = {
                "login": "{}".format(warehouse_id_training),
                "password": "666666",
                "clientid": "8627020338716801569484010323",
                "clientsd": "1569484010332",
                "os": "android",
                "version": "3.1.5"
            }
            req_kit_login_training = requests.post(url=url_kit_login_training, headers=header_kit_login_training,
                                                   json=parameter_kit_login_training, verify=False)
            kit_sessionid_training = req_kit_login_training.json()["data"]["sessionid"]
            print("仓管员登录返回的sessionid：%s" % kit_sessionid_training)
            RedisBase().set('kit_get_user_warehouse_id_and_login_cn_["data"]["sessionid"]', kit_sessionid_training, ex=6000)
