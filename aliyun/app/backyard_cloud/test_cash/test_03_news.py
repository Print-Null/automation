#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 15:11
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_03_news.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
from utils.redisbase import ReadConfig
import time
import random
def get_msg_top_data():
    redisObj = RedisBase()
    readConfigObj = ReadConfig()
    env = redisObj.get("runenv_py")
    if env == False or env == "trunk":
        env = "trunk"
    elif env == "training":
        env = "training"
    # 获取消息置顶的测试数据
    msg_top_data = eval(readConfigObj.get_config(env, "msg_top_data"))
    # 获取消息添加的测试数据
    msg_add_success = eval(readConfigObj.get_config(env, "msg_add_success"))
    return msg_top_data, msg_add_success
msg_top_data = get_msg_top_data()[0]
msg_add_success = get_msg_top_data()[1]

@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
class TestNews:
    @pytest.mark.parametrize("item", msg_add_success)
    def test_3_2_msg_list(self, item, get_data):  # 跟员工有关系，先做员工的
        title = "Web-消息添加"
        logging.info(title)
        url = "{0}/web/msg/add".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"name": "yr自动化测试-web标题" + str(int(round(time.time() * 1000))),
                "content": "yr自动化测试-web消息内容" + str(int(time.time())), "type": item["type"], "ids": item["ids"],
                "is_top": "0"}
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("msg_name_{0}".format(item["id"]), data["name"], ex=108000)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_3_2_1_msg_list(self, get_data):
        title = "Web-消息列表"
        logging.info(title)
        url = "{0}/web/msg/list?page={1}&page_size={2}&name={3}".format(get_data[1], 1, 20,
                                                                        RedisBase().get("msg_name_1"))
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("msg_id", res.json()["data"]["items"][0]["id"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_3_3_msg_detail(self, get_data):
        title = "Web-消息详情"
        logging.info(title)
        url = "{0}/web/msg/detail?id={1}".format(get_data[1], RedisBase().get("msg_id"))
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
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

    @pytest.mark.parametrize("item", msg_top_data)
    def test_3_5_msg_top(self, item, get_data):
        logging.info(item)
        title = "Web-消息置顶"
        logging.info(title)
        logging.info("case" + item["id"])
        url = "{0}/web/msg/top".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"id": RedisBase().get("msg_id"), "is_top": item["is_top"]}
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_3_5_msg_export(self, get_data):
        title = "Web-消息导出"
        logging.info(title)
        url = "{0}/web/msg/export?id={1}".format(get_data[1], RedisBase().get("msg_id"))
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
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

    def test_4_1_appMsg_list(self, get_data):
        title = "app-消息列表"
        logging.info(title)
        url = "{0}/app/msg/list?page={1}&page_size={2}&name={3}".format(get_data[1], 1, 20,
                                                                        RedisBase().get("msg_name_1"))
        headers = {"Accept-Language": "zh-CN", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
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

    def test_4_2_appMsg_detail(self, get_data):
        title = "app-消息详情"
        logging.info(title)
        url = "{0}/app/msg/detail?id={1}".format(get_data[1], RedisBase().get("msg_id"))
        headers = {"Accept-Language": "zh-CN", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
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

    def test_4_3_appMsg_un_read_and_audit(self, get_data):
        title = "app-消息未读数量"
        logging.info(title)
        url = "{0}/app/msg/un_read_and_audit".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
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