import logging
import time

import allure
import pytest
import requests
from assertpy import assert_that

from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase


@allure.feature("收件入仓")
class est_Receipt_And_Entry():
    logging.basicConfig(level=logging.INFO)

    def setup(self):
        self.redisObj = RedisBase()
        self.SESSION_ID = self.redisObj.get('warehouse_login_0_0_0_["data"]["sessionid"]')
        self.pno = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')

    @pytest.mark.run(order=18)
    def test_receipt_and_entry(self):
        comm = Common_data()
        false = False

        host = comm.each_parameter("host")
        url = "api/courier/v1/parcels/" + str(self.pno) + "/receive_warehouse_scan"
        print(url)
        header = {
            "X-FLE-SESSION-ID": self.SESSION_ID,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        ti = int(time.time())
        data ={
            "routed_at": ti,
            "skipped_enabled": false
        }
        resp = requests.post(url=host + url, headers=header, json=data, verify=False)
        logging.info(resp.json())
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")


