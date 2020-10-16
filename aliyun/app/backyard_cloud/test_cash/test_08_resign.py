#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 16:52
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_08_resign.py
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
class TestResigin:
    def test_resign_get_reason(self,get_data):  #[{'code': 1, 'reason': '个人原因'}, {'code': 3, 'reason': '不适应公司文化'}, {'code': 4, 'reason': '薪酬待遇低'}, {'code': 5, 'reason': '缺少发展空间'}, {'code': 6, 'reason': '与上/下级关系不和'}, {'code': 99, 'reason': '其他'}]
        title = "app离职申请--离职原因"
        logging.info(title)
        url = "{0}/app/resign/get_reason".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("company_signin_X-Token")}
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

    def test_resign_add_reason(self,get_data):  #[{'code': 1, 'reason': '个人原因'}, {'code': 3, 'reason': '不适应公司文化'}, {'code': 4, 'reason': '薪酬待遇低'}, {'code': 5, 'reason': '缺少发展空间'}, {'code': 6, 'reason': '与上/下级关系不和'}, {'code': 99, 'reason': '其他'}]
        title = "app离职申请--离职申请"
        logging.info(title)
        url = "{0}/app/resign/add_resign".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("company_signin_X-Token")}
        data={"leave_date":time.strftime('%Y-%m-%d'),"work_handover":"49","reason":"1","remark":"离职原因备注需在20-500字符之间离职原因备注需在20-500字符之间"+str(int(time.time()))}
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