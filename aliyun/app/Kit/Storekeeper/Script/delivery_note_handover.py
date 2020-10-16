import logging
import time

import requests
# #交接
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


class Delivery_Note_Handover():

    def delivery_note_handover(self,i):
        comm = Common_data()
        false = False
        true = True
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219cn8a/delivery_ticket_creation_scan"
        url = host + "api/courier/v1/parcels/"+pno+"/delivery_ticket_creation_scan"
        logging.info("交接,订单号是：")
        logging.info(pno)
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        ti= int(time.time())
        data = {
            "continue_de_enabled": false,
            "openned": true,
            # "routed_at": 1587032057,
            "routed_at": str(ti),
            "skipped_enabled": false
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        return res.json()