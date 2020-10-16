
import requests
#确认妥投
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


class Deliver_Confirm():

    def delivery_confirm(self,i):
        comm = Common_data()
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219cn8a/delivery_confirm"

        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/ticket/parcels/" + pno + "/delivery_confirm"
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        data = {
            "call_duration": 0,
            "continue_payment_flag": false,
            "other_image_key": "deliveryConfirmOther/1587116862-78d4d55fbb92493e91050149d966d461.jpg",
            "payment_category": 1,
            "signer_category": 0,
            "signer_content": "确认妥投"
        }

        res = requests.post(url=url,headers=header,json=data, verify=False)
        return res.json()
    