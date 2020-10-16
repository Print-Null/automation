import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")

import allure
import requests
import logging
import pytest
import configparser
from utils.redisbase import RedisBase
from common.readconfig import ReadConfig

logging.basicConfig(level=logging.INFO)
cf = configparser.ConfigParser()


@allure.feature('training环境合并网点')
class TestPrepareData(object):

    @pytest.mark.run(order=1)
    def test_prepare_data(self):
        readConfigObj = ReadConfig()
        redisObj = RedisBase()
        env = redisObj.get("runenv_py")
        if env == False:
            env = "trunk"
        print("当前环境是：{0}".format(env))
        if env == "training":
            # 超级管理员
            super_administrator_account = readConfigObj.get_config(env, "ms_houtai_login_user")
            super_administrator_pwd = readConfigObj.get_config(env, "ms_houtai_login_pwd")
            print("超级管理员账号：%s，密码：%s" % (super_administrator_account, super_administrator_pwd))
            ms_host = readConfigObj.get_config(env, "ms_host")
            # 超级管理员登录ms
            url_login = "{0}ms/api/auth/signin".format(ms_host)
            data_login = {"login": "{0}".format(super_administrator_account),
                          "password": "{0}".format(super_administrator_pwd)}
            res_login = requests.post(url=url_login, json=data_login, verify=False)
            headers = {"content-type": "application/json;charset=UTF-8", "Accept-Language": "zh-CN",
                       "X-MS-SESSION-ID": res_login.json()["data"]["session_id"]}
            # 查询寄件人邮编下的网点
            url_query_website = "{0}ms/api/setting/district?name=&pageSize=20&pageNum=1&countryCode=&provinceCode=" \
                                "&cityCode=&districtCode=&storeId=&keyWord=10260".format(ms_host)
            req_query_website = requests.get(url=url_query_website, headers=headers, verify=False)
            store_id = req_query_website.json()["data"]["items"][0]["store_id"]
            print("合并后的网点ID：%s" % store_id)
            # 取出邮编下所有网点的code
            merge_website_code = []
            count = 1
            for i in req_query_website.json()["data"]["items"]:
                print("指定邮编下的第%s个网点信息：%s" % (count, i))
                merge_website_code.append(i["code"])
                count += 1
            # 将所有网点合并成一个网点
            merge_website_data = {
                "opened": True,
                "upcountry": None,
                "codes": merge_website_code,
                "store_id": store_id,
                "delivery_enabled": True,
                "beg_time_text": "08:00",
                "end_time_text": "18:00",
                "given_time_text": 8,
                "date_type": 0,
                "two_sorting_code": "",
                "separation_enabled": False
            }
            url_merge_website = "{0}ms/api/setting/district".format(ms_host)
            requests.post(url=url_merge_website, json=merge_website_data, headers=headers, verify=False)
        else:
            pass
