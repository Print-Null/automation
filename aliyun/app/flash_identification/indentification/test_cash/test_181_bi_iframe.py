import sys,os
sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0]+"/flash")
import re
import sys, os
sys.path.append(os.getcwd())
from common.readconfig import ReadConfig
from utils.redisbase import RedisBase
import allure
from assertpy import assert_that
import requests
import logging
import pytest

logging.basicConfig(level=logging.INFO)


@allure.feature('bi闪速认定获取iframe信息')
class Test_Get_Html(object):
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.cookier = self.redisObj.get("indentifi_bi_usr_PHPSESSID")
        print(self.cookier)
        self.host = ReadConfig().get_config(self.runenv_py, "fbi_host_domain")
    @pytest.mark.run(order=181)
    def test_get_html(self):
        logging.info("如果运行失败，到bi闪速认定模块，更新下cookie,bi普通客服登入")
        url = self.host + "cs/ssjudge"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN",
            "BI-PLATFORM": "",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": self.cookier,
        }
        '''
        Cookie  这里面的PHPSESSID 从哪里来的？
        '''
        response = requests.get(url=url, headers=headers, verify=False)
        s = response.text.encode("utf-8")
        logging.info("响应结果是：")
        logging.info(s)
        logging.info("headers")
        logging.info(headers)
        html_utf8 = str(s, encoding="utf-8")
        var_list = re.findall('<iframe[^>]+src="([^"]+)"', html_utf8)
        uu = str(var_list).split("?")[1]
        url_data = uu.split("'")[0]
        lang = url_data.split("&")
        assert_that(lang[0]).is_not_none()
        assert_that(lang[1]).is_not_none()
        assert_that(lang[2]).is_not_none()
        assert_that(lang[3]).is_not_none()

        RedisBase().set('test_1_1_iframe_0', lang[0], ex=6000)
        RedisBase().set('test_1_1_iframe_1', lang[1], ex=6000)
        RedisBase().set('test_1_1_iframe_2', lang[2], ex=6000)
        RedisBase().set('test_1_1_iframe_3', lang[3], ex=6000)

