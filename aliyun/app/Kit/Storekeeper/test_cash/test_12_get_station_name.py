
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


@allure.feature('获取站名')
class Test_get_station_name(object):

    @pytest.mark.run(order=12)
    def test_test_get_station_name(self):
        comm = Common_data()
        host = comm.each_parameter("host_10000")
        # session = read_session_10000("ms_10000", "ms_session")
        session = comm.get_parameter_from_redis('ms_login_10000_0_0_0_["data"]["session_id"]')
        header = {
            # "X-MS-SESSION-ID": "1589437386_e231ab71d33749205743fcc8bf0933e1e9d0cc80184ecaeeaa4525a7165d139f_10000",
            "X-MS-SESSION-ID": session,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN"
        }
        url = host + "ms/api/setting/store/manager/van/line"

        resp = requests.get(url=url, headers=header, verify=False)
        # 获取第一个站名ID 和第二个站名ID，存储到配置文件中
        logging.info(resp.json())
        # id_1 = resp.json()["data"]返回一个数组
        items = resp.json()["data"]
        for item in items:
            logging.info(item)
        logging.info("all datas")
        logging.info(items)
        # 从env中获取第一个站点名称，再根据站点名称，去获取ID
        name = comm.each_parameter("station_name")
        for item in items:
            if item["name"] == name:
                id_1 = item["id"]

        id_2 = resp.json()["data"][1]["id"]
        comm.write_parameter_to_redis("id_1", id_1)
        comm.write_parameter_to_redis("id_2", id_2)
        assert_that(resp.json()["code"]).is_equal_to(1)
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.json()["data"]).is_not_empty()


        # logging.info("jsonschema文件path:../data/jsonschema/11get_plate_number.json")
        # with open("../data/jsonschema/12get_station_name.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()