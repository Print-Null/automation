
import sys,os
sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0]+"/flash")

import allure
from assertpy import assert_that
import requests
import logging
import ast
import json
import time
import pytest
import configparser
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
from common.readconfig import ReadConfig
logging.basicConfig(level=logging.INFO)
cf = configparser.ConfigParser()


@allure.feature('kit-清理数据')
class Test_kit_auth_new_device_login(object):

    @pytest.mark.run(order=43)
    def test_restet_datas(self):
        print("开始执行用例清理操作操作")
        redisObj = RedisBase()
        readConfigObj = ReadConfig()
        env = redisObj.get("runenv_py")
        if env == False or env == "trunk":
            env = "trunk"
        elif env == "training":
            env = "training"
        print("当前环境是：{0}".format(env))

        # 仓管员
        warehouse_keeper_login =  RedisBase().get('warehouse_keeper_login')

        # kit-host地址
        kit_host = readConfigObj.get_config(env, "kit_host")
        #快递员
        my_public_funds_courier_login =  RedisBase().get('my_public_funds_courier_login')
        my_public_funds_courier_pwd=readConfigObj.get_config(env,"my_public_funds_courier_pwd")
        my_public_funds_courier_clientid=readConfigObj.get_config(env,"my_public_funds_courier_clientid")
        my_public_funds_courier_clientsd=readConfigObj.get_config(env,"my_public_funds_courier_clientsd")
        my_public_funds_courier_os=readConfigObj.get_config(env,"my_public_funds_courier_os")
        my_public_funds_courier_version=readConfigObj.get_config(env,"my_public_funds_courier_version")

        # 一键揽收完成的脚本
        import requests
        # 登录kit的账号
        for login_id in {my_public_funds_courier_login, warehouse_keeper_login}:
            print("开始执行{0}账号的清理工作".format(login_id))
            url_login = "{0}api/courier/v1/auth/new_device_login".format(kit_host)
            headers_login = {'content-type': 'application/json; charset=UTF-8', 'Accept-Language': 'zh-CN'}
            data_login = {'login': login_id, 'password': my_public_funds_courier_pwd, 'clientid': my_public_funds_courier_clientid,'clientsd': my_public_funds_courier_clientsd, 'os': my_public_funds_courier_os, 'version': my_public_funds_courier_version}
            sessionid = requests.post(url=url_login, json=data_login, headers=headers_login, verify=False).json()['data']['sessionid']

            url_get_ticket = "{0}api/courier/v1/ticket/simplified_list?abnormal_state=2".format(kit_host)
            header = {"Accept-Language": "zh-CN", "X-FLE-SESSION-ID": sessionid}
            req_ticket = requests.get(url=url_get_ticket, headers=header, verify=False)
            pickups_list = req_ticket.json()["data"]["pickup"]
            delivered_list = req_ticket.json()["data"]["delivery"]
            for i in pickups_list:
                id = i["id"]
                if i["state"] == 1:
                    url_pickup_1 = "{0}api/courier/v1/ticket/{1}".format(kit_host,id)
                    requests.post(url=url_pickup_1, headers=header, verify=False)
                    url_pickup_2 = "{0}api/courier/v1/message/pickupReward/{1}".format(kit_host,id)
                    requests.post(url=url_pickup_2, headers=header, verify=False)
                    print("订单{0}的包裹已揽收".format(id))
                else:
                    break

            # 处理未妥投的
            for i in delivered_list:
                # state=0是需要妥投的数据
                if i["state"] == 0:
                    url_delivered = "{0}api/courier/v1/ticket/parcels/{1}/delivery_confirm".format(kit_host,i["pno"])
                    header = {"Accept-Language": "zh-CN", "X-FLE-SESSION-ID": sessionid}
                    data_delivered = {'signer_category': 1,'sign_image_key': 'deliveryPickupsMarkUpload/1554113259-2ee455ae43ac41208ae7a6396f462e15','signer_content': 'abcdefg', 'call_duration': 200}
                    requests.post(url=url_delivered, json=data_delivered, headers=header, verify=False)
                    print("订单{0}妥投完成！".format(i["pno"]))
                elif i["state"] == 1:
                    pass
            print("{0}账号的清理工作完成".format(login_id))