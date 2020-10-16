import configparser
import logging
import os
import allure
import pytest
import requests
from assertpy import assert_that
# from app.kit.Storekeeper.Script.ms_generate_vehicle_voucher import Ms_Generate_Vehicle_Voucher
# from app.kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.kit.Storekeeper.utils.read_ms_generate_vehicle_voucher import read_ms_generate_vehicle_voucher
# from app.kit.Util.common_data import Common_data
from app.Kit.Storekeeper.Script.ms_generate_vehicle_voucher import Ms_Generate_Vehicle_Voucher
# # from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.Kit.Storekeeper.utils.read_ms_generate_vehicle_voucher import read_ms_generate_vehicle_voucher
from app.Kit.Util.common_data import Common_data


@allure.feature("生成出车凭证")
class Test_Ms_Generate_Vehicle_Voucher_by():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ms = Ms_Generate_Vehicle_Voucher()
    @allure.story("生成出车凭证功能")
    @pytest.mark.run(order=79)
    def test_ms_generate_vehicle_voucher_by(self):
        comm = Common_data()
        # host = read_common("ms_host")
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/fleet/van/proof"
        # SESSION_ID = read_ms_session("ms", "ms_session")
        # SESSION_ID = read_all_ini("by_warehouse_man_session","by_warehouse","warehouse_session")
        SESSION_ID = comm.get_parameter_from_redis("warehouse_session")
        header={
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"en-CN",
            "Content-Type":"application/json;charset=UTF-8",
            "X-MS-SESSION-ID":SESSION_ID
                    }
        null = None
        # data = read_ms_generate_vehicle_voucher("ms_generate_vehicle_voucher_actual_by.json")
        data = dict(eval(comm.get_parameter_from_redis("ms_generate_vehicle_voucher_actual_by")))
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
        logging.info("响应结果是：")
        logging.info(resp.json())
        vehicle_voucher_by_id = resp.json()["data"]["id"]
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # print(curpath)
        # session_path = curpath + "/conf/all_data.ini"
        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/all_data.ini")

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/all_data.ini"


        # cf = configparser.ConfigParser()
        # cf.add_section("vehicle_voucher_by")
        # cf.set("vehicle_voucher_by", option="vehicle_voucher_by_id", value=str(vehicle_voucher_by_id))
        # with open(session_path, "w") as f:
        #     cf.write(f)

        comm.write_parameter_to_redis("vehicle_voucher_by_id", vehicle_voucher_by_id)
        logging.info("常规线路生成出车凭证接口响应结果是：")
        logging.info(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")