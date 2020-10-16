
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


@allure.feature('拆包by')
class Test_unpack_by(object):

    @pytest.mark.run(order=79)
    def test_test_unpack_by(self):

        comm = Common_data()
        pno_list = []
        true = True
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/unseal"
        session_id = comm.get_parameter_from_redis('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')

        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        pack_num = comm.get_parameter_from_redis("pack_no")
        # 修改 list_i
        list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in range(len(list_i)):
            pno = read_request_data("courier_pno_number" + str(i + 18))
            pno_list.append(pno)
        logging.info("订单号读取结果是：")
        logging.info(pno_list)

        data = {
            "continue_flag": true,
            # "pack_no": "P5712",
            "pack_no": pack_num,
            "recent_pnos": pno_list
        }
        unpack = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("拆包接口响应结果是:")
        logging.info(unpack.json())
        assert_that(unpack.json()["code"]).is_equal_to(1)
        assert_that(unpack.json()["message"]).is_equal_to("success")
        assert_that(unpack.json()["data"]).is_none()
        
        # logging.info("jsonschema文件path:../data/jsonschema/79unpack_by.json")
        # with open("../data/jsonschema/79unpack_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = unpack.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        