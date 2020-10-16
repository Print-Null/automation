import configparser
import logging
import os

import requests

# from app.kit.Util.common_data import Common_data

#10000号登入
from app.Kit.Util.common_data import Common_data


class Login_10000():
    #
    logging.basicConfig(level=logging.INFO)
    def login_10000(self):
        comm = Common_data()
        host = comm.each_parameter("host_10000")
        url = host + "ms/api/auth/signin"
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "zh-CN"
        }
        usr = comm.each_parameter("login_usr_10000")
        pwd = comm.each_parameter("login_pwd_10000")
        data = {
            # "login": "10000",
            "login": usr,
            # "password": "123456"
            "password": pwd
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info(resp.json())
        #获取sessionid 存储到.ini文件中
        session = resp.json()["data"]["session_id"]
        comm.write_parameter_to_redis("login_10000",session)
        #
        # # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # # session_path = curpath + "/conf/session_10000.ini"
        #
        # # session_path = os.path.join(os.path.abspath(
        # #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        # #     "conf/session_10000.ini")
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/session_10000.ini"
        #
        #
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("ms_10000")
        # cf.set("ms_10000", option="ms_session", value=str(session))
        # with open(session_path, "w+") as f:
        #     if str(session).startswith("1"):
        #         logging.info("后台10000号，session信息开始写入")
        #         cf.write(f)
        #         logging.info("后台10000号,session信息写入成功")
        #         logging.info("后台10000号，session信息是：")
        #         logging.info(session)

        return resp