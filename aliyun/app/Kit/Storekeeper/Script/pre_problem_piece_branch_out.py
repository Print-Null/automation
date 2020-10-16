import logging

import requests

#交接前，问题件提交，分错网点
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


class Pre_Problem_Piece_Branch_Out():
    logging.basicConfig(level=logging.INFO)
    def pro_problem_piece_branch_out(self,i):
        comm = Common_data()
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/parcels/TH050219xk3a/problem_submission"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        logging.info("交接前，问题件提交，分错网点,订单号是：")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/"+pno+"/problem_submission"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        data ={
            "difficulty_marker_category": 30
        }

        res = requests.post(url=url,headers=header,json=data, verify=False)
        return res