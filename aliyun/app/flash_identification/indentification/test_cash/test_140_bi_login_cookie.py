import sys,os
sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0]+"/flash")
import logging

import allure
import pytest
import requests

from common.readconfig import ReadConfig
from utils.redisbase import RedisBase

logging.basicConfig(level=logging.INFO)
@allure.feature('bi闪速认定获取iframe信息')
class Test_Bi_Login_cookie():
    logging.basicConfig(level=logging.INFO)

    def setup(self):
        self.redisObj = RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        # 网点经理
        self.indentifi_manager_usr = ReadConfig().get_config(self.runenv_py, "indentifi_manager_usr")
        self.indentifi_manager_pwd = ReadConfig().get_config(self.runenv_py, "indentifi_manager_pwd")
        # bi普通客服登入
        self.indentifi_bi_usr = ReadConfig().get_config(self.runenv_py, "indentifi_bi_usr")
        self.indentifi_bi_pwd = ReadConfig().get_config(self.runenv_py, "indentifi_bi_pwd")
        self.host = ReadConfig().get_config(self.runenv_py, "fbi_host_domain")

    @pytest.mark.run(order=140)
    def test_bi_login_cookie(self):
        url = self.host + "loginuser/login"
        #网点经理
        data = {
            "py_test": "1",
            "account": self.indentifi_manager_usr,
            "pwd": self.indentifi_manager_pwd
        }
        resp = requests.post(url=url, data=data)
        logging.info(url)
        logging.info("网点经理登入")
        logging.info(resp.text)
        logging.info(resp.cookies)
        RedisBase().set('indentifi_manager_PHPSESSID', "ga=GA1.2.1105378886.1568691037; lang=zh-CN; _gid=GA1.2.1093029504.1593312587; PHPSESSID=" + resp.json()["data"]["PHPSESSID"] + "; _gat_gtag_UA_145656102_1=1", ex=6000)
        # bi普通客服登入
        data_pu = {
            "py_test": "1",
            "account": self.indentifi_bi_usr,
            "pwd": self.indentifi_bi_pwd
        }
        resp_pu = requests.post(url=url, data=data_pu)
        logging.info("bi普通客服登入")
        logging.info(resp_pu.text)
        logging.info(resp_pu.cookies)
        RedisBase().set('indentifi_bi_usr_PHPSESSID', "lang=zh-CN; _ga=GA1.2.165987491.1592987659; _gid=GA1.2.1533605421.1593590743; PHPSESSID=" + resp_pu.json()["data"]["PHPSESSID"] + "; _gat_gtag_UA_145656102_1=1", ex=6000)



