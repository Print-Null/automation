import logging

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


@allure.feature("到件入仓-输入运单号->快件详情by")
class Test_Warehousing_Waybill_Num_Details_By():
    logging.basicConfig(level=logging.INFO)


    list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @pytest.mark.parametrize("i",list_i)
    @allure.story("到件入仓-输入运单号->快件详情by")
    @pytest.mark.run(order=87)
    def test_warehousing_waybill_num_details_by(self,i):
        comm = Common_data()
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219BN4A"
        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/parcels/%s" % pno
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }

        res = requests.get(url=url, headers=header, verify=False)
        logging.info("到件入仓-输入运单号->快件详情,响应结果:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()