#车辆出港
import logging
import random

import requests
#车辆出港
from app.Kit.Util.common_data import Common_data


class Vehicle_Departure():
    logging.basicConfig(level=logging.INFO)
    def vehicle_departure(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = "api/courier/v1/fleet/proof/outbound/new/bkk3a3163"
        # conventional_circuit_id = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id") #出车凭证码
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        url = host + "api/courier/v1/fleet/proof/outbound/new/%s"%conventional_circuit_id
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # num_read = read_config_ini(file_name="car_seal_code", sections="seal_code", option="code")    #封车码p1000000012
        # num = num_read.split("p")[1]
        # Car_seal_code= "p" + str(num)
        Car_seal_code= "p" + str(random.randint(1000000012,9999999999))
        data={
            "fleet_bound_images": [
                {
                    "image_url": "fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg",
                    "img": "https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg",
                    "sealing_number": Car_seal_code
                    # "sealing_number": "p1000000012"
                }
            ],
            "outbound_image": {
                "image_key": "fleetOutbound/1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg",
                "image_name": "1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg"
            }
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        # num_now = int(num)+1
        # if isinstance(num_now, int):
        #     logging.info("风车码写入成功")
        #     value_new = "p" + str(num_now)
        #     write_config_ini(file_name="car_seal_code", section="seal_code", option="code", value=value_new)
        # else:
        #     logging.info("风车码写入失败")

        comm.write_parameter_to_redis("car_seal_code",Car_seal_code)
        return resp.json()