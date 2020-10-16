import logging
import allure
import pytest
import requests
from assertpy import assert_that

from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase


@allure.feature("复称接口")
class Test_Repetition():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.SESSION_ID = self.redisObj.get('warehouse_login_0_0_0_["data"]["sessionid"]')
        self.pno = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')

    @pytest.mark.run(order=45)
    def test_repetition(self):
        comm = Common_data()
        false =False
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/parcels/"+str(self.pno)+"/store_keeper_update_weight"
        header = {
            "X-FLE-SESSION-ID": self.SESSION_ID,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        data = {
                "height": 1,
                "length": 1,
                "skipped_enabled": false,
                "skipping_tips": [],
                "weight": 4000,
                "width": 1
            }

        response = requests.request("PATCH", url=url, headers=header, json=data, verify=False)
        logging.info(response.json())
        assert_that(response.json()["code"]).is_equal_to(1)
        assert_that(response.json()["message"]).is_equal_to("success")