import configparser
import logging
import os

import allure
import pytest
import requests

from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase


@allure.feature("生成出车凭证")
class est_Ms_Generate_Vehicle_Voucher():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.SESSION_ID = self.redisObj.get("ms_login_indentification")
        self.da = self.redisObj.get("generate_vehicle_voucher")

    @pytest.mark.run(order=42)
    def est_generate_vehicle_voucher(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/fleet/van/proof"
        header={
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

        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # print(curpath)
        # # session_path = curpath + "/config/vehicle_voucher.ini"
        # # session_path = os.path.join(os.path.abspath(
        # #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        # #     "config/vehicle_voucher.ini")
        #
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/config/vehicle_voucher.ini"
        # cf = configparser.ConfigParser()
        # cf.add_section("vehicle_voucher")
        # cf.set("vehicle_voucher", option="vehicle_voucher_id", value=str(vehicle_voucher_id))
        # with open(session_path, "w") as f:
        #     cf.write(f)
        #
        # return resp
