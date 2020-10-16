import configparser
import json
import logging
import os
import datetime

import allure
import pytest
import requests
from assertpy import assert_that
# from app.kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.kit.Util.common_data import Common_data
# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
from app.Kit.Util.common_data import Common_data


@allure.feature("网点车线任务列表by")
class Test_Outlet_Vehicle_Line_By():
    logging.basicConfig(level=logging.INFO)
    @allure.story("网点车线任务列表by")
    @pytest.mark.run(order=78)
    def test_outlet_vehicle_line_by(self):
        comm = Common_data()
        # host = read_common("ms_host")
        host = comm.each_parameter("ms_host")
        today = datetime.date.today()
        # url = host + "ms/api/fleet/van/line/task?type=1&startDate=2020-06-02&pageNum=1&pageSize=20"
        url = host + "ms/api/fleet/van/line/task?type=1&startDate=" + str(today) + "&pageNum=1&pageSize=20"
        # SESSION_ID = read_ms_session("ms", "ms_session")
        # SESSION_ID = read_all_ini("by_warehouse_man_session","by_warehouse","warehouse_session")
        SESSION_ID = comm.get_parameter_from_redis("warehouse_session")
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json;charset=UTF-8",
            "X-MS-SESSION-ID": SESSION_ID
        }
        resp = requests.get(url=url, headers=header, verify=False)
        dat = resp.json()["data"]["items"][0]
        logging.info("接口响应结果是：")
        logging.info(dat)
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "\conf\ms_generate_vehicle_voucher_actual_by.json"
        #
        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf\ms_generate_vehicle_voucher_actual_by.json")
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/ms_generate_vehicle_voucher_actual_by.json"
        #
        #
        # with open(session_path, encoding="utf-8", mode='w') as f:
        #     json.dump(dat, f)

        comm.write_parameter_to_redis("ms_generate_vehicle_voucher_actual_by",str(dat))
        logging.info("网点车险任务响应结果是：")
        logging.info(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
