#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/31 16:47
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_10_approval_management.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
import time


@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
# web审批管理-设置
class TestApprivalManagement:
    def test_approval_list(self, get_data):  # 'code': -1
        title = "数据查询"
        logging.info(title)
        url = "{0}/web/approval/list".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data = {"page_num": 1,"page_count":20,"serial_no":"","audit_type":1,"state":1,"submitter":"","create_date_start":"","create_date_end":"","finish_date_start":"","finish_date_end":""}
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
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

    def test_approval_getInfo(self, get_data):  # 'code': -1
        title = "下拉列表"
        logging.info(title)
        url = "{0}/web/approval/getInfo".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
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

    @pytest.mark.parametrize("audit_type",[1,2])
    def test_workflow_get(self,audit_type, get_data):
        title = "获取审批配置"
        logging.info(title)
        url = "{0}/web/workflow/get".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data={"audit_type":audit_type}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
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

    def test_workflow_save(self, get_data):  # 'code': -1
        title = "保存审批配置"
        logging.info(title)
        url = "{0}/web/workflow/save".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json"}
        data={"audit_type":1,"workflow_request":""}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
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