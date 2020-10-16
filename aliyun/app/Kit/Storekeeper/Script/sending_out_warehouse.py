import time

import requests

# from Courier.Utils.read_common import read_common
# from Courier.Utils.read_request_data import read_request_data
# from Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
# from Storekeeper.utils.read_vehicle_voucher import read_vehicle_voucher

#虚拟线路发件出仓
# from app.kit.Courier.Utils.read_common import read_common
# from app.kit.Courier.Utils.read_request_data import read_request_data
# from app.kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
# from app.kit.Storekeeper.utils.read_vehicle_voucher import read_vehicle_voucher
# from app.kit.Util.common_data import Common_data
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
# from app.Kit.Storekeeper.utils.read_vehicle_voucher import read_vehicle_voucher
from app.Kit.Util.common_data import Common_data


class Sending_Out_Warehouse():

    def sending_out_warehouse(self, i):
        comm = Common_data()
        true = True
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # pno = read_request_data("courier_pno_number"+str(i), "pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        # url = host + "api/courier/v1/parcels/TH050219bn4a/shipment_warehouse_scan?isFromScanner=false"
        url = host + "api/courier/v1/parcels/"+str(pno)+"/shipment_warehouse_scan?isFromScanner=false"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # proof_id = read_vehicle_voucher("vehicle_voucher","id")
        proof_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        ti = int(time.time())
        data= {
            "exist_dst": true,
            "next_store_id": "TH05020101",
            "proof_id": proof_id,
            # "proof_id": "BKK3A3081",
            # "routed_at": 1586854291,
            "routed_at": ti,
            "shipment_switch": true,
            "skipped_enabled": false,
            "transportion_category": 1,
            "van_line_id": "5da418f42d738a2161dbf23d"
        }
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        return resp.json()
