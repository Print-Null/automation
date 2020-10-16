import logging

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.pack_no_range import read_pack_num_only
from app.Kit.Util.common_data import Common_data


@allure.feature("拆包by")
class Test_Unpack_by():
    logging.basicConfig(level=logging.INFO)


    # list_i = [1, 2, 3, 4]
    #去代码逻辑里修改list_i
    @allure.story("拆包")
    @pytest.mark.run(order=89)
    def test_unpack_by(self):
        comm = Common_data()
        pno_list = []
        true = True
        # host = read_common("host")
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/unseal"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")

        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # num_pack_old = read_pack_num_only("pack_no", "pack_num")
        # num_pack_new = int(num_pack_old) - 1
        # pack_num = "p" + str(num_pack_new)
        pack_num = comm.get_parameter_from_redis("pack_no")
        # 修改 list_i
        list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in range(len(list_i)):
            # pno = read_request_data("courier_pno_number" + str(i + 18), "pno" + str(i + 18))
            pno = read_request_data("courier_pno_number" + str(i+18))
            # logging.info(type(pno))
            pno_list.append(pno)
        logging.info("订单号读取结果是：")
        logging.info(pno_list)

        data = {
            "continue_flag": true,
            # "pack_no": "P5712",
            "pack_no": pack_num,
            "recent_pnos": pno_list
        }
        unpack = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("拆包接口响应结果是:")
        logging.info(unpack.json())
        assert_that(unpack.json()["code"]).is_equal_to(1)
        assert_that(unpack.json()["message"]).is_equal_to("success")
        assert_that(unpack.json()["data"]).is_none()

