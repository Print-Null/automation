import datetime
import sys,os
from common.readconfig import ReadConfig
from utils.redisbase import RedisBase
sys.path.append(os.getcwd())
import allure
from assertpy import assert_that
import requests
import logging
import time
import pytest
                
logging.basicConfig(level=logging.INFO)


@allure.feature('数据显示已回复->bi普通客服')
class Test_bi_replied(object):
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
        self.keyword1 = self.redisObj.get('courier_write_order_1_0_0_["data"]["parcel_info"]["pno"]')
        self.keyword2 = self.redisObj.get('courier_write_order_2_0_0_["data"]["parcel_info"]["pno"]')
        self.keyword3 = self.redisObj.get('courier_write_order_3_0_0_["data"]["parcel_info"]["pno"]')
        self.keyword4 = self.redisObj.get('courier_write_order_4_0_0_["data"]["parcel_info"]["pno"]')
        self.keyword5 = self.redisObj.get('courier_write_order_5_0_0_["data"]["parcel_info"]["pno"]')
        self.keyword6 = self.redisObj.get('courier_write_order_6_0_0_["data"]["parcel_info"]["pno"]')


    @pytest.mark.run(order=105)
    def test_test_bi_replied(self):
        logging.info("如果运行失败，到bi闪速认定模块，更新下cookie，bi普通客服登入")

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json;charset=UTF-8",
            "X-MS-SESSION-ID": self.cookier
        }
        url = self.host + 'parcelloseapi/taskList?' + self.iframe_0 + '&' + self.iframe_2 + '&' + self.iframe_3 + '&' + self.iframe_1 + '&page=1&pagesize=100&keyword='+self.keyword+'&source=&state=&tab=1&startTime=&endTime=&area=&vip_type=&taskStartTime=' + str(
            int(time.mktime(
                time.strptime(str(datetime.date.today()) + " 01:00:00", "%Y-%m-%d %H:%M:%S")))) + '&taskEndTime=' + str(
            int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)) + " 00:59:59",
                                          "%Y-%m-%d %H:%M:%S")))) + '&handleStartTime=&handleEndTime='

        url1 = self.host + 'parcelloseapi/taskList?' + self.iframe_0 + '&' + self.iframe_2 + '&' + self.iframe_3 + '&' + self.iframe_1 + '&page=1&pagesize=100&keyword='+self.keyword1+'&source=&state=&tab=1&startTime=&endTime=&area=&vip_type=&taskStartTime=' + str(
            int(time.mktime(
                time.strptime(str(datetime.date.today()) + " 01:00:00", "%Y-%m-%d %H:%M:%S")))) + '&taskEndTime=' + str(
            int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)) + " 00:59:59",
                                          "%Y-%m-%d %H:%M:%S")))) + '&handleStartTime=&handleEndTime='

        url2 = self.host + 'parcelloseapi/taskList?' + self.iframe_0 + '&' + self.iframe_2 + '&' + self.iframe_3 + '&' + self.iframe_1 + '&page=1&pagesize=100&keyword='+self.keyword2+'&source=&state=&tab=1&startTime=&endTime=&area=&vip_type=&taskStartTime=' + str(
            int(time.mktime(
                time.strptime(str(datetime.date.today()) + " 01:00:00", "%Y-%m-%d %H:%M:%S")))) + '&taskEndTime=' + str(
            int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)) + " 00:59:59",
                                          "%Y-%m-%d %H:%M:%S")))) + '&handleStartTime=&handleEndTime='

        url3 = self.host + 'parcelloseapi/taskList?' + self.iframe_0 + '&' + self.iframe_2 + '&' + self.iframe_3 + '&' + self.iframe_1 + '&page=1&pagesize=100&keyword='+self.keyword3+'&source=&state=&tab=1&startTime=&endTime=&area=&vip_type=&taskStartTime=' + str(
            int(time.mktime(
                time.strptime(str(datetime.date.today()) + " 01:00:00", "%Y-%m-%d %H:%M:%S")))) + '&taskEndTime=' + str(
            int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)) + " 00:59:59",
                                          "%Y-%m-%d %H:%M:%S")))) + '&handleStartTime=&handleEndTime='

        url4 = self.host + 'parcelloseapi/taskList?' + self.iframe_0 + '&' + self.iframe_2 + '&' + self.iframe_3 + '&' + self.iframe_1 + '&page=1&pagesize=100&keyword='+self.keyword4+'&source=&state=&tab=1&startTime=&endTime=&area=&vip_type=&taskStartTime=' + str(
            int(time.mktime(
                time.strptime(str(datetime.date.today()) + " 01:00:00", "%Y-%m-%d %H:%M:%S")))) + '&taskEndTime=' + str(
            int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)) + " 00:59:59",
                                          "%Y-%m-%d %H:%M:%S")))) + '&handleStartTime=&handleEndTime='

        url5 = self.host + 'parcelloseapi/taskList?' + self.iframe_0 + '&' + self.iframe_2 + '&' + self.iframe_3 + '&' + self.iframe_1 + '&page=1&pagesize=100&keyword='+self.keyword5+'&source=&state=&tab=1&startTime=&endTime=&area=&vip_type=&taskStartTime=' + str(
            int(time.mktime(
                time.strptime(str(datetime.date.today()) + " 01:00:00", "%Y-%m-%d %H:%M:%S")))) + '&taskEndTime=' + str(
            int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)) + " 00:59:59",
                                          "%Y-%m-%d %H:%M:%S")))) + '&handleStartTime=&handleEndTime='
        url6 = self.host + 'parcelloseapi/taskList?' + self.iframe_0 + '&' + self.iframe_2 + '&' + self.iframe_3 + '&' + self.iframe_1 + '&page=1&pagesize=100&keyword='+self.keyword6+'&source=&state=&tab=1&startTime=&endTime=&area=&vip_type=&taskStartTime=' + str(
            int(time.mktime(
                time.strptime(str(datetime.date.today()) + " 01:00:00", "%Y-%m-%d %H:%M:%S")))) + '&taskEndTime=' + str(
            int(time.mktime(time.strptime(str(datetime.date.today() + datetime.timedelta(days=1)) + " 00:59:59",
                                          "%Y-%m-%d %H:%M:%S")))) + '&handleStartTime=&handleEndTime='


        resp = requests.post(url=url, headers=headers, verify=False)
        resp1 = requests.post(url=url1, headers=headers, verify=False)
        resp2 = requests.post(url=url2, headers=headers, verify=False)
        resp3 = requests.post(url=url3, headers=headers, verify=False)
        resp4 = requests.post(url=url4, headers=headers, verify=False)
        resp5 = requests.post(url=url5, headers=headers, verify=False)
        resp6 = requests.post(url=url6, headers=headers, verify=False)



        logging.info("url日志信息:")
        logging.info(url)
        logging.info("请求头是：")
        logging.info(headers)

        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["data"]["row"][-1]["state_str"] == "已工单回复").is_true()
        assert_that(resp.json()["msg"]).is_equal_to("success")
        #########################################################
        logging.info("url日志信息:")
        logging.info(url1)
        logging.info("响应结果日志信息：")
        logging.info(resp1.json())
        assert_that(resp1.status_code).is_equal_to(200)
        assert_that(resp1.json()["code"]).is_equal_to(1)
        assert_that(resp1.json()["data"]["row"][-1]["state_str"] == "已工单回复").is_true()
        assert_that(resp1.json()["msg"]).is_equal_to("success")
        #############################################################
        logging.info("url日志信息:")
        logging.info(url2)
        logging.info("响应结果日志信息：")
        logging.info(resp2.json())
        assert_that(resp2.status_code).is_equal_to(200)
        assert_that(resp2.json()["code"]).is_equal_to(1)
        assert_that(resp2.json()["data"]["row"][-1]["state_str"] == "已工单回复").is_true()
        assert_that(resp2.json()["msg"]).is_equal_to("success")
        #############################################################
        logging.info("url日志信息:")
        logging.info(url3)
        logging.info("响应结果日志信息：")
        logging.info(resp3.json())
        assert_that(resp3.status_code).is_equal_to(200)
        assert_that(resp3.json()["code"]).is_equal_to(1)
        assert_that(resp3.json()["data"]["row"][-1]["state_str"] == "已工单回复").is_true()
        assert_that(resp3.json()["msg"]).is_equal_to("success")
        #############################################################
        logging.info("url日志信息:")
        logging.info(url4)
        logging.info("响应结果日志信息：")
        logging.info(resp4.json())
        assert_that(resp4.status_code).is_equal_to(200)
        assert_that(resp4.json()["code"]).is_equal_to(1)
        assert_that(resp4.json()["data"]["row"][-1]["state_str"] == "已工单回复").is_true()
        assert_that(resp4.json()["msg"]).is_equal_to("success")
        #############################################################
        logging.info("url日志信息:")
        logging.info(url5)
        logging.info("响应结果日志信息：")
        logging.info(resp5.json())
        assert_that(resp5.status_code).is_equal_to(200)
        assert_that(resp5.json()["code"]).is_equal_to(1)
        assert_that(resp5.json()["data"]["row"][-1]["state_str"] == "已工单回复").is_true()
        assert_that(resp5.json()["msg"]).is_equal_to("success")
        #############################################################
        logging.info("url日志信息:")
        logging.info(url6)
        logging.info("响应结果日志信息：")
        logging.info(resp6.json())
        assert_that(resp6.status_code).is_equal_to(200)
        assert_that(resp6.json()["code"]).is_equal_to(1)
        assert_that(resp6.json()["data"]["row"][-1]["state_str"] == "已工单回复").is_true()
        assert_that(resp6.json()["msg"]).is_equal_to("success")
