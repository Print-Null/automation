#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :2020/8/28 19:41
# @Author :lemon_yaoxiaonie
# @Email  :363111505@qq.com
# @File   :test_30_overtime_configuration.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
import time


@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
# 加班模块-加班配置，申请加班
class TestOvertimeConfiguration:
    def test_apply_ot_setting_info(self, get_data):  # 'code': -1
        title = "获取加班配置信息"
        logging.info(title)
        url = "{0}/web/apply/ot_setting_info".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
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

    def test_apply_overtime_types(self, get_data):  # 'code': -1
        title = "获取所有加班类型"
        logging.info(title)
        url = "{0}/web/apply/overtime_types".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == "SUCCESS"
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

    def test_apply_save_ot_setting(self, get_data):
        title = "保存加班类型配置"
        logging.info(title)
        url = "{0}/web/apply/save_ot_setting".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"ot_set": [1, 2]}
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
            logging.info(res.text)
            logging.info(res.json())

    def test_staffauditovertime_getInit(self, get_data):
        title = "加班初始化"
        logging.info(title)
        url = "{0}/app/staffauditovertime/getInit".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
            # 把csrf_token存入到redis里，后面加班申请会用到
            RedisBase().set("csrf_token", res.json()["data"]["csrf_token"], ex=108000)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_staffauditovertime_saveApply(self, get_data):  # 加班类型1=工作日 1.5倍，2=节假日加班 3倍，3节假日正常上班 1倍
        title = "加班申请"
        logging.info(title)
        url = "{0}/app/staffauditovertime/saveApply?ot_date_at={1}&ot_type={2}&ot_start_time={3}&ot_end_time={4}&ot_duration={5}&ot_audit_reason={6}&csrf_token={7}".format(
            get_data[1], time.strftime('%Y-%m-%d'), 3, '01:00', '02:00', 60, "加班原因" + str(int(time.time())),
            RedisBase().get("csrf_token"))
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
            # 存储加班申请的id
            RedisBase().set("overtime_apply_id", res.json()["data"]["data"]["id"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_staffauditovertime_getDetail(self, get_data):  # 500
        title = "加班获取详情"
        logging.info(title)
        # url = "{0}/app/staffauditovertime/getDetail?id={1}".format(get_data[1],RedisBase().get("overtime_apply_id"))
        url = "{0}/app/staffauditovertime/getDetail?id={1}".format(get_data[1],"24")

        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
            # 存储加班申请的id
            RedisBase().set("overtime_apply_id", res.json()["data"]["data"]["id"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_staffauditovertime_getWorkflow(self, get_data):  # 500
        title = "加班审批流"
        logging.info(title)
        url = "{0}/app/staffauditovertime/getWorkflow".format(get_data[1])

        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

#审批
    @pytest.mark.parametrize("audit_show_type",[1,2])
    @pytest.mark.parametrize("audit_state_type",[1,2])
    def test_approval_list(self, audit_show_type,audit_state_type,get_data):  # audit_show_type  1-我的申请 2-我的审批  audit_state_type 1-进行中 2已完成
        title = "app审批-列表"
        logging.info(title)
        url = "{0}/app/approval/list".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data={"audit_show_type":audit_show_type,"audit_state_type":audit_state_type,"page_num":1,"page_count":20}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    @pytest.mark.parametrize("audit_type",[1,2])
    @pytest.mark.parametrize("isApply",[1,2])
    def test_approval_detail(self,audit_type,isApply, get_data):  # 是否是申请 1-我的申请 2-我的审批
        title = "app审批-详情"
        logging.info(title)
        url = "{0}/app/approval/detail".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data={"audit_type":audit_type,"audit_id":1,"isApply":isApply}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    #待我审批的数量-不是我提交申请，待审批的数量
    def test_approval_waitAuditNum(self, get_data):
        title = "app审批-待审核"
        logging.info(title)
        url = "{0}/app/approval/waitAuditNum".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.post(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    @pytest.mark.parametrize("audit_type",[1,2])
    def test_approval_getStream(self, audit_type,get_data):  # 是否是申请 1-我的申请 2-我的审批
        title = "app审批-获取审批详情审批流"
        logging.info(title)
        url = "{0}/app/approval/getStream".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data={"audit_type":audit_type,"audit_id":1}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_approval_reject(self, get_data):  #
        title = "app审批-审批驳回"
        logging.info(title)
        url = "{0}/app/approval/reject".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token"),
                   "Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data={"audit_id":23,"audit_type":1,"reject_reason":"驳回原因111"}
        res = requests.post(url=url, json=data,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"].upper() == ""
            logging.info("断言成功,响应结果是:")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())