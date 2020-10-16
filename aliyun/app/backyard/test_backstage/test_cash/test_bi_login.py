import configparser
import hashlib
import logging
import os
import time

import allure
import pytest
import requests

from app.backyard.test_backstage.util.write_ini import write_ini
from common.base import BaseTestCase
from common.readconfig import ReadConfig
from utils import redisbase
from utils.redisbase import RedisBase

logging.basicConfig(level=logging.INFO)
@allure.feature("申请加班车仓管员登入")
class Test_Bi_Login():
    # md5生成密码
    def setup(self):
        self.redisObj = redisbase.RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.login = ReadConfig().get_config(self.runenv_py, "fbi_login")

        login_pwd = "fbi"+ self.login + str(int(time.time()))
        print(login_pwd)
        self.m = hashlib.md5(login_pwd.encode(encoding='utf-8')).hexdigest()
        print(self.m+str(int(time.time())))
        self.pwd = self.m + str(int(time.time()))
        logging.info("ssssss")
        logging.info(self.pwd)


    @pytest.mark.run(order=1)
    def test_bi_login(self):

        host = ReadConfig().get_config(self.runenv_py, "fbi_host")

        url = host + "v1/login"
        header = {
            "Content-Type": "application/json"
        }
        data = {
            "username": self.login,
            # "password": "abdf9af86b0335c144281a667603c9621591704742"
            "password": self.pwd
        }

        resp = requests.post(url=url,headers=header,json=data,verify=False)
        logging.info(data)
        logging.info("bi登入接口响应结果是：")
        logging.info(resp.json())
        token = resp.json()["body"]["token"]
        # write_ini(filename="bi_login",section="token",option="token",Values=token,mode="w")
        RedisBase().set('bi_login',token, ex=6000)

# {'code': 0, 'msg': '', 'body': {'user_name': 'SuperAdmin', 'user_id': 'SuperAdmin',
#                                 'sys_department_id': None, 'sys_store_id': '-1',
#                                 'token': 'ZDY1YzFlNjUyYmE1NWJjOTYxM2RlN2ZmZjU2NWNhODM=',
#                                 'access': {'fbi.role': ['SUPER_ADMIN', 'SALARY_EDIT', 'EMAIL_EDIT',
#                                                         'WEEK_WORKING_DAY_EDIT', 'JOB_TITLE_LEVEL_GRAD_EDIT'],
#                                            'role': ['NOT.FOUND', 'SUPER_ADMIN'],
#                                            'view_shift': {'sys_department_id': '', 'sys_store_id': ''}}}, 'version': 190404}
# 92f1ff3bbff587d3c33bd70366ef33c7
# f589ff2f83ded218c9d9f70598ec296a1592799035



