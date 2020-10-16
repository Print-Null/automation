import logging
import time
import allure
import pytest
import requests

#交接
from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase


@allure.feature("交接接口")
class Test_Delivery_Note_Handover():
    def setup(self):
        self.redisObj = RedisBase()
        self.SESSION_ID = self.redisObj.get('courier_login_0_0_0_["data"]["sessionid"]')
        # self.SESSION_ID = self.redisObj.get('warehouse_login_0_0_0_["data"]["sessionid"]')
        self.pno = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')
    @pytest.mark.run(order=48)
    def test_delivery_note_handover(self):
        comm = Common_data()
        false = False
        true = True
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/parcels/"+str(self.pno)+"/delivery_ticket_creation_scan"
        logging.info("交接,订单号是：")
        logging.info(self.pno)
        header = {
            "X-FLE-SESSION-ID": self.SESSION_ID,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        logging.info("交接给的快递员是")
        logging.info(self.SESSION_ID)
        ti= int(time.time())
        data = {
            "continue_de_enabled": false,
            "openned": true,
            # "routed_at": 1587032057,
            "routed_at": str(ti),
            "skipped_enabled": false
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info(res.json())