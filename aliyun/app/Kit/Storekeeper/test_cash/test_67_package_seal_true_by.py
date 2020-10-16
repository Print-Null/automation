import random
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


@allure.feature('集包接口-集包成功')
class Test_package_seal_true_by(object):


    @allure.story("集包功能->集包成功")
    @pytest.mark.run(order=67)
    def test_test_package_seal_true_by(self):

        comm = Common_data()
        pno_list = []
        true = True
        false = False
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/seal"
        session_id = comm.get_parameter_from_redis('storekeeper_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # 修改 list_i
        list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in range(len(list_i)):
            # pno = read_request_data("courier_pno_number"+str(i+18), "pno"+str(i+18))
            pno = read_request_data("courier_pno_number" + str(i + 18))
            pno_list.append(pno)

        logging.info("订单号读取结果是：")
        logging.info(pno_list)
        pack_no = "p" + str(random.randint(1000, 9999))
        logging.info("集包号生成结果是：")
        logging.info(pack_no)

        data = {
            "direction_store_code": "C",
            "pack_category": 1,
            # "pack_no": "p5041",
            "pack_no": pack_no,
            "recent_pnos":
                pno_list,
            "valid_parcel": true
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info(resp.json())
        # 集包检查 设置为false

        list_i_F = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in range(len(list_i_F)):
            # pno_F = read_request_data("courier_pno_number"+str(i+18), "pno"+str(i+18))
            pno_F = read_request_data("courier_pno_number" + str(i + 18))
            pno_list.append(pno_F)
        logging.info("订单号读取结果是：")
        logging.info(pno_list)
        logging.info("集包号读取结果是：")
        logging.info(pack_no)

        data1 = {
            "direction_store_code": "C",
            "pack_category": 1,
            # "pack_no": "p5041",
            "pack_no": pack_no,
            "recent_pnos":
                pno_list,
            "valid_parcel": false
        }
        resp1 = requests.post(url=url, headers=header, json=data1, verify=False)
        logging.info(resp1.json())
        comm.write_parameter_to_redis("pack_no", pack_no)
        # return resp.json(), resp1.json()

        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["data"]).is_none()

        assert_that(resp1.json()["code"]).is_equal_to(1)
        assert_that(resp1.json()["message"]).is_equal_to("success")
        assert_that(resp1.json()["data"]).is_none()
        # logging.info("jsonschema文件path:../data/jsonschema/67package_seal_true_by.json")
        # with open("../data/jsonschema/67package_seal_true_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()












