import logging
import allure
import pytest
import requests
from assertpy import assert_that
# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
from app.Kit.Util.common_data import Common_data


@allure.feature("车辆出港接口->出车凭证线路校验by")
class Test_Vehicle_Departure_Check_By():
    logging.basicConfig(level=logging.INFO)

    @allure.story("车辆出港功能->出车凭证线路校验by")
    @pytest.mark.run(order=81)
    def test_vehicle_departure_check_by(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # Vehicle_Voucher = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")
        # proof_id = read_all_ini("all_data", "vehicle_voucher_by", "vehicle_voucher_by_id")
        proof_id = comm.get_parameter_from_redis("vehicle_voucher_by_id")
        url = host + "api/courier/v1/fleet/proof/" + str(proof_id)
        # url = host + "api/courier/v1/fleet/proof/bkk3a3081"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        resp = requests.get(url=url, headers=header, verify=False)
        logging.info("车辆出港功能->出车凭证线路校验,响应结果是:")
        logging.info(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["data"]).is_not_none()


