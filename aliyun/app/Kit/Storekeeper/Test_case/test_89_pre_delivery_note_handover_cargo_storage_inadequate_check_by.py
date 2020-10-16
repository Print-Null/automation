import logging

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


@allure.feature("交接前，货件留仓->运单检查")
class Test_Pre_Delivery_Note_Handover_Cargo_Storage_Inadequate_Check_By():
    logging.basicConfig(level=logging.INFO)

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #将第一个订单，来进行此接口,不需要修改list_i
    list_i = [18]

    @allure.title("货件留仓->运单检查")
    @allure.story("交接前，货件留仓->运单检查")
    @pytest.mark.parametrize("i",list_i)
    @pytest.mark.run(order=90)
    def test_pre_delivery_note_handover_cargo_storage_inadequate_check_by(self,i):

        comm = Common_data()
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219ws1a/marker_info"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/parcels/"+pno+"/marker_info"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        res = requests.get(url=url, headers=header, verify=False)
        logging.info(res.json())
        logging.info("交接前，货件留仓->运力不足，响应结果是：")
        assert_that(res.status_code).is_equal_to(200)
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()



