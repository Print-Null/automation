import datetime
import logging
import time

import allure
import pytest
import requests
from assertpy import assert_that

from common.readconfig import ReadConfig
from utils.redisbase import RedisBase

logging.basicConfig(level=logging.INFO)
@allure.feature('bi普通客服->闪速理赔tasklist')
class Test_ShanSuLiPei_Task_List():
    logging.basicConfig(level=logging.INFO)

    def setup(self):
        self.redisObj = RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.cookier = self.redisObj.get("indentifi_bi_usr_PHPSESSID")
        self.host = ReadConfig().get_config(self.runenv_py, "fbi_host_domain")
        self.iframe_0 = self.redisObj.get("test_1_1_iframe_0")
        self.iframe_2 = self.redisObj.get("test_1_1_iframe_2")
        self.iframe_3 = self.redisObj.get("test_1_1_iframe_3")
        self.iframe_1 = self.redisObj.get("test_1_1_iframe_1")
        self.keyword = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')

    @pytest.mark.run(order=386)
    def test_shansulipei_task_list(self):

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": self.cookier
        }

        url = self.host + 'api/parcelclaim/taskList?'+self.iframe_0+'&'+self.iframe_2+'&'+self.iframe_3+'&'+self.iframe_1+'&page=1&pagesize=100&keyword='+self.keyword+'&tab=1&startTime=&endTime=&area=&vip_type=&client_data=&check_data=&taskStartTime=&taskEndTime=&handleStartTime=&handleEndTime='
        resp = requests.post(url=url, headers=headers, verify=False)
        logging.info("url日志信息:")
        logging.info(url)
        logging.info("请求头是：")
        logging.info(headers)

        logging.info("响应结果日志信息：")
        logging.info(resp.json())

        logging.info("获取到的最新的task_id")
        logging.info(resp.json()["data"]["row"][0]["id"])
        RedisBase().set("bi_qery_list_task_id", resp.json()["data"]["row"][0]["id"], ex=6000)

        assert_that(resp.status_code).is_equal_to(200)

        assert_that(resp.json()["code"]).is_equal_to(1)

        if "zh" in headers["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "th" in headers["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "en" in headers["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
