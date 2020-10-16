import configparser
import sys, os

# from app.kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.kit.Util.common_data import Common_data
# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
from app.Kit.Util.common_data import Common_data

sys.path.append(os.getcwd())
import allure
from assertpy import assert_that
import requests
import logging
import pytest

logging.basicConfig(level=logging.INFO)


@allure.feature('加班车申请（中控审批界面）')
class Test_backyard_overtime_car_ms_api_fleet_line_approve_1():

    @pytest.mark.run(order=71)
    def test_test_backyard_overtime_car_ms_api_fleet_line_approve_1(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        # id = read_all_ini("all_data", "line_approve_id", "line_approve_id")
        id = comm.get_parameter_from_redis("line_approve_id")
        url = host + "ms/api/fleet/line/approve/" + str(id)
        SESSION_ID = comm.get_parameter_from_redis("ms_session")
        # SESSION_ID = read_all_ini("by_warehouse_man_session", "ms_session", "ms_session")
        headers = {
            "Accept-Language": "zh-CN",
            "Accept": "application/json, text/plain, */*",
            "X-MS-SESSION-ID": SESSION_ID
        }
        logging.info(url)
        resp = requests.get(url=url, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        #["data"]["items"][-1]["id"]
        # 将仓管员登入的sessionid保存
        # 获取sessionid 存储到.ini文件中
        start_store = resp.json()["data"]["start_store"]
        end_store = resp.json()["data"]["end_store"]
        car_type = resp.json()["data"]["car_type"]
        car_type_text = resp.json()["data"]["car_type_text"]

        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/all_data.ini"
        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/all_data.ini")

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/all_data.ini"
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("line_approve_1")
        # cf.set("line_approve_1", option="start_store", value=str(start_store))
        # cf.set("line_approve_1", option="end_store", value=str(end_store))
        # cf.set("line_approve_1", option="car_type", value=str(car_type))
        # cf.set("line_approve_1", option="car_type_text", value=str(car_type_text))
        # with open(session_path, "a+") as f:  # 可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)

        comm.write_parameter_to_redis("start_store",start_store)
        comm.write_parameter_to_redis("end_store",end_store)
        comm.write_parameter_to_redis("car_type",car_type)
        comm.write_parameter_to_redis("car_type_text",car_type_text)
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")

