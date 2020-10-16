import logging
import requests
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data

logging.basicConfig(level=logging.INFO)
#揽收完成
class Collect_Complete():

    def collect_complete(self, i):
        comm = Common_data()
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        # ticket_pickup_id = read_request_data("ticket_pickup" + str(i), "ticket_pickup_id" + str(i))
        ticket_pickup_id = read_request_data("ticket_pickup_id" + str(i))
        url = "api/courier/v1/ticket/%s"%ticket_pickup_id
        header = {
            "X-FLE-SESSION-ID":session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # host = read_common("host")
        host = comm.each_parameter("host")
        resp = requests.post(url=host+url, headers=header, verify=False)
        logging.info("揽收完成接口运行完毕")
        return resp.json()


