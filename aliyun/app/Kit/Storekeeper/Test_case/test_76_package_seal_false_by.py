import logging
import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.pack_no_range import pack_no_range
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


@allure.feature("集包接口-将集包号设为无效")
class est_Package_Seal_False_By():
    logging.basicConfig(level=logging.INFO)


    # list_i = [1, 2, 3, 4],去代码逻辑层修改list_i
    @allure.story("集包功能->集包成功")
    @pytest.mark.run(order=76)
    def est_package_seal_false_by(self):
        comm = Common_data()
        pno_list = []
        true = True
        false = False
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/seal"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # 修改 list_i
        list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in range(len(list_i)):
            # pno = read_request_data("courier_pno_number" + str(i + 18), "pno" + str(i + 18))
            pno = read_request_data("courier_pno_number" + str(i+18))
            pno_list.append(pno)
        logging.info("订单号读取结果是：")
        logging.info(pno_list)
        pack_num = pack_no_range("pack_no", "pack_num")

        pack_no = "p" + str(pack_num)
        logging.info("集包号读取结果是：")
        logging.info(pack_no)

        data = {
            "direction_store_code": "C",
            "pack_category": 1,
            # "pack_no": "p5041",
            "pack_no": pack_no,
            "recent_pnos":
                pno_list,
            "valid_parcel": false
        }
        result = requests.post(url=url, headers=header, json=data, verify=False)

        logging.info("集包返回结果为：")
        logging.info(result.json())
        assert_that(result.json()["code"]).is_equal_to(1)
        assert_that(result.json()["message"]).is_equal_to("success")
        assert_that(result.json()["data"]).is_none()

