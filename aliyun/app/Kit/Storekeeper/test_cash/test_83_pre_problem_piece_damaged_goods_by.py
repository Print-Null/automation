
import sys,os

from app.Kit.Courier.Utils.read_request_data import read_request_data
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


@allure.feature('交接前，问题件提交，货物破损')
class Test_pre_problem_piece_damaged_goods_by(object):

    @pytest.mark.run(order=83)
    def test_test_pre_problem_piece_damaged_goods_by(self):
        comm = Common_data()
        session_id = comm.get_parameter_from_redis('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')
        host = comm.each_parameter("host")
        pno = read_request_data("courier_pno_number21")
        url = host + "api/courier/v1/parcels/" + pno + "/problem_submission"

        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        ti = int(time.time())
        data = {
            "difficulty_marker_category": 20,
            "image_keys": [
                "difficulty/" + str(ti) + "-0e0d9fc03a3f40028bd582cc709dcdb2.jpg"
            ],
            "remark": "货物破损"
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("交接前，问题件提交，货物破损,响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()

        
        # logging.info("jsonschema文件path:../data/jsonschema/83pre_problem_piece_damaged_goods_by.json")
        # with open("../data/jsonschema/83pre_problem_piece_damaged_goods_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = res.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        