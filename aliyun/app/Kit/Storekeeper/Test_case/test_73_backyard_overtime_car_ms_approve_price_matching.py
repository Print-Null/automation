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


@allure.feature('加班车申请（中控审批界面）->系统报价')
class Test_backyard_overtime_car_ms_approve_price_matching():


    @pytest.mark.run(order=73)
    def test_test_backyard_overtime_car_ms_approve_price_matching(self):
        comm = Common_data()
        host = comm.each_parameter("ms_host")
        url = host + "ms/api/fleet/line/approve/price_matching"
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
        data = {
        "car_type": 100,
        "single_line": 2,
        "line_timetable_dtolist": [
          {
            "order_no": 1,
            "store_id": str(start_store),
            "estimate_end_time": "1399",
            "estimate_start_time": "1401"
          },
          {
            "order_no": 2,
            "store_id": str(end_store),
            "estimate_start_time": "",
            "estimate_end_time": "1039"
          }
        ],
        "line_back_timetable_dtolist": [
          {
            "order_no": 1,
            "store_id": str(end_store),
            "estimate_end_time": "1410",
            "estimate_start_time": "1415",
            "running_mileage": ""
          },
          {
            "order_no": 2,
            "store_id": str(start_store),
            "running_mileage": "",
            "estimate_start_time": "",
            "estimate_end_time": "1430"
          }
        ]

        }

        logging.info(url)
        logging.info(data)
        resp = requests.post(url=url, json=data, headers=headers, timeout=120, verify=False)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
