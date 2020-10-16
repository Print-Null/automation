import configparser
import logging
import os
import requests
#获取车牌号等信息

from app.Kit.Util.common_data import Common_data


class Get_Plate_Number():
    #
    logging.basicConfig(level=logging.INFO)
    def get_plate_number(self):
        comm = Common_data()
        host = comm.each_parameter("host_10000")
        # com_id = read_query_company_name("query_company", "id")
        #id = resp.json()["data"]["items"][1]["id"]
        com_id = comm.get_parameter_from_redis("query_company_name")
        # url = host + "ms/api/fleet/van?ms_houtai_login_user=5eb4cb1b2d738a07c837ff43"
        url = host + "ms/api/fleet/van?ms_houtai_login_user=" + str(com_id)
        # session = read_session_10000("ms_10000", "ms_session")
        session = comm.get_parameter_from_redis("login_10000")
        header = {
            # "X-MS-SESSION-ID": "1589437386_e231ab71d33749205743fcc8bf0933e1e9d0cc80184ecaeeaa4525a7165d139f_10000",
            "X-MS-SESSION-ID": session,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN"
        }
        resp = requests.get(url=url, headers=header, verify=False)
        #将获取到的车牌号等信息，存储到指定文件
        plate_number = resp.json()["data"]["items"][0]["plate_number"]
        type_text = resp.json()["data"]["items"][0]["type_text"]
        id = resp.json()["data"]["items"][0]["id"]
        fleet_id = resp.json()["data"]["items"][0]["fleet_id"]

        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/plate_number.ini"

        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/plate_number.ini")

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/plate_number.ini"
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("plate_number")
        # cf.set("plate_number", option="plate_number", value=str(plate_number))
        # cf.set("plate_number", option="type_text", value=str(type_text))
        # cf.set("plate_number", option="id", value=str(id))
        # cf.set("plate_number", option="fleet_id", value=str(fleet_id))
        #
        # with open(session_path, "w+", encoding="utf-8") as f:
        #     logging.info("后台10000号，将获取到的车牌号等信息，存储到指定文件，信息开始写入")
        #     cf.write(f)
        #     logging.info("后台10000号，将获取到的车牌号等信息，存储到指定文件，信息写入完成")
        #     logging.info(id)

        comm.write_parameter_to_redis("plate_number",plate_number)
        comm.write_parameter_to_redis("type_text",type_text)
        comm.write_parameter_to_redis("id",id)
        comm.write_parameter_to_redis("fleet_id",fleet_id)

        return resp