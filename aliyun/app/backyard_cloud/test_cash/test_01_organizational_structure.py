#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 11:28
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_01_organizational_structure.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
import time

@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
class TestOrganizationalStructure:
    def test_2_1_Organization_info(self, get_data):
        title = "组织信息"
        logging.info(title)
        url = "{0}/web/Organization/info".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
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

    def test_Organization_commonDeptList(self, get_data):
        title = "web组织架构-通用部门列表（通用插件使用）"
        logging.info(title)
        url = "{0}/web/Organization/commonDeptList?department_id={1}".format(get_data[1], 1)
        headers = {"Accept-Language": "zh-CN",
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

    def test_Organization_ommonSearchDeptStaff(self, get_data):
        title = "web组织架构-人员查询（通用插件使用）"
        logging.info(title)
        url = "{0}/web/Organization/commonSearchDeptStaff?search_name={1}".format(get_data[1], "")
        headers = {"Accept-Language": "zh-CN",
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

    def test_2_2_job_title_list(self, get_data):
        title = "职位列表（分页）"
        logging.info(title)
        url = "{0}/web/job_title/list?page={1}&page_size={2}&$search_name={3}".format(get_data[1], 1, 10,
                                                                                      "")
        headers = {"Accept-Language": "zh-CN",
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

    # @pytest.mark.parametrize("job_title_type",[1,2,3,4,5,6,7,8,9,10,11,12])  # 1. 财务 2. 出纳 3. 销售 4. 客服 5. 质检 6. 产品 7. 研发 8. 行政 9. 设计 10. 产品 11. 管理 12. 其他
    def test_2_5_Job_title_create(self, get_data):
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

    def test_2_5_4_Job_title_view(self, get_data):
        title = "职位详情"
        logging.info(title)
        url = "{0}/web/Job_title/view?id={1}".format(get_data[1], RedisBase().get("job_title_id"))

        headers = {"Accept-Language": "zh-CN",
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

    def test_2_6_Job_title_edit(self, get_data):
        title = "职位编辑"
        logging.info(title)
        url = "{0}/web/Job_title/edit".format(get_data[1])
        headers = {"Content-Type": "application/json",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        data = {"id": RedisBase().get("job_title_id"), "job_title_name": RedisBase().get("job_title_name") + str(int(time.time())),
                "job_title_type": 1, "description": "yr自动化测试-职位创建" + str(int(time.time()))}

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
            logging.info(data)
            logging.info(res.json())

    def test_2_8_job_title_jobTitleType(self, get_data):
        title = "职位类别枚举"
        logging.info(title)
        url = "{0}/web/job_title/jobTitleType".format(get_data[1])
        headers = {"Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.post(url=url, headers=headers)
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

    def test_2_9_Organization_departmentList(self, get_data):
        title = "部门列表"
        logging.info(title)
        url = "{0}/web/Organization/departmentList?department_id=1".format(get_data[1])
        headers = {"Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            #存储最新的部门id存储到redis里作为新建部门的上级部门id
            RedisBase().set("Organization_departmentList_ancestry_id", res.json()["data"][-1]["department_id"], ex=10800)  # 上级部门id
            # RedisBase().set("supervisor_id", res.json()["data"][0]["supervisor_id"], ex=10800)  # 负责人id
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
                "supervisor_id": ""}  #RedisBase().get("Organization_departmentList_staff_id")
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

    def test_2_11_Organization_editDepartment(self, get_data):  #{'code': 0, 'message': 'dept_6', 'data': []}
        title = "部门编辑"
        logging.info(title)
        url = "{0}/web/Organization/editDepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"department_id": RedisBase().get("department_id"),
                "department_name": "yr自动化测试部门创建" + str(int(time.time())),
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

    def test_Organization_info(self, get_data):  ##未完成
        title = "app组织架构-组织信息"
        logging.info(title)
        url = "{0}/app/Organization/info".format(get_data[1])
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

    def test_Organization_getDepartmentList(self, get_data):  ##department_id，部门id
        title = "app组织架构-部门列表"
        logging.info(title)
        # url = "{0}/app/Organization/getDepartmentList?department_id={1}".format(get_data[1],"145")
        url = "{0}/app/Organization/getDepartmentList?department_id={1}".format(get_data[1],RedisBase().get("department_id"))
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

    def test_2_7_Job_title_del(self, get_data):
        title = "职位删除"
        logging.info(title)
        url = "{0}/web/Job_title/del".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        data = {"id": RedisBase().get("job_title_id")}
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
            logging.info(data)
            logging.info(res.json())

    def test_4_2_12_Organization_deldepartment(self, get_data):
        title = "部门删除"
        logging.info(title)
        url = "{0}/web/organization/deldepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
        data = {"department_id": RedisBase().get("department_id")}
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
            logging.info(data)
            logging.info(res.json())