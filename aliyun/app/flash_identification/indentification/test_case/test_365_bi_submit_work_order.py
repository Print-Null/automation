
import sys,os

from common.readconfig import ReadConfig

sys.path.append(os.getcwd())
import allure
from assertpy import assert_that
import requests
import logging
import ast
import json
import time
import pytest
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
                
logging.basicConfig(level=logging.INFO)


@allure.feature('bi提交工单->普通客服')
class Test_bi_submit_work_order(object):
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        self.host = ReadConfig().get_config(self.runenv_py, "fbi_host_domain")
        self.cook = self.redisObj.get("indentifi_bi_usr_PHPSESSID")
        self.iframe_0 = self.redisObj.get("test_1_1_iframe_0")
        self.iframe_2 = self.redisObj.get("test_1_1_iframe_2")
        self.iframe_3 = self.redisObj.get("test_1_1_iframe_3")
        self.iframe_1 = self.redisObj.get("test_1_1_iframe_1")
        self.keyword = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')
        self.task_id = self.redisObj.get("bi_qery_list_task_id")
    @pytest.mark.run(order=365)
    def test_test_bi_submit_work_order(self):
        url_te = self.host + "parcelloseapi/workorder?" + self.iframe_0 + "&" + self.iframe_2 + "&" + self.iframe_3 + "&" + self.iframe_1 + "&pno=" + self.keyword + "&task_id=" + self.task_id + "&store_id[0]=TH05020201&store_id[1]=&manger_id[0]=7&manger_id[1]=&order_type=8&workorder_title=自动化测试包裹丢失&workorder_content=自动化测试包裹丢失自动化测试包裹丢失自动化测试包裹丢失&speed_level=1"

        url_tra = self.host + "parcelloseapi/workorder?" + self.iframe_0 + "&" + self.iframe_2 + "&" + self.iframe_3 + "&" + self.iframe_1 + "&pno=" + self.keyword + "&task_id=" + self.task_id + "&store_id[0]=TH01010101&store_id[1]=&manger_id[0]=7&manger_id[1]=&order_type=8&workorder_title=自动化测试包裹丢失&workorder_content=自动化测试包裹丢失自动化测试包裹丢失自动化测试包裹丢失&speed_level=1"
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN",
            "BI-PLATFORM": None,
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": self.cook
        }
        if self.runenv_py == "trunk":
            resp_te = requests.post(url=url_te,headers=header)
            logging.info("请求头是：")
            logging.info(header)
            logging.info("请求参数日志信息：")
            logging.info(url_te)
            logging.info("响应结果日志信息：")
            logging.info(resp_te.json())
            assert_that(resp_te.json()["msg"]).is_equal_to("success")
            assert_that(resp_te.status_code).is_equal_to(200)
            assert_that(resp_te.json()["code"]).is_equal_to(1)

        elif self.runenv_py == "training":
            logging.info("预发布环境")
            resp_te = requests.post(url=url_tra, headers=header,verify=False)
            logging.info("请求头是：")
            logging.info(header)
            logging.info("请求参数日志信息：")
            logging.info(url_te)
            logging.info("响应结果日志信息：")
            logging.info(resp_te.json())
            assert_that(resp_te.json()["msg"]).is_equal_to("success")
            assert_that(resp_te.status_code).is_equal_to(200)
            assert_that(resp_te.json()["code"]).is_equal_to(1)

# http://bi-training.flashexpress.com/parcelloseapi/workorder?ang= zh-CN&auth= 9dff25c3261f7bfcd3ba2b827693ea99&fbid= 32902&time= 1593858190&pno= TH050222PK8A&task_id= SSRD00050724&store_id[0]= TH01010101&store_id[1]= &manger_id[0]= 7&manger_id[1]= &order_type= 8&workorder_title= diushi&workorder_content= diushi&speed_level= 1
# http://sapi-training.flashexpress.com/parcelloseapi/workorder?lang=zh-CN&auth=af97ca37beebfd093ff6c975f8985c22&fbid=32902&time=1593859894&pno=TH050222PM2A&task_id=SSRD00050725&store_id[0]=TH05020201&store_id[1]=&manger_id[0]=7&manger_id[1]=&order_type=8&workorder_title=自动化测试包裹丢失&workorder_content=自动化测试包裹丢失自动化测试包裹丢失自动化测试包裹丢失&speed_level=1
