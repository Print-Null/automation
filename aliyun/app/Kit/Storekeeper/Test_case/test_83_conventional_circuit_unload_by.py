import logging
import allure
import pytest
import requests
from assertpy import assert_that
# from app.Kit.Storekeeper.utils.read_config_ini import read_config_ini
# from app.Kit.Storekeeper.utils.read_ini_file_all import read_all_ini
from app.Kit.Util.common_data import Common_data


@allure.feature("常规线路解车by")
class Test_Conventional_Circuit_Unload_By():
    logging.basicConfig(level=logging.INFO)

    @allure.story("常规线路解车by")
    @pytest.mark.run(order=84)
    def test_conventional_circuit_unload_by(self):
        false = False
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/fleet/proof/inbound/unload/BKK3A3172"
        # conventional_circuit_id = read_vehicle_voucher("vehicle_voucher", "vehicle_voucher_id")  # 出车凭证码
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_by_id")
        # conventional_circuit_id = read_all_ini("all_data", "vehicle_voucher_by", "vehicle_voucher_by_id")
        url = host + "api/courier/v1/fleet/proof/inbound/unload/%s" % conventional_circuit_id
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # num_read = read_config_ini(file_name="car_seal_code", sections="seal_code", option="code")  # 封车码p1000000012
        # num = num_read.split("p")[1]
        # num_new = int(num) - 1
        # Car_seal_code = "p" + str(num_new)
        Car_seal_code = comm.get_parameter_from_redis("car_seal_code")
        # data = {
        #     "fleet_bound_images": [
        #         {
        #             "image_url": "fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg",
        #             # "img": "https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg",
        #             # "img": "fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg",
        #             # "img": "1591255219-1617ba71ffca40b183d0d7c2e26b419c.jpg",
        #             "sealing_number": str(Car_seal_code)
        #             # "sealing_number": "p1000000012"
        #         }
        #     ],
        #     "outbound_image": {
        #         "image_key": "fleetOutboundAutograph/1591255219-1617ba71ffca40b183d0d7c2e26b419c.jpg",
        #         "image_name": "1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg"
        #     }
        # }
        data = {
            "fleet_bound_images": [
                {
                    "sealing_number": str(Car_seal_code)
                }
            ],
            "inbound_unusual_images": [],
            "outbound_autograhph_image": {
                "image_key": "fleetOutboundAutograph/1591255915-003ba372edb6484a825772c4cdc8dd84.jpg",
                "image_name": "fleetOutboundAutograph/1591255915-003ba372edb6484a825772c4cdc8dd84.jpg"
            },
            "remark": "",
            "sealing_enabled": false
        }
        logging.info("请求参数是：")
        logging.info(data)
        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("常规线路解车, 响应结果是:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()

