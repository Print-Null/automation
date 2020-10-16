import logging
import time
import allure
import pytest
import requests

from app.Kit.Util.common_data import Common_data
from utils.redisbase import RedisBase

@allure.feature("常规线路发件出仓")
class est_Conventional_Circuit_Sending_Out_Warehouse():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.redisObj = RedisBase()
        self.SESSION_ID = self.redisObj.get('warehouse_login_0_0_0_["data"]["sessionid"]')
        self.pno = self.redisObj.get('courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]')
        self.proof_id = self.redisObj.get('vehicle_voucher_id')
        self.van_line_id_ = self.redisObj.get('generate_vehicle_voucher')
    @pytest.mark.run(order=21)
    def test_conventional_circuit_sending_out_warehouse(self):
        comm = Common_data()
        true = True
        false = False
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/parcels/" + str(self.pno) + "/shipment_warehouse_scan?isFromScanner=false"
        header = {
            "X-FLE-SESSION-ID": self.SESSION_ID,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        ti = int(time.time())
        van_line_id = dict(eval(self.van_line_id_))
        data = {
            "exist_dst": true,
            "next_store_id": "TH01470301",
            "proof_id": self.proof_id,
            # "proof_id": "BKK3A3081",
            # "routed_at": 1586854291,
            "routed_at": ti,
            "shipment_switch": true,
            "skipped_enabled": false,
            "transportion_category": 1,
            # "van_line_id": "5d1dc8642d738a29e93034e9"
            "van_line_id": str(van_line_id["id"])
        }
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        logging.info("响应结果")
        logging.info(resp.json())
        logging.info("请求参数")
        logging.info(data)
