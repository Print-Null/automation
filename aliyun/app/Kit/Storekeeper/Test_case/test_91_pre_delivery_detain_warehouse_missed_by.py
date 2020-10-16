import logging

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


@allure.feature("交接前-货件留仓-错过班车时间")
class Test_Pre_Delivery_Detain_Warehouse_Missed_By():
    logging.basicConfig(level=logging.INFO)


    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #将第一个订单，来进行此接口,不需要修改list_i
    list_i = [20]
    @allure.title("错过加班车时间")
    @allure.story("错过加班车时间")
    @pytest.mark.parametrize("i", list_i)
    @pytest.mark.run(order=92)
    def test_pre_delivery_detain_warehouse_missed_by(self,i):
        comm = Common_data()
        false = False
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219ws1a/detain_warehouse"
        # pno = read_request_data(sections="courier_pno_number" + str(i), option="pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        # url = host + "api/courier/v1/parcels/" + pno + "/marker_info"
        url = host + "api/courier/v1/parcels/" + pno + "/detain_warehouse"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        data = {
            "detained_marker_category": 41,
            "skipped_enabled": false
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)

        logging.info("交接前-货件留仓-错过班车时间,响应结果是：")
        logging.info(res.json())
        assert_that(res.status_code).is_equal_to(200)
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
        schema_res = Validate_jsonschema(res.json(), "pre_delivery_detain_warehouse_inadquate.json")
        assert_that(schema_res).is_none()
