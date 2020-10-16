#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 16:15
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_06_app_public_tools.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
from utils.redisbase import ReadConfig
import time
import random
@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
class TestAppPublicTools:
    def test_appMenu_index(self, get_data):
        title = "app-菜单"
        logging.info(title)
        url = "{0}/app/menu/index".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == ""
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_appMenu_about(self, get_data):
        title = "app-我的菜单"
        logging.info(title)
        url = "{0}/app/menu/about".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == ""
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_tool_upload_url(self, get_data):
        title = "app-文件上传"
        logging.info(title)
        url = "{0}/app/tool/upload_url".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data={"data":"fileyr{0}.txt".format(str(int(time.time()))),"bucket_name":"file"}
        logging.info(data)
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == ""
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_tool_excel(self, get_data):
        title = "app公共工具-excel"
        logging.info(title)
        url = "{0}/app/tool/excel".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.post(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == ""
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_tool_excelImport(self, get_data):   ##server error File not found
        title = "app公共工具-excel导入"
        logging.info(title)
        url = "{0}/app/tool/excelImport".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.post(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == ""
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())
