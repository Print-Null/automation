import configparser
import logging
import os
import random

import requests
from ruamel import yaml
from app.Kit.Util.common_data import Common_data

logging.basicConfig(level=logging.INFO)
class Login():

    def login(self):

        comm = Common_data()
        host = comm.each_parameter("host")
        # host = read_common("host")
        url = host + "api/courier/v1/auth/new_device_login"
        header={
            "Content-Type":"application/json"
        }

        # user = read_common("courier_login_user")
        user = comm.each_parameter("courier_login_user")

        # pwd = read_common("courier_login_password")
        pwd = comm.each_parameter("courier_login_password")
        # version = read_common("login_version")
        version = comm.each_parameter("login_version")


        data = {
                "login": user,
                "password": pwd,
                "clientid": "8698940239062391583120286987",
                "clientsd": "1583120286995",
                "os": "android",
                 # "version": "3.6.7"
                 "version": version

            }
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        print(resp.json())
        logging.info(data)

        #将sessionID存到redis
        Common_data().write_parameter_to_redis("session_id",resp.json()["data"]["sessionid"])







        # # 快递员session_id 写入文件
        # session_id = {
        #     "courier_session_id": resp.json()["data"]["sessionid"]
        # }
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # yamlpath = root_path + "/app/Kit/Courier/Config/session_courier.yaml"
        # # 写入到yaml文件
        # with open(yamlpath, 'w+', encoding="utf-8") as f:
        #     yaml.dump(session_id, f, Dumper=yaml.RoundTripDumper)
        #     logging.info("快递员session_id写入文件成功")
        #


        # #每次运行前，清空request_data中的旧的订单数据
        # cf = configparser.ConfigParser()
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # requests_data_clear = root_path + "/app/Kit/Courier/Config/request_data.ini"
        #
        # cf.clear()
        # cf.write(open(requests_data_clear, "w+"))
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # pack_number_path = root_path + "/app/Kit/Storekeeper/conf/pack_number.ini"
        #
        #
        # #pack_number.ini随机数
        #
        # cf = configparser.ConfigParser()
        # # session = random.randint(100,9999,1)
        # session = random.randint(100, 9999)
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("pack_no")
        # cf.set("pack_no", option="pack_num", value=str(session))
        # with open(pack_number_path, "w+") as f:
        #     cf.write(f)
        # #car_seal_code.ini code = p1000000256
        # # car_seal_code = curpath + "/conf/car_seal_code.ini"
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # car_seal_code = root_path + "/app/Kit/Storekeeper/conf/car_seal_code.ini"
        #
        # # car_seal_code = curpath
        # cf = configparser.ConfigParser()
        # # session = random.randint(100,9999,1)
        # num = random.randint(1000000000, 9999999999)
        # sessioncar_seal_code = "p" + str(num)
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("seal_code")
        # cf.set("seal_code", option="code", value=str(sessioncar_seal_code))
        # with open(car_seal_code, "w+") as f:
        #     cf.write(f)
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # pickup_id_path = root_path + "/app/Kit/Courier/Config/order_type_all.txt"
        # with open(pickup_id_path, 'w') as f:
        #     f.write("")
        #



        return resp.json()

