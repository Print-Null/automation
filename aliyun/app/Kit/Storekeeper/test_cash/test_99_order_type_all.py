import json
import logging
import os
from jsonschema import validate
import allure
import pytest
import requests
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data
from utils import redisbase
from assertpy import assert_that
from utils.redisbase import RedisBase


@allure.feature("下单所有类型")
class Test_Order_Type_All():
    logging.basicConfig(level=logging.INFO)
    @pytest.mark.parametrize("article_category", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 99])
    @pytest.mark.parametrize("material_category", [(0, 500), (1, 1000), (2, 1500), (3, 2000), (4, 2500), (5, 3500), (6, 500), (7, 500)])
    @pytest.mark.parametrize("volume",
                             [(1, 1, 1), (14, 20, 6), (20, 30, 10), (17, 25, 9), (24, 37, 14), (20, 30, 11), (27, 43, 20), (22, 35, 14), (35, 45, 25), (24, 40, 17), (40, 50, 30), (30, 45, 20)])
    @pytest.mark.run(order=109)
    def test_order_type_all(self,article_category, material_category, volume):
        null = None
        self.redisObj = redisbase.RedisBase()
        self.runenv_py = self.redisObj.get("runenv_py")
        root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        pickup_id_path = root_path + "/app/Kit/Courier/Config/order_type_all.txt"
        with open(pickup_id_path, 'r') as f:
            pick_read = f.readline()
            logging.info(pick_read)

        comm = Common_data()

        # session_id = read_courier_session_id()
        # session_id = read_courier_session_id("session_id")
        session_id = read_courier_session_id('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')
        false = False
        true = True
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/ticket/pickups/parcel"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8626360321249741583752305908",
            "X-FLE-EQUIPMENT-TYPE": "kit",
            "Content-Type": "application/json; charset=UTF-8"
        }
        client_id = comm.each_parameter("client_id")
        data = {
            "addr_core_ids": [],
            "article_category": article_category,
            "call_duration": 0,
            "client_id": client_id,
            "cod_amount": 0,
            "cod_enabled": false,
            "customer_type_category": 2,
            "dst_city_code": "TH0101",
            "dst_country_code": "TH",
            "dst_detail_address": "自动化收件地址",
            "dst_district_code": "TH010103",
            "dst_name": "自动化收件",
            "dst_phone": "1232311233",
            "dst_postal_code": "10260",
            "dst_province_code": "TH01",
            "express_category": 1,
            "freight_insure_enabled": false,
            "height": volume[2],
            "insure_declare_value": 0,
            "insured": false,
            "length": volume[0],
            "material_amount": material_category[1],
            "material_category": material_category[0],
            "request_ids": [],
            "settlement_category": 1,
            "skipping_tips": [],
            "src_city_code": "TH0101",
            "src_country_code": "TH",
            "src_detail_address": "自动化寄件地址",
            "src_district_code": "TH010103",
            "src_name": "自动化寄件",
            "src_phone": "1232311230",
            "src_postal_code": "10110",
            "src_province_code": "TH01",
            "total_amount": 3500,
            "weight": 2000,
            "width": volume[1]
        }
        # data = {
        #     "addr_core_ids": [],
        #     "article_category": article_category,
        #     "call_duration": 0,
        #     # "client_id": "CA0546",
        #     "client_id": client_id,
        #     "cod_amount": 3400,
        #     "cod_enabled": true,
        #     "customer_type_category": 2,
        #     "dst_city_code": "TH0101",
        #     "dst_country_code": "TH",
        #     "dst_detail_address": "自动化收件地址",
        #     "dst_district_code": "TH010101",
        #     "dst_name": "自动化收件",
        #     "dst_phone": "1232311234",
        #     "dst_postal_code": "10111",
        #     "dst_province_code": "TH01",
        #     "express_category": 1,
        #     "freight_insure_enabled": false,
        #     "height": volume[2],
        #     "insure_declare_value": 0,
        #     "insured": false,
        #     "length": volume[0],
        #     "material_amount": material_category[1],
        #     "material_category": material_category[0],
        #     "request_ids": [],
        #     "settlement_category": 1,
        #     "skipping_tips": [],
        #     "src_city_code": "TH0101",
        #     "src_country_code": "TH",
        #     "src_detail_address": "自动化寄件地址",
        #     "src_district_code": "TH010101",
        #     "src_name": "自动化寄件",
        #     "src_phone": "1232311230",
        #     "src_postal_code": "10110",
        #     "src_province_code": "TH01",
        #     "total_amount": 1500,
        #     "weight": 2000,
        #     "width": volume[1]
        # }
        data_tra = {
            "customer_type_category": 2,
            "client_id": client_id,
            # "client_id": "BA0020",
            "freight_insure_enabled": false,
            "insured": false,
            "insure_declare_value": 0,
            "insure_amount": 0,
            "cod_amount": null,
            "cod_enabled": false,
            "express_category": 1,
            "article_category": 1,
            "material_category": material_category[0],
            "material_amount": material_category[1],
            "src_name": "0967484061",
            "src_phone": "0967484061",
            "src_province_code": "TH01",
            "src_city_code": "TH0101",
            "src_district_code": "TH010101",
            "src_postal_code": "10110",
            "src_detail_address": "0967484061",
            "dst_name": "0967484061",
            "dst_phone": "0967484061",
            "ka_warehouse_id": null,
            "dst_province_code": "TH01",
            "dst_city_code": "TH0105",
            "dst_district_code": "TH010502",
            "dst_postal_code": "10900",
            "dst_detail_address": "0967484061",
            "total_amount": 34650,
            "settlement_category": 1,
            "weight": 25000,
            "length": volume[0],
            "width": volume[1],
            "height": volume[2],
            "skipping_tips": [],
            "request_ids": ["ef9994b589464d7aac34fe81697602ad"]
            }
        # data_tra = {
        #     "addr_core_ids": [],
        #     "article_category": 1,
        #     "call_duration": 0,
        #     # "client_id": "CA0609",
        #     "client_id": client_id,
        #     "cod_amount": 3000,
        #     "cod_enabled": false,
        #     "customer_type_category": 2,
        #     "dst_city_code": "TH2001",
        #     "dst_country_code": "TH",
        #     "dst_detail_address": "1修改测试",
        #     "dst_district_code": "TH200101",
        #     "dst_name": "1",
        #     "dst_phone": "1346999281",
        #     "dst_postal_code": "20000",
        #     "dst_province_code": "TH20",
        #     "express_category": 2,
        #     "freight_insure_enabled": false,
        #     "height": volume[2],
        #     "insure_declare_value": 0,
        #     "insured": false,
        #     "length": volume[0],
        #     "material_amount": material_category[1],
        #     "material_category": material_category[0],
        #     "request_ids": [],
        #     "settlement_category": 1,
        #     "skipping_tips": [],
        #     "src_city_code": "TH0101",
        #     "src_country_code": "TH",
        #     "src_detail_address": "1",
        #     "src_district_code": "TH010101",
        #     "src_name": "1",
        #     "src_phone": "1232311232",
        #     "src_postal_code": "10110",
        #     "src_province_code": "TH01",
        #     "total_amount": 1500,
        #     "weight": 2000,
        #     "width": volume[1]
        # }
        if self.runenv_py == 'trunk':
            res = requests.post(url=url, headers=header, json=data, verify=False)
            logging.info("测试环境填单接口返回的结果是：")
            logging.info(res.json())
            logging.info("测试环境请求url:")
            logging.info(url)
            logging.info("测试环境请求参数")
            logging.info(data)
            logging.info("测试环境请求header")
            logging.info(header)

            ticket_pickup_id = res.json()["data"]["ticket_pickup_id"]

            logging.info("aaaaaa")
            logging.info(ticket_pickup_id)
            # # pick_read.append(ticket_pickup_id)
            # with open(pickup_id_path, 'w') as f:
            #     f.write("")
            # pick_read = pick_read + str(ticket_pickup_id) + ","
            # with open(pickup_id_path, 'a+') as f:
            #     f.write(pick_read)
            # RedisBase().set("ticket_pickup_id", str(ticket_pickup_id) + ",", ex=6000)
            # self.redisObj.set("ticket_pickup_id", str(ticket_pickup_id) + ",", ex=6000)
            # comm.append_data("ticket_pickup_id_{0}".format(self.runenv_py), str(ticket_pickup_id) + ",")
            comm.append_data("ticket_pickup_id", str(ticket_pickup_id) + ",")
        elif self.runenv_py == 'training':
            res_tra = requests.post(url=url, headers=header, json=data_tra, verify=False)
            logging.info("预发布填单接口返回的结果是：")
            logging.info(res_tra.json())
            logging.info("预发布请求url:")
            logging.info(url)
            logging.info("预发布请求参数")
            logging.info(data_tra)
            logging.info("预发布请求header")
            logging.info(header)
            ticket_pickup_id = res_tra.json()["data"]["ticket_pickup_id"]
            logging.info("aaaaaa")
            logging.info(ticket_pickup_id)
            # comm.append_data("ticket_pickup_id", ticket_pickup_id)
            # RedisBase().set("ticket_pickup_id", str(ticket_pickup_id) + ",", ex=6000)
            # self.redisObj.set("ticket_pickup_id", str(ticket_pickup_id) + ",", ex=6000)
            # comm.append_data("ticket_pickup_id_{0}".format(self.runenv_py), str(ticket_pickup_id) + ",")
            comm.append_data("ticket_pickup_id", str(ticket_pickup_id) + ",")
            # # pick_read.append(ticket_pickup_id)
            # with open(pickup_id_path, 'w') as f:
            #     f.write("")
            # pick_read = pick_read + str(ticket_pickup_id) + ","
            # with open(pickup_id_path, 'a+') as f:
            #     f.write(pick_read)
            # logging.info("jsonschema文件path:../data/jsonschema/99_order_type_all.json")
            # with open("../data/jsonschema/99_order_type_all.json", "r", encoding="utf-8") as f:
            #     shcema = json.load(f)
            #     res = validate(instance=res_tra.json(), schema=shcema)
            #     logging.info("jsonschema验证结果是： " + str(res))
            # assert_that(res).is_none()


