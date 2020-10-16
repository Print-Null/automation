#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/25 15:56
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_04_company.py
import pytest
import requests
import logging
from utils.redisbase import RedisBase
from utils.redisbase import ReadConfig
import time
import random
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
class TestCompany:
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
            if RedisBase().exists("industry"):
                RedisBase().delete("industry")
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
            logging.info(res.json())
            if RedisBase().exists("size"):
                RedisBase().delete("size")
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
            if RedisBase().exists("country_code"):
                RedisBase().delete("country_code")
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

    # @pytest.mark.parametrize("country_code", company_create_parameter[0])
    # @pytest.mark.parametrize("industry", company_create_parameter[1])
    # @pytest.mark.parametrize("size", company_create_parameter[2])
    @pytest.mark.parametrize("country_code", ["CHN","THA"])
    @pytest.mark.parametrize("industry", [1,2])
    @pytest.mark.parametrize("size", [1,2])
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
        data = {"c_id": RedisBase().get("company_cid"), "pwd": ReadConfig().get_config(get_data[0],"company_admin_pwd")}
        # data = {"c_id": "0cfe51385f", "pwd": "123Abcd"}

        res = requests.post(url=url, json=data, headers=headers)
        try:
            assert res.status_code == 200
            assert res.json()["code"] == 1
            assert res.json()["message"] == "success"
            logging.info("断言成功,响应结果是:")
            logging.info(res.json())
            RedisBase().set("company_signin_X-Token",res.json()["data"]["token"],ex=10800)
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

    # @pytest.mark.parametrize("country_code", company_create_parameter[0])
    # @pytest.mark.parametrize("industry", company_create_parameter[1])
    # @pytest.mark.parametrize("size", company_create_parameter[2])
    @pytest.mark.parametrize("country_code", ["CHN"])
    @pytest.mark.parametrize("industry", [1])
    @pytest.mark.parametrize("size", [1])
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

    def test_sms_send(self, get_data):  ####图形验证码  trunk不校验captcha
        title = "重置管理员密码-发送短信验证码"
        logging.info(title)
        url = "{0}/auth/sms/send".format(get_data[1])
        headers = {"Content-Type": "application/json", "Accept-Language": "zh-CN"}
        data = {"sid": RedisBase().get("sid"), "captcha": "666666", "mobile": get_data[2]}
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

    def test_company_resetPassword(self, get_data):  #error
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

    def test_company_transfer(self, get_data):  #error
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