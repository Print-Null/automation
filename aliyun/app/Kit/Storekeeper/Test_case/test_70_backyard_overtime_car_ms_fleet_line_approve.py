import configparser
import os
from datetime import datetime
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


@allure.feature('ms后台加班车审批列表->查询展示')
class Test_backyard_overtime_car_ms_fleet_line_approve():

    @pytest.mark.run(order=70)
    def test_test_backyard_overtime_car_ms_fleet_line_approve(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        url = host + 'ms/api/fleet/line/approve?serialNo=&applyStartDate=&applyEndDate=&state=7&pageSize=20&pageNum=1&startTime='+str(datetime.now().strftime("%Y-%m-%d 00:00:00"))+'&endTime='+str(datetime.now().strftime("%Y-%m-%d 23:59:59"))
        # SESSION_ID = read_all_ini("by_warehouse_man_session", "ms_session", "ms_session")
        SESSION_ID = comm.get_parameter_from_redis("ms_session")
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
        session = resp.json()["data"]["items"][-1]["id"]
        logging.info(session)
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
        # cf.add_section("line_approve_id")
        # cf.set("line_approve_id", option="line_approve_id", value=str(session))
        # with open(session_path, "a+") as f:  # 可读可写，会覆盖  a+可读可写，不会覆盖
        #     cf.write(f)

        comm.write_parameter_to_redis("line_approve_id", session)
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")

