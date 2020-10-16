
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
from common.readconfig import ReadConfig

from jsonschema import validate
                
logging.basicConfig(level=logging.INFO)


@allure.feature('获取岛屿的邮政编码')
class Test_kit_v1_address(object):

    @pytest.mark.run(order=39)
    def test_get_Island_postal_code(self):
        print("获取岛屿的邮政编码")
        redisObj = RedisBase()
        readConfigObj = ReadConfig()
        env = redisObj.get("runenv_py")
        if env == False or env == "trunk":
            env = "trunk"
        elif env == "training":
            env = "training"
        print("当前环境是：{0}".format(env))
        # 超级管理员
        super_administrator_login = readConfigObj.get_config(env, "ms_houtai_login_user")
        super_administrator_pwd = readConfigObj.get_config(env, "ms_houtai_login_pwd")
        # 仓管员
        warehouse_keeper_login = readConfigObj.get_config(env, "warehouse_keeper_login")

        # ms-host地址
        ms_host = readConfigObj.get_config(env, "ms_host")
        # 寄件人手机号
        send_phone = readConfigObj.get_config(env, "send_phone")
        # 寄件人姓名
        send_name = readConfigObj.get_config(env, "send_name")
        # 10000登录ms
        url_login = "{0}ms/api/auth/signin".format(ms_host)
        data_login = {"login": "{0}".format(super_administrator_login),"password": "{0}".format(super_administrator_pwd)}
        headers_login = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN"}
        res_login = requests.post(url=url_login, json=data_login, headers=headers_login, verify=False)
        # ms环境下10000登录以后的headers
        headers = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN", "X-MS-SESSION-ID": res_login.json()["data"]["session_id"]}
        #服务区域结果查询
        list_url="{0}ms/api/setting/district?name=&pageSize=20&pageNum=1&upcountry=1&countryCode=&provinceCode=&cityCode=&districtCode=&storeId=&keyWord=".format(ms_host)
        list_res=requests.get(url=list_url,headers=headers,verify=False)
        for i in list_res.json()["data"]["items"]:
            #是岛屿
            if i["island"] == 1:
                #存入redis
                RedisBase().set("island_postal_code",i["postal_code"],ex=6000)
                print("存入postal_code{0}成功".format(i["postal_code"]))
                break