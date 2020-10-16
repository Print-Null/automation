import random
import sys, os

from app.Kit.Util.common_data import Common_data

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")
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


@allure.feature('车辆出港接口')
class Test_vehicle_departure(object):

    @allure.story("车辆出港功能")
    @pytest.mark.run(order=19)
    def test_test_vehicle_departure(self):
        comm = Common_data()
        host = comm.each_parameter("host")
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_id")
        url = host + "api/courier/v1/fleet/proof/outbound/new/%s" % conventional_circuit_id
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        Car_seal_code = "p" + str(random.randint(1000000012, 9999999999))
        data = {
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
        logging.info(resp.json())
        comm.write_parameter_to_redis("car_seal_code", Car_seal_code)
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        # logging.info("jsonschema文件path:../data/jsonschema/19vehicle_departure.json")
        # with open("../data/jsonschema/19vehicle_departure.json", "r", encoding="utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance=resp.json(), schema=shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
