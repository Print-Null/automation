import logging

import requests
#选择留仓原因为错过班车时间
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


class Pre_Delivery_Detain_Warehouse_Missed():
    logging.basicConfig(level=logging.INFO)
    def pre_delivery_detain_warehouse_missed(self,i):
        comm = Common_data()
        false = False
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219ws1a/detain_warehouse"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        logging.info("交接前-货件留仓-错过班车时间,订单号是：")
        logging.info(pno)
        # url = host + "api/courier/v1/parcels/" + pno + "/marker_info"
        url = host + "api/courier/v1/parcels/" + pno + "/detain_warehouse"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        data = {
            "detained_marker_category": 41,
            "skipped_enabled": false
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)

        return res