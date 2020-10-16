import random
import sys, os

from common.readconfig import ReadConfig

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


@allure.feature('711')
class Test_callback_speed_d_orders(object):
    @pytest.mark.run(order=1)
    def test_test_callback_speed_d_orders(self):
        baseTest = BaseTestCase()
        readConfigObj = ReadConfig()
        redisObj = RedisBase()
        env = redisObj.get("runenv_py")
        if env is False:
            env = "trunk"
        print("当前环境是：{0}".format(env))
        if env == "trunk":
            headers_trunk = {
                "Accept-Language": "zh-CN",
                "Content-Type": "application/json",
                "X-SPEED-D-ID": "AA0396"
            }
            consignment_trunk = random.randint(0000000000, 9999999999999)
            parameter_trunk = {
                "consignment": "{}".format(consignment_trunk),
                "brand": "Speed-D",
                "orderReceivedAt": "2019-04-27T09:53:11.598Z",
                "parcelSizeId": "SATCHEL",
                "sender": {
                    "name": "น.ส. จังคนิภา บุตโรบล",
                    "phone": "0944839133",
                    "shopCode": "123",
                    "shopType": "N01",
                    "shopName": "ceshi",
                    "address": "สาขา สนง.การนิคม ลาดกระบัง (03317) – ซ.ฉลองกรุง 31 แขวงลำปลาทิว เขตลาดกระบัง กรุงเทพมหานคร",
                    "subdistrict": "ลำปลาทิว",
                    "district": "ลาดกระบัง",
                    "city": "กรุงเทพมหานคร",
                    "postcode": "10520",
                    "lat": 16.757965051246175,
                    "lng": 80.78965782265044,
                    "cutoffDateTime": "2018-12-12T21:00:00Z",
                    "shopAvailable": "เปิด 24 ชม."
                },
                "recipient": {
                    "name": "",
                    "phone": "1234561231",
                    "shopCode": "",
                    "shopType": "",
                    "shopName": "",
                    "address": "",
                    "subdistrict": "",
                    "district": "",
                    "city": "",
                    "postcode": "10520",
                    "shopAvailable": ""
                },
                "C2Ccode": "{}".format(consignment_trunk),
                "shopCode": "1",
                "recipientShopCode": ""
            }
            host_speed_d_trunk = readConfigObj.get_config(env, "common_host")
            url_speed_d_trunk = "{}/callback/speed_d/orders".format(host_speed_d_trunk)
            print("请求地址是：\n%s" % url_speed_d_trunk)
            print("请求头是：\n%s" % headers_trunk)
            print("请求参数是：\n%s" % parameter_trunk)
            resp = requests.post(url=url_speed_d_trunk, headers=headers_trunk, json=parameter_trunk)
            print("响应结果日志信息: \n%s" % resp.json())

            assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
            assert_that(resp.status_code).is_equal_to(201)
            if "zh" in eval(str(headers_trunk))["Accept-Language"].lower():
                assert_that(resp.json()["message"]).is_equal_to("Create order success")
            elif "th" in eval(str(headers_trunk))["Accept-Language"].lower():
                assert_that(resp.json()["message"]).is_equal_to("Create order success")
            elif "en" in eval(str(headers_trunk))["Accept-Language"].lower():
                assert_that(resp.json()["message"]).is_equal_to("Create order success")
        if env == "training":
            headers_training = {
                "Accept-Language": "zh-CN",
                "Content-Type": "application/json",
                "X-SPEED-D-ID": "AA0109"
            }
            consignment_training = random.randint(0000000000, 9999999999999)
            parameter_training = {
                "consignment": "{}".format(consignment_training),
                "brand": "Speed-D",
                "orderReceivedAt": "2019-04-27T09:53:11.598Z",
                "parcelSizeId": "SATCHEL",
                "sender": {
                    "name": "น.ส. จังคนิภา บุตโรบล",
                    "phone": "0944839133",
                    "shopCode": "123",
                    "shopType": "N01",
                    "shopName": "ceshi",
                    "address": "สาขา สนง.การนิคม ลาดกระบัง (03317) – ซ.ฉลองกรุง 31 แขวงลำปลาทิว เขตลาดกระบัง กรุงเทพมหานคร",
                    "subdistrict": "ลำปลาทิว",
                    "district": "ลาดกระบัง",
                    "city": "กรุงเทพมหานคร",
                    "postcode": "10520",
                    "lat": 16.757965051246175,
                    "lng": 80.78965782265044,
                    "cutoffDateTime": "2018-12-12T21:00:00Z",
                    "shopAvailable": "เปิด 24 ชม."
                },
                "recipient": {
                    "name": "",
                    "phone": "1234561231",
                    "shopCode": "",
                    "shopType": "",
                    "shopName": "",
                    "address": "",
                    "subdistrict": "",
                    "district": "",
                    "city": "",
                    "postcode": "10520",
                    "shopAvailable": ""
                },
                "C2Ccode": "{}".format(consignment_training),
                "shopCode": "1",
                "recipientShopCode": ""
            }
            host_speed_d_training = readConfigObj.get_config(env, "common_host")
            url_speed_d_training = "{}/callback/speed_d/orders".format(host_speed_d_training)
            print("请求地址是：\n%s" % url_speed_d_training)
            print("请求头是：\n%s" % headers_training)
            print("请求参数是：\n%s" % parameter_training)
            resp = requests.post(url=url_speed_d_training, headers=headers_training, json=parameter_training)
            print("响应结果日志信息: \n%s" % resp.json())

            assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
            print(id(resp.status_code))
            print(id("201"))
            assert_that(resp.status_code).is_equal_to(201)

            if "zh" in eval(str(headers_training))["Accept-Language"].lower():
                assert_that(resp.json()["message"]).is_equal_to("Create order success")
            elif "th" in eval(str(headers_training))["Accept-Language"].lower():
                assert_that(resp.json()["message"]).is_equal_to("Create order success")
            elif "en" in eval(str(headers_training))["Accept-Language"].lower():
                assert_that(resp.json()["message"]).is_equal_to("Create order success")
