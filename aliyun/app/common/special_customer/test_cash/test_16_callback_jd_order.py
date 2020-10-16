import base64
import datetime
import hashlib
import random
import sys, os
import urllib.parse

from common.readconfig import ReadConfig

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")
import allure
import requests
import logging
import json
import pytest
from utils.redisbase import RedisBase

logging.basicConfig(level=logging.INFO)


@allure.feature('jd客户下单')
class Test_callback_jd_orders(object):
    @pytest.mark.run(order=16)
    def test_test_callback_jd_orders(self):
        readConfigObj = ReadConfig()
        redisObj = RedisBase()
        env = redisObj.get("runenv_py")
        if env is False:
            env = "trunk"
        print("当前环境是：{0}".format(env))
        package_info = [
            {"packageId": str(random.randint(100000000, 999999999)),
             "weight": 5,
             "volume": "",
             "lenght": "",
             "width": "",
             "height": ""}]
        sender = {
            "name": "Bangkok Sorting",
            "mobile": "0135" + str(random.randint(100000, 999999)),
            "province": "Samut Prakan",
            "city": "Bang Phli",
            "county": "Bang Pla",
            "town": "",
            "address": "333/9-12 Moo.3Bang Sao Thong， Samut Prakan 10540",
            "zipCode": "10540"
        }
        receiver = {
            "name": "อรจิรา",
            "mobile": "0134" + str(random.randint(100000, 999999)),
            "province": "Bangkok",
            "city": "Pom Prap Sattru Phai",
            "county": "Khlong Maha Nak",
            "town": "",
            "address": "3333 Bang Khae Nuea ",
            "zipCode": "10110",
            "email": ""
        }
        order_detail = {
            "orderCreateTime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "orderType": 1,
            "gotStartTime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "gotEndTime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "goodsValue": 200,
            "totalFee": "",
            "insuranceValue": "",
            "totalServiceFee": "",
            "codSplitFee": "",
            "sch eduleType": ""
        }
        logistics_info = {
            "logisticsProviderCode": "Flash",
            "country": "th",
            "createSiteName": "BBK",
            "waybillCode": "",
            "orderId": str(random.randint(100000000, 999999999)),
            "packageInfos": package_info,
            "sender": sender,
            "receiver": receiver,
            "orderDetail": order_detail,
            "extendFields": [
                {
                    "key": "vendorId",
                    "value": "106"
                },
                {
                    "key": " serviceLevel",
                    "value": "JDExpress"
                }
            ],
            "remark": ""
        }
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        times_tamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        jd_key = "123456"
        logistics_info_str = json.dumps(logistics_info)
        # 对logisticsInfo做url_decode加密
        logistics_info_url_encode = urllib.parse.quote(logistics_info_str, encoding="utf-8")

        # 生成encrypt_data(logisticsInfo+timestamp+key的字符串先MD5加密在转换成base64的字符串在做url_encode加密)
        # 拼接签名字符串
        signature_content = logistics_info_str + times_tamp + jd_key
        # 对签名字符串做MD5加密
        md5_str = hashlib.md5()
        md5_str.update(signature_content.encode("utf-8"))
        sign_str = md5_str.hexdigest()
        # 将MD5加密字符串转成base64字符串
        base64_str = str(base64.b64encode(sign_str.encode("utf-8")), "utf-8")
        # 将base64字符串转成url_encode加密字符串
        encrypt_data = urllib.parse.quote(base64_str, encoding="utf-8")
        parameter = {
            "logistics_info": logistics_info_url_encode,
            "timestamp": times_tamp,
            "encrypt_data": encrypt_data
        }

        if env == "trunk":
            jd_host_trunk = readConfigObj.get_config(env, "common_host")
            order_url_trunk = "{}/callback/jd/order".format(jd_host_trunk)
            print("请求地址是：\n%s" % order_url_trunk)
            print("请求参数是：\n%s" % parameter)
            req = requests.post(url=order_url_trunk, headers=header, data=parameter)
            print("响应结果日志：\n%s" % req.json())

            assert req.json()["isSuccess"] is True
        if env == "training":
            jd_host_training = readConfigObj.get_config(env, "common_host")
            order_url_training = "{}/callback/jd/order".format(jd_host_training)
            print("请求地址是：\n%s" % order_url_training)
            print("请求参数是：\n%s" % parameter)
            req = requests.post(url=order_url_training, headers=header, data=parameter)
            print("响应结果日志：\n%s" % req.json())

            assert req.json()["isSuccess"] is True
