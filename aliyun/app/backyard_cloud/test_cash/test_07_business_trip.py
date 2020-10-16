#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 16:19
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_07_business_trip.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
from utils.redisbase import ReadConfig
import datetime
import random
import time
@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
class TestBusinessTrip:
    def test_get_transportation_type(self, get_data):  ###error
        title = "app出差--交通工具"
        logging.info(title)
        url = "{0}/app/businesstrip/get_transportation_type".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"company_signin_X-Token":RedisBase().get("company_signin_X-Token")}
        res = requests.get(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == ""
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            logging.info(res.json()["data"])
            # RedisBase().set("transportation",str(res.json()["data"]),ex=10800)
            # # 把size追加存入redis里
            # for key in res.json()["data"].keys():
            #     RedisBase().append_("transportation_type", key + ",")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_get_singleroundtrip_type(self, get_data):  ###{'1': '单程', '2': '往返'}
        title = "app出差--往返类型"
        logging.info(title)
        url = "{0}/app/businesstrip/get_singleroundtrip_type".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"company_signin_X-Token":RedisBase().get("company_signin_X-Token")}
        res = requests.get(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == ""
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            logging.info(res.json()["data"])
            # RedisBase().set("transportation",str(res.json()["data"]),ex=10800)
            # # 把size追加存入redis里
            # for key in res.json()["data"].keys():
            #     RedisBase().append_("transportation_type", key + ",")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    # @pytest.mark.parametrize("traffic_tools,other_traffic_name", [["1","飞机"],["2","火车"],["3","汽车"],["4","其他"]])
    # @pytest.mark.parametrize("oneway_or_roundtrip",[1,2])
    # @pytest.mark.parametrize("days_num",[1,2,3,4,5,6,7,8,9,10])
    def test_businesstrip_addtrip(self,get_data):  #{'code': 0, 'message': 'ApprovalService server error ', 'data': None}
        title = "app出差--出差申请"
        logging.info(title)
        url = "{0}/app/businesstrip/addtrip".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"company_signin_X-Token":RedisBase().get("company_signin_X-Token")}
        # data={"audit_reason":"加班理由10到50个字才可以"+str(int(time.time())),"traffic_tools":1,"other_traffic_name":"飞机","oneway_or_roundtrip":1,"departure_city":"出发地","destination_city":"目的地","start_date":"2020-08-24","end_date":"2020-08-26","days_num":3,"remark":"rmark需要10-500个字才可以"+str(int(time.time())),"image_path":"https://www.baidu.com"}
        data={'audit_reason': '加班理由10到50个字才可以1598274187', 'traffic_tools': '1', 'other_traffic_name': '飞机',
         'oneway_or_roundtrip': 1, 'departure_city': '出发地', 'destination_city': '目的地', 'start_date': time.strftime('%Y-%m-%d'),
         'end_date': time.strftime('%Y-%m-%d',time.localtime(int(time.time())+86400)), 'days_num': 1, 'remark': 'rmark需要10-500个字才可以1598274187',
         'image_path': 'https://www.baidu.com'}
        logging.info(data)
        res = requests.post(url=url,json=data,headers=headers)
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

    def test_businesstrip_getWorkflow(self,get_data):
        title = "app出差--出差审批流"
        logging.info(title)
        url = "{0}/app/businesstrip/getWorkflow".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"company_signin_X-Token":RedisBase().get("company_signin_X-Token")}
        res = requests.get(url=url,headers=headers)
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

    def test_businesstrip_getDetail(self,get_data):  #staff_audit_business表
        title = "app出差--出差详情"
        logging.info(title)
        url = "{0}/app/businesstrip/getDetail?id={1}".format(get_data[1],50)
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"company_signin_X-Token":RedisBase().get("company_signin_X-Token")}
        res = requests.get(url=url,headers=headers)
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