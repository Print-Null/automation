import logging
import time

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


@allure.feature("到件入仓-输入运单号")
class Test_Warehousing_Waybill_Num_By():
    logging.basicConfig(level=logging.INFO)


    list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @pytest.mark.parametrize("i",list_i)
    @allure.story("到件入仓-输入运单号")
    @pytest.mark.run(order=86)
    def test_warehousing_waybill_num_by(self,i):
        comm = Common_data()
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")

        # url = host + "api/courier/v1/parcels/TH050219bn4a/arrival_warehouse_scan"
        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/parcels/" + pno + "/arrival_warehouse_scan"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # conventional_circuit_id = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")  # 出车凭证码
        # conventional_circuit_id = read_all_ini("all_data", "vehicle_voucher_by", "vehicle_voucher_by_id")
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        ti = int(time.time())
        data = {
            # "proof_id": "BKK3A3163",
            "proof_id": conventional_circuit_id,
            # "routed_at": 1587020880,
            "routed_at": ti,
            "skipped_enabled": false
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("到件入仓-输入运单号,响应结果:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()

