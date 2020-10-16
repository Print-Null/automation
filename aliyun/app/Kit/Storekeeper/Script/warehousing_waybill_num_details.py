import logging

import requests
#到件入仓-输入运单号->快件详情
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


class Warehousing_Waybill_Num_Details():
    logging.basicConfig(level=logging.INFO)
    def warehousing_waybill_num_details(self,i):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219BN4A"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        logging.info("到件入仓-输入运单号->快件详情,订单号是：")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/%s"%pno
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }

        resp = requests.get(url=url, headers=header, verify=False)
        return resp.json()