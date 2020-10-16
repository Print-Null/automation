#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 16:09
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_05_enterprise_invitation_code.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
from utils.redisbase import ReadConfig
import time
import random
@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
class TestEnterpriseInvitationCode:
    def test_inviteWeb_checkcode(self, get_data):  #没有id?
        title = "企业邀请码-web端--生成企业邀请码"
        logging.info(title)
        url = "{0}/web/invite/createcode".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("company_signin_X-Token")}
        res = requests.post(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
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

    def test_inviteWeb_getcode(self, get_data):  # 没有id?
        title = "企业邀请码-web端--获取企业邀请码"
        logging.info(title)
        url = "{0}/web/invite/getcode".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "X-Token": RedisBase().get("company_signin_X-Token")}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
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

    def test_inviteWeb_switchstate(self, get_data):  # 没有id?
        title = "企业邀请码-web端--邀请码激活开关"
        logging.info(title)
        url = "{0}/web/invite/switchstate".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "X-Token": RedisBase().get("company_signin_X-Token")}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            # 将邀请码存入redis
            RedisBase().set("invite_code", res.json()["data"]["data"]["code"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    ###先用新建的员工登录，再去做邀请码验证
    # 图形验证码
    def test_sms_captcha(self, get_data):
        title = "图形验证码"
        logging.info(title)
        url = "{0}/auth/sms/captcha".format(get_data[1])
        headers = {"Accept-Language": "zh-CN"}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("sid", res.json()["data"]["sid"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    # 发送短信验证码 - 正例
    def test_sms_send(self, get_data, get_case_title):  ####图形验证码  trunk不校验captcha
        title = "发送短信验证码"
        logging.info(title)
        url = "{0}/auth/sms/send".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"sid": RedisBase().get("sid"), "captcha": "666666", "mobile": RedisBase().get("staff_mobile")}
        res = requests.post(url=url, json=data, headers=headers)
        logging.info(res.status_code)
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

    # 短信登录
    def test_sms_login(self, get_data):  ##短信验证码也不校验
        title = "短信登录"
        logging.info(title)
        url = "{0}/auth/sms/login".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"mobile": RedisBase().get("staff_mobile"), "verify_code": "666666"}
        res = requests.post(url=url, json=data, headers=headers)
        logging.info(url)
        logging.info(headers)
        logging.info(data)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("token_type", res.json()["data"]["token_type"] + " ", ex=10800)
            RedisBase().set("access_token", res.json()["data"]["access_token"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_inviteApp_checkcode(self, get_data):  # 提示已加入该公司
        title = "企业邀请码-app端--加入企业-邀请码验证"
        logging.info(title)
        url = "{0}/app/invite/checkcode".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        data = {"code": RedisBase().get("invite_code"), "name": RedisBase().get("staff_name"),
                "phone": RedisBase().get("staff_mobile"), "is_add": "1"}
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
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

    def test_inviteApp_applyList(self, get_data):  # 没有id?
        title = "企业邀请码-app端--邀请码申请记录"
        logging.info(title)
        url = "{0}/app/invite/applylist".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
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

    def test_inviteWeb_applyList(self, get_data):  # 没有id?
        title = "web端--待处理列表"
        logging.info(title)
        url = "{0}/web/invite/pendingList".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "X-Token": RedisBase().get("company_signin_X-Token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("invite_id", res.json()["data"]["data"][-1]["id"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_inviteWeb_approval(self, get_data):  ###error
        title = "web端--邀请码审批"
        logging.info(title)
        url = "{0}/web/invite/approval".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "X-Token": RedisBase().get("company_signin_X-Token")}
        data = {"id": RedisBase().get("invite_id"), "state": "1", "department_id": "1", "job_title_id": "1",
                "formal_date": "2099-09-09", "hire_date": "2020-08-24", "staff_code": "76954394893376906625"}
        res = requests.post(url=url, json=data, headers=headers)
        logging.info(data)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
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

    def test_inviteWeb_searchList(self, get_data):  ###error
        title = "web端--审批历史记录列表"
        logging.info(title)
        url = "{0}/web/invite/searchList?state={1}&operator_id={2}".format(get_data[1], 1, "")
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "X-Token": RedisBase().get("company_signin_X-Token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
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