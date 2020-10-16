import logging

import requests
#车辆出港->出车凭证线路校验
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
# from app.Kit.Storekeeper.utils.read_vehicle_voucher import read_vehicle_voucher
from app.Kit.Util.common_data import Common_data


class Vehicle_Departure_Check():

    def vehicle_departure_check(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # Vehicle_Voucher = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")
        Vehicle_Voucher = comm.get_parameter_from_redis("vehicle_voucher_id")
        url = host + "api/courier/v1/fleet/proof/" + str(Vehicle_Voucher)
        # url = host + "api/courier/v1/fleet/proof/bkk3a3081"
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

