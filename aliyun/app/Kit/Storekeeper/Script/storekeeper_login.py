import configparser
import logging
import os

import requests

# from Courier.Utils.read_common import read_common

#仓管员登入
# from app.kit.Courier.Utils.read_common import read_common
# from app.kit.Util.common_data import Common_data
from app.Kit.Util.common_data import Common_data


class Storekeeper_Login():
    logging.basicConfig(level=logging.INFO)
    def storekeeper_login(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/auth/new_device_login"
        header = {
            "Content-Type": "application/json"
        }

        # user = read_common("Storekeeper_login_user")
        user = comm.each_parameter("Storekeeper_login_user")
        # pwd = read_common("Storekeeper_login_pwd")
        pwd = comm.each_parameter("Storekeeper_login_pwd")
        # version = read_common("login_version")
        version = comm.each_parameter("login_version")
        data = {
            "login": user,
            "password": pwd,
            "clientid": "8698940239062391583120286987",
            "clientsd": "1583120286995",
            "os": "android",
            "version": version
            # "version": "3.6.7"

        }
        resp = requests.post(url=url, json=data, headers=header, verify=False)
        print(resp.json())

        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # print(curpath)
        # session_path = curpath + "/conf/storekeeper_session_id.ini"
        #
        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/storekeeper_session_id.ini")
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/storekeeper_session_id.ini"
        #
        # storekeeper_session_id = resp.json()["data"]["sessionid"]
        # print(storekeeper_session_id)
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("storekeeper_session")
        # cf.set("storekeeper_session", option="session_id", value=str(storekeeper_session_id))
        # with open(session_path, "w+") as f:
        #     if str(storekeeper_session_id).startswith("1"):
        #         logging.info("仓管员session信息开始写入")
        #         cf.write(f)
        #         logging.info("仓管员session信息写入成功")
        #         logging.info("仓管员session信息是：")
        #         logging.info(storekeeper_session_id)

        Common_data().write_parameter_to_redis("storekeeper_session", resp.json()["data"]["sessionid"])
        return resp.json()
