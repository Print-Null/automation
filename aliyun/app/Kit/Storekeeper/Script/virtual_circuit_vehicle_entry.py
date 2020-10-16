
import requests
#虚拟线路车辆入港
from app.Kit.Util.common_data import Common_data


class Virtual_Circuit_Vehicle_Entry():

    def Virtual_circuit_vehicle_entry(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # id = read_vehicle_voucher("vehicle_voucher", "id")  # 出车凭证码
        id = comm.get_parameter_from_redis("vehicle_voucher_id")
        url = host + "api/courier/v1/fleet/proof/%s"%id
        # url = host + "api/courier/v1/fleet/proof/bkk3a3163"
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
