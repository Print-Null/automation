import time
import requests
#交接后，COD金额不正确
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


class After_Problem_Piece_COD_Price_Err():

    def after_problem_piece_cod_price_err(self,i):
        comm = Common_data()
        true = True
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219WZ3A/mark"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/ticket/parcels/"+pno+"/mark"

        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        num = int(time.time())
        data = {
            "attachment_form": [
                {
                    # "object_key": "deliveryPickupsMarkUpload/1587539227-147953f42a194d3e97a7935dd594ad91.jpg"
                    "object_key": "deliveryPickupsMarkUpload/"+str(num)+"-147953f42a194d3e97a7935dd594ad91.jpg"
                }
            ],
            "marker_category": 76,
            "remark": "e",
            "upload_photo": true
        }

        res = requests.post(url=url, headers=header, json=data, verify=False)
        return res