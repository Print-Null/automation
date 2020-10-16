import logging

import pytest
import requests
from assertpy import assert_that
import allure
# from app.Kit.Storekeeper.utils.read_config_ini import read_config_ini
# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
# from app.Kit.Storekeeper.utils.write_config_ini import write_config_ini
from app.Kit.Util.common_data import Common_data


@allure.feature("车辆出港接口by")
class Test_Vehicle_Departure_By():
    logging.basicConfig(level=logging.INFO)

    @allure.story("车辆出港功能by")
    @pytest.mark.run(order=82)
    def test_vehicle_departure_by(self):
        comm = Common_data()
        host = comm.each_parameter("host")
        # conventional_circuit_id = read_all_ini("all_data", "vehicle_voucher_by", "vehicle_voucher_by_id")
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_by_id")
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
        Car_seal_code= comm.get_parameter_from_redis("car_seal_code")
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
        res = requests.post(url=url, headers=header, json=data, verify=False)
        # num_now = int(num)+1
        # if isinstance(num_now, int):
        #     logging.info("封车码写入成功")
        #     value_new = "p" + str(num_now)
        #     write_config_ini(file_name="car_seal_code", section="seal_code", option="code", value=value_new)
        # else:
        #     logging.info("风车码写入失败")

        logging.info("车辆出港接口返回:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()


