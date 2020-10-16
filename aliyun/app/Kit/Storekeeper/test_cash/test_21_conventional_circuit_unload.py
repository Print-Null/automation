
import sys,os

from app.Kit.Util.common_data import Common_data

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0]+"/flash")
import allure
from assertpy import assert_that
import requests
import logging
import ast
import json
import time
import pytest
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
                
logging.basicConfig(level=logging.INFO)


@allure.feature('常规线路解车')
class Test_conventional_circuit_unload(object):

    @pytest.mark.parametrize("parameter",["{'fleet_bound_images': [{'sealing_number': '$car_seal_code$'}], 'inbound_unusual_images': [], 'outbound_autograhph_image': {'image_key': 'fleetOutboundAutograph/1591255915-003ba372edb6484a825772c4cdc8dd84.jpg', 'image_name': 'fleetOutboundAutograph/1591255915-003ba372edb6484a825772c4cdc8dd84.jpg'}, 'remark': '', 'sealing_enabled': False}"])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$storekeeper_login_0_2_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\'}', '{\'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$storekeeper_login_0_2_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\'}', '{\'Accept-Language\': \'th-CN\', \'X-FLE-SESSION-ID\': \'$storekeeper_login_0_2_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/fleet/proof/inbound/unload/$vehicle_voucher_id$'])
    @pytest.mark.run(order=21)
    def test_test_conventional_circuit_unload(self, parameter,headers,address):
        false = False
        comm = Common_data()
        host = comm.each_parameter("host")
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_id")

        url = host + "api/courier/v1/fleet/proof/inbound/unload/%s" % conventional_circuit_id
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        Car_seal_code = comm.get_parameter_from_redis("car_seal_code")
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

        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info(res.json())
        assert_that(res.status_code).is_equal_to(200)
        assert_that(res.json()["code"]).is_equal_to(1)
        # logging.info("jsonschema文件path:../data/jsonschema/21conventional_circuit_unload.json")
        # with open("../data/jsonschema/21conventional_circuit_unload.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = res.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()










