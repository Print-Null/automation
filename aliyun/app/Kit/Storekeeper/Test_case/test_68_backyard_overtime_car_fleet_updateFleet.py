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


@allure.feature('经理->单条申请，同意')
class Test_backyard_overtime_car_fleet_updateFleet(object):

    @pytest.mark.run(order=68)
    def test_test_backyard_overtime_car_fleet_updateFleet(self):
        comm = Common_data()
        host = comm.each_parameter("backyard_host")
        url = host + "api/_/fleet/updateFleet"
        # SESSION_ID = read_all_ini("by_warehouse_man_session", "outlet_manager", "outlet_manager_session")
        SESSION_ID = comm.get_parameter_from_redis("outlet_manager_session")
        headers = {
            "Accept-Language": "zh-CN",
            "Content-Type": "application/json",
            "BY-PLATFORM": "FB_ANDROID",
            "X-BY-SESSION-ID": SESSION_ID
        }
        # id = read_all_ini("all_data", "auditlist_detail_id", "auditlist_detail_id")
        id = comm.get_parameter_from_redis("auditlist_detail_id")
        data = {
          "status": 2,
          "audit_id": id,
          "reject_reason": "1"
        }
        logging.info(data)
        resp = requests.post(url=url, json=data, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["msg"]).is_equal_to("请求成功!")



