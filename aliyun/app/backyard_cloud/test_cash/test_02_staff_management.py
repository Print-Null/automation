#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 14:55
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_01_web_staff_management.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
from utils.redisbase import ReadConfig
import time
import random

@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
class TestStaffManagement:

    def test_Job_title_create(self, get_data):
        title = "职位创建"
        logging.info(title)
        url = "{0}/web/Job_title/create".format(get_data[1])
        headers = {"Content-Type": "application/json",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        data = {"job_title_name": "yr自动化测试" + str(int(time.time())), "job_title_type": "1",
                "description": "yr自动化测试-职位创建" + str(int(time.time()))}
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("job_title_name", data["job_title_name"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_2_5_3_JobTitle_list(self, get_data):
        title = "职位all"
        logging.info(title)
        url = "{0}/web/Job_title/allList".format(get_data[1])
        headers = {"Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("job_title_id", res.json()["data"][-1]["id"], ex=10800)
            logging.info("新增的职位id是")
            logging.info(res.json()["data"][-1]["id"])
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())


    def test_2_10_Organization_createDepartment(self, get_data):
        title = "部门创建"
        logging.info(title)
        url = "{0}/web/Organization/createDepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"department_name": "yr自动化测试部门创建" + str(int(time.time())), "ancestry_id": RedisBase().get("Organization_departmentList_ancestry_id"),
                "supervisor_id": ""}
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            # 存储新建的部门department_id
            RedisBase().set("department_id", res.json()["data"]["department_id"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    # @pytest.mark.parametrize("state",[1,2,3]) #1在职2离职3待离职
    # @pytest.mark.parametrize("formal",[1,2]) #1正式2非正式
    # @pytest.mark.parametrize("salary_method",[1,2]) #1现金2转账
    # @pytest.mark.parametrize("settlement_type",[1,2]) #1月结2日结，99其他
    def test_5_2_staff_create(self, get_data):
        title = "员工创建"
        logging.info(title)
        url = "{0}/web/staff/create".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {
            "staff_code": str(random.randint(1, 99999999999999999999)),
            "staff_name": "yr自动化测试" + str(int(time.time())),
            "mobile": str(random.randint(0000000000, 9999999999)),
            "mobile_country_code": "86",
            "personal_email": "",
            "job_title_id": RedisBase().get("job_title_id"),
            "department_id": RedisBase().get("department_id"),
            "manager_id": "",
            "state": "1",
            "formal": "1",
            "hire_date": time.strftime('%Y-%m-%d'),
            "leave_date": "",
            "stop_duties_date": "",
            "formal_date": "",
            "salary_method": "1",
            "settlement_type": "1"
        }
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("staff_mobile", data["mobile"], ex=10800)
            RedisBase().set("staff_name", data["staff_name"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_5_1_staff_list(self, get_data):
        title = "员工列表"
        logging.info(title)
        url = "{0}/web/staff/list?page=1&page_size=20&search_name={1}&department_id=&job_title_id=&begin_hire_date=&end_hire_date=&state=&formal=".format(
            get_data[1], RedisBase().get("staff_name"))
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        logging.info(url)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("staff_id", res.json()["data"]["rows"][-1]["staff_id"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())


    def test_5_3_staff_edit(self, get_data):
        title = "员工编辑"
        logging.info(title)
        url = "{0}/web/staff/edit".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        data = {
            "staff_id": RedisBase().get("staff_id"),
            "staff_code": str(random.randint(1, 99999999999999999999)),
            "staff_name": "yr自动化测试" + str(int(time.time())),
            "mobile": str(random.randint(0000000000, 9999999999)),
            "mobile_country_code": "86",
            "personal_email": "123@qq.com",
            "job_title_id": RedisBase().get("job_title_id"),
            "department_id": RedisBase().get("department_id"),
            "manager_id": "",
            "state": "1",
            "formal": "1",
            "hire_date": time.strftime('%Y-%m-%d'),
            "leave_date": "2099-09-09",
            "stop_duties_date": "2099-09-09",
            "formal_date": "2099-09-09",
            "salary_method": "1",
            "settlement_type": "1"
        }
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("staff_name", data["staff_name"], ex=10800)
            RedisBase().set("staff_mobile", data["mobile"], ex=10800)
            RedisBase().set("staff_code", data["staff_code"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())


    def test_5_4_staff_view(self, get_data):  ##未完成
        title = "员工详情"
        logging.info(title)
        url = "{0}/web/staff/view?staff_id={1}".format(get_data[1], RedisBase().get("staff_id"))
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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


    def test_5_4_staff_sysInfo(self, get_data):  ##未完成
        title = "员工基础信息"
        logging.info(title)
        url = "{0}/web/staff/sysInfo".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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


    def test_5_5_staff_searchStaff(self, get_data):
        title = "员工搜索（手机号）"
        logging.info(title)
        url = "{0}/web/staff/searchStaff?search_name={1}&page_size={2}".format(get_data[1],
                                                                               RedisBase().get("staff_mobile"), 10)
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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


    def test_5_5_1_staff_searchStaff(self, get_data):  ##未完成
        title = "员工搜索（姓名）"
        logging.info(title)
        url = "{0}/web/staff/searchStaff?search_name={1}&page_size={2}".format(get_data[1],
                                                                               RedisBase().get("staff_name"), 10)
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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


    def test_5_6_staff_updateStaffDepartment(self, get_data):  ##未完成
        title = "员工批量设置部门信息"
        logging.info(title)
        url = "{0}/web/staff/updateStaffDepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        #data里的staff_ids需要优化一下
        data = {"staff_ids": ["122495a5796f", "0a95837914bb"], "department_id": "1"}
        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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

    def test_staffApp_searchStaff(self, get_data):  ##未完成
        title = "app人员信息-员工搜索（手机号）"
        logging.info(title)
        url = "{0}/app/staff/searchStaff?search_name={1}&page_size={2}".format(get_data[1],
                                                                               RedisBase().get("staff_mobile"), 10)
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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

    def test_staffApp_searchStaff_name(self, get_data):  ##未完成
        title = "app人员信息-搜索（姓名）"
        logging.info(title)
        url = "{0}/app/staff/searchStaff?search_name={1}&page_size={2}".format(get_data[1],
                                                                               RedisBase().get("staff_name"), 10)
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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

    def test_staff_view(self, get_data):
        title = "app人员信息-员工详情"
        logging.info(title)
        url = "{0}/app/staff/view?staff_id={1}".format(get_data[1], RedisBase().get("staff_id"))
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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

    def test_staffApp_info(self, get_data):  #没有id?
        title = "app人员信息-登陆人详情"
        logging.info(title)
        url = "{0}/app/staff/info".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
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

