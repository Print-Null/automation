import logging
import time
import requests
#交接前，问题件提交，货物破损
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


class Pre_Problem_Piece_Damaged_Goods():
    logging.basicConfig(level=logging.INFO)
    def pre_problem_piece_damaged_goods(self,i):
        comm = Common_data()
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219WZ3A/mark"
        pno = read_request_data("courier_pno_number"+str(i))
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        # url = host + "api/courier/v1/parcels/TH050219x61a/problem_submission"
        url = host + "api/courier/v1/parcels/"+pno+"/problem_submission"
        logging.info("交接前，问题件提交，货物破损,订单号是")
        logging.info(pno)
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        ti = int(time.time())
        data = {
            "difficulty_marker_category": 20,
            "image_keys": [
                # "difficulty/1587551931-0e0d9fc03a3f40028bd582cc709dcdb2.jpg"
                "difficulty/"+str(ti)+"-0e0d9fc03a3f40028bd582cc709dcdb2.jpg"
            ],
            "remark": "货物破损"
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        return res
