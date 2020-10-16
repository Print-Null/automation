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


@allure.feature('加班车申请（中控审批界面）->车牌号模糊查询')
class Test_backyard_overtime_car_ms_approve_van_info_query():


    @pytest.mark.run(order=72)
    def test_test_backyard_overtime_car_ms_approve_van_info_query(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/fleet/line/approve/van_info_query"
        # SESSION_ID = read_all_ini("by_warehouse_man_session", "ms_session", "ms_session")
        SESSION_ID = comm.get_parameter_from_redis("ms_session")
        headers = {
            "Accept-Language": "zh-CN",
            "Accept": "application/json, text/plain, */*",
            "X-MS-SESSION-ID": SESSION_ID
        }
        data = {
            "plate_name": "3",
            "province_code": "TH01",
            "fuzzy": "True"
        }
        logging.info(url)
        resp = requests.post(url=url, json=data, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        #["data"]["items"][-1]["id"]
        # 将仓管员登入的sessionid保存
        # 获取sessionid 存储到.ini文件中
        fleet_id = resp.json()["data"][0]["line_van_query_dto"]["fleet_id"]
        province_code = resp.json()["data"][0]["line_van_query_dto"]["province_code"]
        plate_name = resp.json()["data"][0]["plate_name"]

        #
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
        # cf.add_section("approve_van_info_query")
        # cf.set("approve_van_info_query", option="fleet_id", value=str(fleet_id))
        # cf.set("approve_van_info_query", option="province_code", value=str(province_code))
        # cf.set("approve_van_info_query", option="plate_name", value=str(plate_name))
        #
        # with open(session_path, "a+") as f:  # 可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)


        comm.write_parameter_to_redis("fleet_id",fleet_id)
        comm.write_parameter_to_redis("province_code",province_code)
        comm.write_parameter_to_redis("plate_name",plate_name)

        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")