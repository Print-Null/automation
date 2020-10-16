
import requests
#妥投完成后,奖励金额提示
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data


class Delivery_Confirm_DeliveryReward():

    def delivery_confirm_deliveryReward(self, i):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/message/deliveryReward/TH050219cn8a"

        # pno = read_request_data(sections="courier_pno_number"+str(i), option="pno"+str(i))
        pno = read_request_data("courier_pno_number"+str(i))
        url = host + "api/courier/v1/message/deliveryReward/%s"%pno
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url,headers=header, verify=False)
        return res.json()