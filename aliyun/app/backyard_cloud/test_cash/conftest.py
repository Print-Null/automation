#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/15 18:19
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :conftest.py
import pytest
from utils.redisbase import RedisBase
from common.readconfig import ReadConfig
import logging

@pytest.fixture(scope="class")
def get_data():
    redisObj = RedisBase()
    readConfigObj = ReadConfig()
    env = redisObj.get("runenv_py")
    if env == False or env == "trunk":
        env = "trunk"
    elif env == "training":
        env = "training"
    logging.info("当前环境是：{0}".format(env))
    backyard_cloud_host=readConfigObj.get_config(env,'backyard_cloud_host')
    yield (env,backyard_cloud_host)
    # 后置
    logging.info("所有用例执行结束!!")

@pytest.fixture
def get_case_title():
    logging.info("正在运行的用例是:")
    yield
    # 后置
    logging.info("本条用例执行结束!")