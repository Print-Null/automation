import configparser
import logging
import os

import requests
#查询公司名称
from app.Kit.Util.common_data import Common_data


class Query_Company_Name():
    logging.basicConfig(level=logging.INFO)
    def query_company_name(self):
        #
        comm = Common_data()
        host = comm.each_parameter("host_10000")
        url = host + "ms/api/fleet"
        # session = read_session_10000("ms_10000", "ms_session")
        session = comm.get_parameter_from_redis("login_10000")
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "X-MS-SESSION-ID": session,
            "Accept-Language": "zh-CN"
        }
        resp = requests.get(url=url, headers=header, verify=False)
        logging.info(url)
        #将查询到的参数，存储到配置文件中
        id = resp.json()["data"]["items"][1]["id"]
        logging.info(id)
        comm.write_parameter_to_redis("query_company_name", id)


        # # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # # session_path = curpath + "/conf/query_company_name.ini"
        #
        # # session_path = os.path.join(os.path.abspath(
        # #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        # #     "conf/query_company_name.ini")
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/query_company_name.ini"
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("query_company")
        # cf.set("query_company", option="id", value=str(id))
        # with open(session_path, "w+") as f:
        #     logging.info("后台10000号，查到公司名称接口，获取到ID信息，信息开始写入")
        #     cf.write(f)
        #     logging.info("后台10000号，查到公司名称接口，获取到ID信息，信息写入完成")
        #     logging.info(id)

        return resp
