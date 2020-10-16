import logging

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


@allure.feature("确认妥投后-收入金额提示")
class Test_Delivery_Confirm_DeliveryReward_by():
    logging.basicConfig(level=logging.INFO)


    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口

    list_i = [34]

    @pytest.mark.parametrize("i", list_i)
    @allure.story("确认妥投后-收入金额提示")
    @allure.title("确认妥投后-收入金额提示")
    @pytest.mark.run(order=108)
    def test_delivery_confirm_deliveryReward_by(self,i):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/message/deliveryReward/TH050219cn8a"
        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/message/deliveryReward/%s" % pno
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url, headers=header, verify=False)
        logging.info("确认妥投后-收入金额提示,接口响应结果是:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["msg"]).is_equal_to("成功")
        assert_that(res.json()["data"]).is_not_none()


