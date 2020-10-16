import logging

import requests

#交接前，货件留仓->订单检查
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


class Pre_Delivery_Note_Handover_Cargo_Storage_Inadequate_Check():
    logging.basicConfig(level=logging.INFO)
    def pre_delivery_note_handover_cargo_storage_inadequate_check(self,i):
        comm = Common_data()
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219ws1a/marker_info"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        logging.info("货件留仓->运单检查,订单号是：")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/"+pno+"/marker_info"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        res = requests.get(url=url, headers=header, verify=False)
        return res

