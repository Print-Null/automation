import logging

import pytest
import requests
from assertpy import assert_that
import allure
# from app.Kit.Storekeeper.utils.pack_no_range import read_pack_num_only
from app.Kit.Util.common_data import Common_data


@allure.feature("拆包功能->集包号码检查by")
class Test_Unpacking_Pack_Num_Check_By():
    logging.basicConfig(level=logging.INFO)


    @allure.story("拆包功能->集包号码检查")
    @pytest.mark.run(order=88)
    def test_unpacking_pack_num_check_by(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/pack/unseal/verify/p5712"
        # num_pack_old = read_pack_num_only("pack_no", "pack_num")
        # num_pack_new = int(num_pack_old) - 1
        # pack_num = "p" + str(num_pack_new)
        # logging.info("读取到的真实集包号是：")
        # logging.info(pack_num)
        pack_num = comm.get_parameter_from_redis("pack_no")
        url = host + "api/courier/v1/pack/unseal/verify/" + str(pack_num)
        logging.info("url拼接结果是：")
        logging.info(url)
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url, headers=header, verify=False)
        logging.info("拆包功能->集包号码检查,响应结果是:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()



