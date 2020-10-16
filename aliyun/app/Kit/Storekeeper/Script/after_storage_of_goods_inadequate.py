import logging

import requests
#交接后-货件留仓-运力不足-快递员
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


class After_Storage_Of_Goods_Inadequate():
    logging.basicConfig(level=logging.INFO)
    def after_storage_of_goods_inadequate(self,i):
        comm = Common_data()
        true = True
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219WM1A/mark"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        logging.info("运力不足,订单号是：")
        logging.info(pno)
        url = host + "api/courier/v1/ticket/parcels/"+pno+"/mark"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        data = {
            "marker_category": 71,
            "upload_photo": true
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        return res