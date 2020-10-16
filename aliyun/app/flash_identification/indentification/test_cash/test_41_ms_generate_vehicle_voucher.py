import datetime
import json
import logging
import os
import random
import time

import allure
import pytest
import requests
from assertpy import assert_that

from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase



@allure.feature('网点车线任务列表->生成出车凭证')
class Test_Ms_Generate_Vehicle_Voucher_1():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.SESSION_ID = self.redisObj.get("ms_login_indentification")
        # self.SESSION_ID = self.redisObj.get("ms_login_indentification")
        # self.da = self.redisObj.get("generate_vehicle_voucher")

    @pytest.mark.run(order=41)
    def test_generate_vehicle_voucher_1(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        today = datetime.date.today()
        url = host + "ms/api/fleet/van/line/task?type=1&startDate="+str(today)+"&pageNum=1&pageSize=20"
        header={
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"zh-CN",
            "Content-Type":"application/json;charset=UTF-8",
            # "Origin":"http://192.168.0.222",
            # "Referer":"http://192.168.0.222/",
            "X-MS-SESSION-ID":self.SESSION_ID
                    }
        resp = requests.get(url=url, headers=header, verify=False)
        logging.info(resp.json())
        num_i = random.randint(0,10)
        dat = resp.json()["data"]["items"][num_i]
        logging.info("请求参数")
        logging.info(dat)
        logging.info("接口响应结果是：")
        logging.info(dat)
        RedisBase().set("generate_vehicle_voucher", str(dat), ex=6000)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")

        time.sleep(1)
        ##########################
        # comm = Common_data()

        self.da = self.redisObj.get("generate_vehicle_voucher")
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/fleet/van/proof"
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json;charset=UTF-8",
            "X-MS-SESSION-ID": self.SESSION_ID
        }
        null = None
        # data = read_ms_generate_vehicle_voucher("ms_generate_vehicle_voucher_actual.json")
        data = eval(self.da)
        fleet_id = data["fleet_id"]
        van_line_id = data["id"]
        fleet_name = data["fleet_name"]
        driver = data["driver"]
        plate_id = data["plate_id"]
        driver_phone = data["driver_phone"]
        departure_time = data["expect_start_time"]
        data_vehi = {
            "id": null,
            "fleet_id": fleet_id,
            "van_line_id": van_line_id,
            "fleet_name": fleet_name,
            "driver": driver,
            "plate_id": plate_id,
            "driver_phone": driver_phone,
            "departure_time": departure_time
        }
        logging.info("请求data是：")
        logging.info(data_vehi)
        resp = requests.post(url=url, json=data_vehi, headers=header, verify=False)
        logging.info(resp.json())
        logging.info(resp.json()["data"]["id"])
        # vehicle_voucher_id = resp.json()["data"]["id"]
        RedisBase().set("vehicle_voucher_id", str(resp.json()["data"]["id"]), ex=6000)





