import logging

import allure
import pytest
import requests
from assertpy import assert_that
# from app.kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
# from app.kit.Util.common_data import Common_data
# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


@allure.feature("到件入仓")
class Test_Warehousing_Vehicle_Voucher_Check_By():
    logging.basicConfig(level=logging.INFO)

    @allure.story("到件入仓->出车凭证校验")
    @pytest.mark.run(order=85)
    def test_warehousing_vehicle_voucher_check_by(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/fleet/proof/bkk3a3163"
        # conventional_circuit_id = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")  # 出车凭证码
        # conventional_circuit_id = read_all_ini("all_data", "vehicle_voucher_by", "vehicle_voucher_by_id")
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_by_id")
        url = host + "api/courier/v1/fleet/proof/%s"%conventional_circuit_id
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url, headers=header, verify=False)
        logging.info("到件入仓->出车凭证校验,响应结果:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_empty()
