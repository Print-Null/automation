import requests
#妥投前确认
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


class Pre_Delivery_Confirm():

    def pre_delivery_confirm(self,i):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/ticket/parcels/TH050219cn8a/pre_delivery_confirm"
        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number" + str(i))
        url = host + "api/courier/v1/ticket/parcels/"+pno+"/pre_delivery_confirm"
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url, headers=header, verify=False)
        return res.json()