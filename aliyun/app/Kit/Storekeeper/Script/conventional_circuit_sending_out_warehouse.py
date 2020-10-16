import json
import logging
import os
import time
import requests


#常规线路发件出仓
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.read_vehicle_voucher import read_vehicle_voucher
from app.Kit.Util.common_data import Common_data


class Conventional_Circuit_Sending_Out_Warehouse():
    logging.basicConfig(level=logging.INFO)
    def conventional_circuit_sending_out_warehouse(self, i):
        comm = Common_data()
        true = True
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # pno = read_request_data("courier_pno_number" + str(i), "pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        logging.info("新建常规线路获取到的订单号是")
        logging.info(pno)
        # url = host + "api/courier/v1/parcels/TH050219bn4a/shipment_warehouse_scan?isFromScanner=false"
        url = host + "api/courier/v1/parcels/" + str(pno) + "/shipment_warehouse_scan?isFromScanner=false"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # proof_id = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")
        proof_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        ti = int(time.time())
        #获取van_line_id
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "\conf\ms_generate_vehicle_voucher_actual.json"
        # session_path = curpath + "\conf\ms_generate_vehicle_voucher_actual.json"
        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf\ms_generate_vehicle_voucher_actual.json")

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/ms_generate_vehicle_voucher_actual.json"
        #
        #
        # with open(session_path, encoding="utf-8", mode='r') as f:
        #     van_id = json.load(f)
        #     logging.info("读取到的信息是：")
        #     logging.info(van_id)
        #     logging.info(type(van_id))
        #     logging.info(van_id["id"])
        #     van_line_id = van_id["id"]
        # ms_generate_vehicle_voucher_actual
        van_id = dict(eval(comm.get_parameter_from_redis("ms_generate_vehicle_voucher_actual")))
        van_line_id = van_id["id"]
        data = {
            "exist_dst": true,
            "next_store_id": "TH01470301",
            "proof_id": proof_id,
            # "proof_id": "BKK3A3081",
            # "routed_at": 1586854291,
            "routed_at": ti,
            "shipment_switch": true,
            "skipped_enabled": false,
            "transportion_category": 1,
            # "van_line_id": "5d1dc8642d738a29e93034e9"
            "van_line_id": str(van_line_id)
        }
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        return resp.json()
