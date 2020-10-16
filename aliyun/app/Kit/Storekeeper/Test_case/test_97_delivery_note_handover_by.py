import logging
import time

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


@allure.feature("交接接口")
class Test_Delivery_Note_Handover_By():
    logging.basicConfig(level=logging.INFO)


    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # 1, 2, 3, 4, 5, 6, 7, 8,运单状态为 疑难件处理中 不允许交接
    list_i = [27, 28, 29, 30, 31, 32, 33, 34]
    @pytest.mark.parametrize("i", list_i)
    @allure.story("交接")
    @allure.title("交接")
    @pytest.mark.run(order=98)
    def test_delivery_note_handover_by(self,i):
        comm = Common_data()
        false = False
        true = True
        pno = read_request_data("courier_pno_number" + str(i))
        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219cn8a/delivery_ticket_creation_scan"
        url = host + "api/courier/v1/parcels/" + pno + "/delivery_ticket_creation_scan"

        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        ti = int(time.time())
        data = {
            "continue_de_enabled": false,
            "openned": true,
            # "routed_at": 1587032057,
            "routed_at": str(ti),
            "skipped_enabled": false
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)

        logging.info("交接,接口响应结果:")
        logging.info(res.json())

        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
