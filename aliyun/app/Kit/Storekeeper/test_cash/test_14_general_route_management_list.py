import datetime
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


@allure.feature('常规线路管理列表')
class Test_general_route_management_list(object):


    @pytest.mark.run(order=14)
    def test_test_general_route_management_list(self):
        null = None
        comm = Common_data()
        host = comm.each_parameter("host_10000")
        url = host + "ms/api/fleet/van/line?sortingNo=&type=&originStoreId=&targetStoreId=&lineName=&pageSize=100&pageNum=1&passStoreId="
        # session = read_session_10000("ms_10000", "ms_session")
        session = comm.get_parameter_from_redis('ms_login_10000_0_0_0_["data"]["session_id"]')
        header = {
            # "X-MS-SESSION-ID": "1589437386_e231ab71d33749205743fcc8bf0933e1e9d0cc80184ecaeeaa4525a7165d139f_10000",
            "X-MS-SESSION-ID": session,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN"
        }
        res = requests.get(url=url, headers=header, verify=False)
        logging.info("响应结果是：")
        logging.info(res.json())
        logging.info("请求头是：")
        logging.info(header)
        logging.info("请求url是：")
        logging.info(url)
        data_item = res.json()["data"]["items"][0]
        # logging.info(res.json())
        # 获取最新一条数据[0]
        datas = res.json()["data"]["items"][0]["time_tables"][0]["estimate_start_time"]
        logging.info(datas)
        # logging.info("datas ")
        # logging.info(datas)
        # 将以下数据保存到文件中
        '''
        {
            "id": null,
            "fleet_id": "5d2edf122d738a490871c918",
            "van_line_id": "5d1dc8642d738a29e93034e9",
            "fleet_name": "我有两个车",
            "driver": "2",
            "plate_id": "5e8759522ff36f3edb3cef8f",
            "driver_phone": "2221212121",
            "departure_time": "2020-04-17 10:35"
        }
        '''
        today = datetime.date.today()
        min = int(datas)
        hour = min // 60
        print(hour)
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = hour
        fenzhong = min % 60
        if fenzhong < 10:
            fenzhong = "0" + str(fenzhong)
        else:
            fenzhong = fenzhong
        departure_time = str(today) + " " + str(hour) + ":" + str(fenzhong)
        new_dict = {
            "id": null,
            "fleet_id": null,
            "van_line_id": data_item["id"],
            "fleet_name": null,
            "driver": null,
            "plate_id": null,
            "driver_phone": null,
            "departure_time": departure_time
        }

        comm.write_parameter_to_redis("ms_generate_vehicle_voucher_virtual", str(new_dict))
        assert_that(res.status_code).is_equal_to(200)
        assert_that(res.json()["code"]).is_equal_to(1)
        # logging.info("jsonschema文件path:../data/jsonschema/14general_route_management_list.json")
        # with open("../data/jsonschema/14general_route_management_list.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = res.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()












