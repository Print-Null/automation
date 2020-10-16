import logging

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


@allure.feature("交接前，问题件提交，分错网点")
class Test_Pre_Problem_Piece_Branch_Out_By():
    logging.basicConfig(level=logging.INFO)



    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [22]
    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接前，问题件提交，分错网点")
    @allure.story("交接前，问题件提交，分错网点")
    @pytest.mark.run(order=94)
    def test_pro_problem_piece_branch_out_by(self, i):
        comm = Common_data()
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id =comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219xk3a/problem_submission"
        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/parcels/" + pno + "/problem_submission"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        data = {
            "difficulty_marker_category": 30
        }

        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("交接前，问题件提交，分错网点,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()
