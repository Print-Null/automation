import logging
import requests
#复称
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


class Repetition():
    logging.basicConfig(level=logging.INFO)
    def repetition(self, i):
        comm = Common_data()
        false =False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # pno = read_request_data("courier_pno_number"+str(i), "pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        logging.info("复称接口，读取到的订单号是：")
        logging.info(pno)

        # url = host + "api/courier/v1/parcels/TH050219YG5A/store_keeper_update_weight"
        url = host + "api/courier/v1/parcels/"+str(pno)+"/store_keeper_update_weight"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # data = "{\n    \"height\": 1,\n    \"length\": 1,\n    \"skipped_enabled\": false,\n    \"skipping_tips\": [],\n    \"weight\": 4000,\n    \"width\": 1\n}"
        data = {
                "height": 1,
                "length": 1,
                "skipped_enabled": false,
                "skipping_tips": [],
                "weight": 4000,
                "width": 1
            }

        response = requests.request("PATCH", url=url, headers=header, json=data, verify=False)
        return response.json()