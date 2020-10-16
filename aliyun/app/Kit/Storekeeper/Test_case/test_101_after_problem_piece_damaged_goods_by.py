import logging
import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


@allure.feature("交接后，货物破损")
class Test_After_Problem_Piece_Damaged_Goods_By():
    logging.basicConfig(level=logging.INFO)


    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [30]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接后，货物破损")
    @allure.story("交接后，货物破损")
    @pytest.mark.run(order=102)
    def test_after_problem_piece_damaged_goods_by(self,i):
        comm = Common_data()
        true = True
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219WZ3A/mark"
        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/ticket/parcels/" + pno + "/mark"

        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        data = {"marker_category": 5, "upload_photo": true}

        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("交接后，货物破损，响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()
