import logging

import pytest
import requests
from assertpy import assert_that
import allure
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


@allure.feature("妥投前确认")
class Test_Pre_Delivery_Confirm_by():
    logging.basicConfig(level=logging.INFO)

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i

    list_i = [34]

    @pytest.mark.parametrize("i", list_i)
    @allure.story("妥投前确认")
    @allure.title("妥投前确认")
    @pytest.mark.run(order=106)
    def test_pre_delivery_confirm_by(self,i):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219cn8a/pre_delivery_confirm"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/ticket/parcels/"+pno+"/pre_delivery_confirm"
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url, headers=header, verify=False)
        logging.info("妥投前确认接口,响应结果是:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()




