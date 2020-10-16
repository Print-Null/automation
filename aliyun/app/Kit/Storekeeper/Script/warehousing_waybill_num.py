import logging
import time
import requests
#到件入仓-输入运单号
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


class Warehousing_Waybill_Num():
    logging.basicConfig(level=logging.INFO)
    def warehousing_waybill_num(self, i):
        comm = Common_data()
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")

        # url = host + "api/courier/v1/parcels/TH050219bn4a/arrival_warehouse_scan"
        # pno=read_request_data(sections="courier_pno_number" + str(i), option="pno"+ str(i))
        pno=read_request_data("courier_pno_number" + str(i))
        logging.info("到件入仓-输入运单号,获取的订单号是")
        logging.info(pno)
        url = host + "api/courier/v1/parcels/"+pno+"/arrival_warehouse_scan"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # conventional_circuit_id = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")  # 出车凭证码
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        ti = int(time.time())
        data = {
            # "proof_id": "BKK3A3163",
            "proof_id": conventional_circuit_id,
            # "routed_at": 1587020880,
            "routed_at": ti,
            "skipped_enabled": false
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        return resp.json()