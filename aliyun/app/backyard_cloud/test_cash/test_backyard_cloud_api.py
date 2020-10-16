#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :2020/8/15 17:29
# @Author :lemon_yaoxiaonie
# @Email  :363111505@qq.com
# @File   :backyard_cloud_api.py
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


def get_parameter():
    if RedisBase().exists("country_code"):
        country_code = RedisBase().get("country_code").split(",")
        country_code.remove("")
    else:
        country_code=["CHN","TNA"]
    if RedisBase().exists("industry"):
        industry = RedisBase().get("industry").split(",")
        industry.remove("")
    else:
        industry=[1,2,3,4,5,6]
    if RedisBase().exists("size"):
        size = RedisBase().get("size").split(",")
        size.remove("")
    else:
        size=[1,2,3]
    if RedisBase().exists("transportation_type"):
        transportation_type = RedisBase().get("transportation_type").split(",")
        transportation_type.remove("")
    else:
        transportation_type=[1,2,3,4]
    if RedisBase().exists("transportation"):
        transportation=eval(RedisBase().get("transportation"))
    else:
        transportation={'1': '飞机', '2': '火车', '3': '汽车', '4': '其他'}
    return country_code, industry, size, transportation_type,transportation

company_create_parameter=get_parameter()


@pytest.mark.usefixtures("get_data")
@pytest.mark.usefixtures("get_case_title")
class TestBackyardCloud:
    # 图形验证码
    def test_1_1_sms_captcha(self, get_data):
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
    def test_1_2_sms_send(self, get_data, get_case_title):  ####图形验证码  trunk不校验captcha
        title = "发送短信验证码"
        logging.info(title)
        url = "{0}/auth/sms/send".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"sid": get_case_title[1], "captcha": "666666", "mobile": get_data[2]}
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
            logging.info(res.text)

    # 短信登录
    def test_1_3_sms_login(self, get_data):  ##短信验证码也不校验
        title = "短信登录"
        logging.info(title)
        url = "{0}/auth/sms/login".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"mobile": get_data[2], "verify_code": "666666"}
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
            RedisBase().set("token_type", res.json()["data"]["token_type"]+" ", ex=10800)
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

    def test_company_industries(self, get_data):
        title = "公司行业"
        logging.info(title)
        url = "{0}/web/company/industries".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN","Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            # 把size追加存入redis里
            for key in res.json()["data"].keys():
                RedisBase().append_("industry", key + ",")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_company_size(self, get_data):
        title = "公司规模"
        logging.info(title)
        url = "{0}/web/company/size".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN","Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            # 把size追加存入redis里
            for key in res.json()["data"].keys():
                RedisBase().append_("size", key + ",")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_company_countries(self, get_data):
        title = "国家/地区接口"
        logging.info(title)
        url = "{0}/web/company/countries".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN","Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            logging.info(res.json()["data"].keys())
            #把country_code追加存入redis里
            for key in res.json()["data"].keys():
                RedisBase().append_("country_code",key+",")
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    @pytest.mark.parametrize("country_code", company_create_parameter[0])
    @pytest.mark.parametrize("industry", company_create_parameter[1])
    @pytest.mark.parametrize("size", company_create_parameter[2])
    def test_company_new(self,country_code,industry,size, get_data):
        title = "创建公司"
        logging.info(title)
        url = "{0}/web/company/new".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN","Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
        data = {"name": "yr创建公司" + str(int(time.time())), "country_code": country_code, "industry": industry,
                "size": size, "admin_name": "yr公司管理员", "sa_pwd": "123Abcd", "re_sa_pwd": "123Abcd"}
        res = requests.post(url=url, json=data, headers=headers)
        logging.info(res.status_code)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            # 存储创建公司的cid,name
            RedisBase().set("company_cid", res.json()["data"]["c_id"], ex=10800)
            RedisBase().set("company_name", data["name"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())


    def test_company_signin(self, get_data):  ####图形验证码  trunk不校验captcha
        title = "公司登录"
        logging.info(title)
        url = "{0}/web/company/signin".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN","Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
        # data = {"c_id": RedisBase().get("company_cid"), "pwd": ReadConfig().get_config(get_data[0],"company_admin_pwd")}
        data = {"c_id": "0cfe51385f", "pwd": "123Abcd"}

        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("X-Token",res.json()["data"]["token"],ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(data)
            logging.info(res.json())

    def test_company_info(self, get_data):  #error
        title = "公司信息"
        logging.info(title)
        url = "{0}/web/company/info?c_id={1}".format(get_data[1],RedisBase().get("company_cid"))
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN","Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
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

    @pytest.mark.parametrize("country_code", company_create_parameter[0])
    @pytest.mark.parametrize("industry", company_create_parameter[1])
    @pytest.mark.parametrize("size", company_create_parameter[2])
    def test_company_update(self, country_code,industry,size,get_data):  ####error
        title = "更新公司信息"
        logging.info(title)
        url = "{0}/web/company/update".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN","Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
        data = {"name": RedisBase().get("company_name"), "country_code": country_code, "industry":industry,"size":size,"logo_url":"https://www.baidu.com/img/flexible/logo/pc/index.png"}
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
            logging.info(res.status_code)
            logging.info(res.json())

    def test_sms_send(self, get_data, get_case_title):  ####图形验证码  trunk不校验captcha
        title = "重置管理员密码-发送短信验证码"
        logging.info(title)
        url = "{0}/auth/sms/send".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"sid": get_case_title[1], "captcha": "666666", "mobile": get_data[2]}
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

    def test_company_resetPassword(self, get_data, get_case_title):  #error
        title = "重置管理员密码"
        logging.info(title)
        url = "{0}/web/company/resetPassword".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"c_id": RedisBase().get("company_cid"), "verify_code": "666666", "mobile": get_data[2],"sa_pwd":ReadConfig().get_config(get_data[0],"company_admin_pwd_new"),"re_sa_pwd":ReadConfig().get_config(get_data[0],"company_admin_pwd_new")}
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

    def test_company_transfer(self, get_data, get_case_title):  #error
        title = "更换主管理员"
        logging.info(title)
        url = "{0}/web/company/transfer".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"verify_code": "666666", "mobile": get_data[2]}
        # data = {"verify_code": "666666", "mobile": "0123456789"}
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

    def test_translation_gen(self, get_data):
        title = "更新语言包"
        logging.info(title)
        url = "{0}/admin/translation/gen".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.get(url=url,headers=headers)
        logging.info(res.status_code)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "build ok"
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

    def test_sys_setenv(self, get_data):  #error
        title = "配置设置"
        logging.info(title)
        url = "{0}/admin/sys/setenv".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data={"code":"101","content":"yr测试","remarks":"yr123"}
        res = requests.post(url=url,json=data,headers=headers)
        logging.info(res.status_code)
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

    def test_sys_getenv(self, get_data):  #error
        title = "配置读取"
        logging.info(title)
        url = "{0}/admin/sys/getenv?code={1}".format(get_data[1],101)
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.get(url=url,headers=headers)
        logging.info(res.status_code)
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

    def test_1_3_7_user_info(self, get_data):
        title = "用户信息"
        logging.info(title)
        url = "{0}/auth/user/info".format(get_data[1])
        headers = {"Authorization": RedisBase().get("token_type")+RedisBase().get("access_token"), "Accept-Language": "zh-CN"}
        res = requests.get(url=url, headers=headers)
        logging.info(url)
        logging.info(headers)
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

    def test_1_4_qr_code(self, get_data):
        title = "二维码生成"
        logging.info(title)
        url = "{0}/auth/qr/code".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        res = requests.get(url=url, headers=headers)
        logging.info(url)
        logging.info(headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("tmp", res.json()["data"]["tmp"], ex=10800)
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_1_5_qr_callback(self, get_data):  # state 2 3 已扫描，待确 -code 1
        title = "二维码扫描回调"
        logging.info(title)
        url = "{0}/auth/qr/callback?state={1}&tmp={2}".format(get_data[1], 1, RedisBase().get("tmp"))  # 1，确认登录
        headers = {"Authorization": RedisBase().get("token_type")+RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "确认登录"
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

    def test_1_6_qr_status(self, get_data):
        title = "二维码扫描状态查询"
        logging.info(title)
        url = "{0}/auth/qr/status?tmp={1}".format(get_data[1], RedisBase().get("tmp"))
        res = requests.get(url=url)
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
            logging.info(res.json())

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

    def test_2_2_job_title_list(self, get_data):
        title = "职位列表（分页）"
        logging.info(title)
        url = "{0}/web/job_title/list?page={1}&page_size={2}&$search_name={3}".format(get_data[1], 1, 10,
                                                                                      "yr自动化测试")
        headers = {"Accept-Language": "zh-CN", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
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

    def test_2_5_Job_title_create(self, get_data):
        title = "职位创建"
        logging.info(title)
        url = "{0}/web/Job_title/create".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
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
        headers = {"Accept-Language": "zh-CN", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("id", res.json()["data"][-1]["id"], ex=10800)
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

    def test_2_5_4_Job_title_view(self, get_data, get_case_title):
        title = "职位详情"
        logging.info(title)
        url = "{0}/web/Job_title/view?id={1}".format(get_data[1], get_case_title[0])

        headers = {"Accept-Language": "zh-CN", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
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

    def test_2_6_Job_title_edit(self, get_data, get_case_title):
        title = "职位编辑"
        logging.info(title)
        url = "{0}/web/Job_title/edit".format(get_data[1])
        headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"id": get_case_title[0], "job_title_name": RedisBase().get("job_title_name") + str(int(time.time())),
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
        headers = {"Accept-Language": "zh-CN", "Authorization": RedisBase().get("token_type") + RedisBase().get("access_token")}
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
        headers = {"Accept-Language": "zh-CN", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.post(url=url, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "SUCCESS"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("ancestry_id", res.json()["data"][0]["ancestry_id"], ex=10800)  # 上级部门id
            # RedisBase().set("supervisor_id", res.json()["data"][0]["supervisor_id"], ex=10800)  # 负责人id
        except Exception as e:
            logging.error("断言失败,报错信息是:")
            logging.error(e)
            raise e
        finally:
            logging.info(url)
            logging.info(headers)
            logging.info(res.json())

    def test_5_2_staff_create(self, get_data):  ##未完成
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
            "personal_email": "123@qq.com",
            "job_title_id": "1",
            "department_id": "1",
            "manager_id": "8042feea4edf",
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
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
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

    def test_5_3_staff_edit(self, get_data):  ##未完成
        title = "员工编辑"
        logging.info(title)
        url = "{0}/web/staff/create".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {
            "staff_id": RedisBase().get("staff_id"),
            "staff_code": str(random.randint(1, 99999999999999999999)),
            "staff_name": "yr自动化测试" + str(int(time.time())),
            "mobile": str(random.randint(0000000000, 9999999999)),
            "mobile_country_code": "86",
            "personal_email": "123@qq.com",
            "job_title_id": "1",
            "department_id": "1",
            "manager_id": "8042feea4edf",
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
            logging.info(res.json())

    def test_5_4_staff_view(self, get_data):  ##未完成
        title = "员工详情"
        logging.info(title)
        url = "{0}/web/staff/view?staff_id={1}".format(get_data[1], RedisBase().get("staff_id"))
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

    def test_5_4_staff_sysInfo(self, get_data):  ##未完成
        title = "员工基础信息"
        logging.info(title)
        url = "{0}/web/staff/sysInfo".format(get_data[1])
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

    def test_5_5_staff_searchStaff(self, get_data):  ##未完成
        title = "员工搜索（手机号）"
        logging.info(title)
        url = "{0}/web/staff/searchStaff?search_name={1}&page_size={2}".format(get_data[1],
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

    def test_5_5_1_staff_searchStaff(self, get_data):  ##未完成
        title = "员工搜索（姓名）"
        logging.info(title)
        url = "{0}/web/staff/searchStaff?search_name={1}&page_size={2}".format(get_data[1],
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

    def test_5_6_staff_updateStaffDepartment(self, get_data):  ##未完成
        title = "员工批量设置部门信息"
        logging.info(title)
        url = "{0}/web/staff/updateStaffDepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
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

    def test_2_10_Organization_createDepartment(self, get_data):
        title = "部门创建"
        logging.info(title)
        url = "{0}/web/Organization/createDepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"department_name": "yr自动化测试部门创建" + str(int(time.time())), "ancestry_id": RedisBase().get("ancestry_id"),
                "supervisor_id": RedisBase().get("staff_id")}
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

    def test_2_11_Organization_editDepartment(self, get_data):
        title = "部门编辑"
        logging.info(title)
        url = "{0}/web/Organization/editDepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"department_id": RedisBase().get("department_id"),
                "department_name": "yr自动化测试部门创建" + str(int(time.time())),
                "supervisor_id": RedisBase().get("staff_id")}

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
        data={"data":"file_0824.txt","bucket_name":"file"}
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

    # def test_tool_excelImport(self, get_data):   ##server error File not found
    #     title = "app公共工具-excel导入"
    #     logging.info(title)
    #     url = "{0}/app/tool/excelImport".format(get_data[1])
    #     headers = {"Content-Type": "application/json", "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
    #     res = requests.post(url=url,headers=headers)
    #     try:
    #         assert res.status_code == 200
    #         assert res.json()["code"] == 1
    #         assert res.json()["message"] == ""
    #         logging.info("断言成功,响应结果是:")
    #         logging.info(res.json())
    #     except Exception as e:
    #         logging.error("断言失败,报错信息是:")
    #         logging.error(e)
    #         raise e
    #     finally:
    #         logging.info(url)
    #         logging.info(headers)
    #         logging.info(res.json())



    def test_inviteWeb_checkcode(self, get_data):  #没有id?
        title = "企业邀请码-web端--生成企业邀请码"
        logging.info(title)
        url = "{0}/web/invite/createcode".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
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

    def test_inviteWeb_getcode(self, get_data):  #没有id?
        title = "企业邀请码-web端--获取企业邀请码"
        logging.info(title)
        url = "{0}/web/invite/getcode".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
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

    def test_inviteWeb_switchstate(self, get_data):  #没有id?
        title = "企业邀请码-web端--邀请码激活开关"
        logging.info(title)
        url = "{0}/web/invite/switchstate".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
        res = requests.post(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            #将邀请码存入redis
            RedisBase().set("invite_code",res.json()["data"]["data"]["code"],ex=10800)
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
            RedisBase().set("token_type", res.json()["data"]["token_type"]+" ", ex=10800)
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

    def test_inviteApp_checkcode(self, get_data):  #提示已加入该公司
        title = "企业邀请码-app端--加入企业-邀请码验证"
        logging.info(title)
        url = "{0}/app/invite/checkcode".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data={"code":RedisBase().get("invite_code"),"name":RedisBase().get("staff_name"),"phone":RedisBase().get("staff_mobile"),"is_add":"1"}
        res = requests.post(url=url, json=data,headers=headers)
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

    def test_inviteApp_applyList(self, get_data):  #没有id?
        title = "企业邀请码-app端--邀请码申请记录"
        logging.info(title)
        url = "{0}/app/invite/applylist".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        res = requests.get(url=url,headers=headers)
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

    def test_inviteWeb_applyList(self, get_data):  #没有id?
        title = "web端--待处理列表"
        logging.info(title)
        url = "{0}/web/invite/pendingList".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
        res = requests.get(url=url,headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "ok"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("invite_id",res.json()["data"]["data"][-1]["id"],ex=10800)
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
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
        data={"id":RedisBase().get("invite_id"),"state":"1","department_id":"1","job_title_id":"1","formal_date":"2099-09-09","hire_date":"2020-08-24","staff_code":"76954394893376906625"}
        res = requests.post(url=url,json=data,headers=headers)
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
        url = "{0}/web/invite/searchList?state={1}&operator_id={2}".format(get_data[1],1,"")
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
        res = requests.get(url=url,headers=headers)
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

    def test_get_transportation_type(self, get_data):  ###error
        title = "app出差--交通工具"
        logging.info(title)
        url = "{0}/app/businesstrip/get_transportation_type".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
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
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
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
    def test_businesstrip_addtrip(self,get_data):
        title = "app出差--出差申请"
        logging.info(title)
        url = "{0}/app/businesstrip/addtrip".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
        # data={"audit_reason":"加班理由10到50个字才可以"+str(int(time.time())),"traffic_tools":traffic_tools,"other_traffic_name":other_traffic_name,"oneway_or_roundtrip":oneway_or_roundtrip,"departure_city":"出发地","destination_city":"目的地","start_date":"2020-08-24","end_date":"2020-08-26","days_num":3,"remark":"rmark需要10-500个字才可以"+str(int(time.time())),"image_path":"https://www.baidu.com"}
        data={'audit_reason': '加班理由10到50个字才可以1598274187', 'traffic_tools': '1', 'other_traffic_name': '飞机',
         'oneway_or_roundtrip': 1, 'departure_city': '出发地', 'destination_city': '目的地', 'start_date': '2020-08-20',
         'end_date': '2020-08-21', 'days_num': 1, 'remark': 'rmark需要10-500个字才可以1598274187',
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
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
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
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
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

    def test_resign_get_reason(self,get_data):  #[{'code': 1, 'reason': '个人原因'}, {'code': 3, 'reason': '不适应公司文化'}, {'code': 4, 'reason': '薪酬待遇低'}, {'code': 5, 'reason': '缺少发展空间'}, {'code': 6, 'reason': '与上/下级关系不和'}, {'code': 99, 'reason': '其他'}]
        title = "app离职申请--离职原因"
        logging.info(title)
        url = "{0}/app/resign/get_reason".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
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
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token"),"X-Token":RedisBase().get("X-Token")}
        data={"leave_date":"2020-09-01","work_handover":"","reason":"1","remark":"离职原因备注需在20-500字符之间离职原因备注需在20-500字符之间"+str(int(time.time()))}
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

####******************************************************************************************************************
    def test_4_3_4_msg_cancel(self, get_data):
        title = "Web-消息撤回"
        logging.info(title)
        url = "{0}/web/msg/cancel".format(get_data[1], RedisBase().get("msg_id"))
        headers = {"Content-Type": "application/json"}
        data = {"id": RedisBase().get("msg_id")}
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

    def test_4_2_12_Organization_deldepartment(self, get_data):
        title = "部门删除"
        logging.info(title)
        url = "{0}/web/organization/deldepartment".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
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

    def test_2_7_Job_title_del(self, get_data, get_case_title):
        title = "职位删除"
        logging.info(title)
        url = "{0}/web/Job_title/del".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN",
                   "Authorization": RedisBase().get("token_type")+ RedisBase().get("access_token")}
        data = {"id": get_case_title[0]}
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

if __name__ == '__main__':
    pytest.main()
