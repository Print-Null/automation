import logging
import time

import requests

#收件入仓
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


class Receipt_And_Entry():
    logging.basicConfig(level=logging.INFO)
    def receipt_and_entry(self, i):
        comm = Common_data()
        false = False
        # pno = read_request_data("courier_pno_number" + str(i), "pno" + str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        logging.info(pno)
        # host = read_common("host")
        host = comm.each_parameter("host")
        url = "api/courier/v1/parcels/" + str(pno) + "/receive_warehouse_scan"
        print(url)
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        logging.info(session_id)
        header = {
            "X-FLE-SESSION-ID": session_id,
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
        return resp.json()

