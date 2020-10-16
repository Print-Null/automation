import requests
#到件入仓->出车凭证校验
# from app.Kit.Storekeeper.utils.read_vehicle_voucher import read_vehicle_voucher
from app.Kit.Util.common_data import Common_data


class Warehousing_Vehicle_Voucher_Check():

    def warehousing_vehicle_voucher_check(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/fleet/proof/bkk3a3163"
        # conventional_circuit_id = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")  # 出车凭证码
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        url = host + "api/courier/v1/fleet/proof/%s"%conventional_circuit_id
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