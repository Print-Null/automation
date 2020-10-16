import logging
import random
import allure
import pytest
import requests
from assertpy import assert_that

from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase


@allure.feature("集包接口-集包成功")
class est_Package_seal():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.SESSION_ID = self.redisObj.get('warehouse_login_0_0_0_["data"]["sessionid"]')
        self.pno = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')

    @pytest.mark.run(order=20)
    def test_package_seal(self):
        comm = Common_data()
        pno_list = []
        true = True
        false = False
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/seal"
        header = {
            "X-FLE-SESSION-ID": self.SESSION_ID,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        pack_no = "p" + str(random.randint(1000, 9999))
        data = {
            "direction_store_code": "C",
            "pack_category": 1,
            # "pack_no": "p5041",
            "pack_no": pack_no,
            "recent_pnos":[self.pno],
            "valid_parcel": true
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("设置为true")
        logging.info(resp.json())
        logging.info(data)

        data1 = {
            "direction_store_code": "C",
            "pack_category": 1,
            "pack_no": pack_no,
            "recent_pnos": [self.pno],
            "valid_parcel": false
        }
        resp1 = requests.post(url=url, headers=header, json=data1, verify=False)
        logging.info("设置为false")
        logging.info(resp1.json())
        logging.info(data1)

        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp1.json()["code"]).is_equal_to(1)
        assert_that(resp1.json()["message"]).is_equal_to("success")