import configparser
import os
from datetime import datetime
import random
# from app.kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.kit.Util.common_data import Common_data
import allure
from assertpy import assert_that
import requests
import logging

import pytest

# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
from app.Kit.Util.common_data import Common_data

logging.basicConfig(level=logging.INFO)


@allure.feature('加班车申请（中控审批界面）->审批通过')
class Test_backyard_overtime_car_ms_api_fleet_line_approve_pass():

    @pytest.mark.run(order=74)
    def test_test_backyard_overtime_car_ms_api_fleet_line_approve_pass(self):
        null = None
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        # line_approve_id = read_all_ini("all_data", "line_approve_id", "line_approve_id")
        line_approve_id = comm.get_parameter_from_redis("line_approve_id")
        url = host + 'ms/api/fleet/line/approve/' + str(line_approve_id) + '/pass'
        # SESSION_ID = read_all_ini("by_warehouse_man_session", "ms_session", "ms_session")
        SESSION_ID = comm.get_parameter_from_redis("ms_session")
        headers = {
            "Accept-Language": "zh-CN",
            "Accept": "application/json, text/plain, */*",
            "X-MS-SESSION-ID": SESSION_ID
        }
        # start_store = read_all_ini("all_data", "store_id_start", "store_id")
        start_store = comm.get_parameter_from_redis("store_id_start")
        # end_store = read_all_ini("all_data", "store_id_end", "store_id")
        end_store = comm.get_parameter_from_redis("store_id_end")
        # fleet_id = read_all_ini("all_data", "approve_van_info_query", "fleet_id")
        fleet_id = comm.get_parameter_from_redis("fleet_id")
        # province_code = read_all_ini("all_data", "approve_van_info_query", "province_code")
        province_code = comm.get_parameter_from_redis("province_code")
        # car_type_text = read_all_ini("all_data", "line_approve_1", "car_type_text")
        car_type_text = comm.get_parameter_from_redis("car_type_text")

        data = {
            "car_type": 200,
            "fleet_id": str(fleet_id),
            "plan_date": str(datetime.now().strftime('%Y-%m-%d')),
            "single_line": 1,
            "system_quote": null,
            "abnormal_cost": null,
            "final_cost": 2200,
            "line_cost": 2200,
            "line_back_cost": null,
            "line_name": "DD1-"+str(car_type_text)+"-LT1-3421-" + datetime.now().strftime("%Y%m%d 23:10"),
            "line_back_name": "DD2-"+str(car_type_text)+"-3421-LT1-null null",
            "driver": "autoname",
            "driver_phone": "111111111",
            "province_code": province_code,
            "plate_name": str(random.randint(100000000,9999999999)),
            "audit_type": 1,
            "fd_courier_id": null,
            "fd_courier_name": null,
            "line_timetable_dtolist": [
                {
                    "order_no": 1,
                    "store_id": start_store,
                    "estimate_end_time": "1380",
                    "estimate_start_time": "1390"
                },
                {
                    "order_no": 2,
                    "store_id": end_store,
                    "estimate_start_time": "",
                    "estimate_end_time": "1400"
                }
            ],
            "line_back_timetable_dtolist": [
                {
                    "order_no": 1,
                    "store_id": end_store,
                    "estimate_end_time": "",
                    "estimate_start_time": "",
                    "running_mileage": ""
                },
                {
                    "order_no": 2,
                    "store_id": start_store,
                    "running_mileage": "",
                    "estimate_start_time": "",
                    "estimate_end_time": ""
                }
            ]
        }
        logging.info(url)
        logging.info(data)
        resp = requests.post(url=url, json=data, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/all_data.ini"

        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/all_data.ini")


        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/all_data.ini"
        #
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("fleet_id")
        # cf.set("fleet_id", option="fleet_id", value=str(fleet_id))
        # with open(session_path, "a+") as f:  # 可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)

        comm.write_parameter_to_redis("fleet_id",fleet_id)
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")