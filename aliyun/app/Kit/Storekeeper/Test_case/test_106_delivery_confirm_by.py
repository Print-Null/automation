import logging

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


@allure.feature("确认妥投接口")
class Test_Delivery_Perfirm_by():
    logging.basicConfig(level=logging.INFO)


    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [34]

    @pytest.mark.parametrize("i", list_i)
    @allure.story("确认妥投")
    @allure.title("确认妥投")
    @pytest.mark.run(order=107)
    def test_delivery_confirm_by(self,i):
        comm = Common_data()
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219cn8a/delivery_confirm"

        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/ticket/parcels/" + pno + "/delivery_confirm"
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        data = {
            "call_duration": 0,
            "continue_payment_flag": false,
            "other_image_key": "deliveryConfirmOther/1587116862-78d4d55fbb92493e91050149d966d461.jpg",
            "payment_category": 1,
            "signer_category": 0,
            "signer_content": "确认妥投"
        }

        res = requests.post(url=url, headers=header, json=data, verify=False)

        logging.info("确认妥投,接口响应结果:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_empty()




