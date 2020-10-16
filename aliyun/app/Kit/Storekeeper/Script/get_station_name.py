import configparser
import logging
import os
import requests

#获取站名
from app.Kit.Util.common_data import Common_data


class Get_Station_Name():
    #
    logging.basicConfig(level=logging.INFO)
    def get_station_name(self):
        comm = Common_data()
        host = comm.each_parameter("host_10000")
        # session = read_session_10000("ms_10000", "ms_session")
        session = comm.get_parameter_from_redis("login_10000")
        header = {
            # "X-MS-SESSION-ID": "1589437386_e231ab71d33749205743fcc8bf0933e1e9d0cc80184ecaeeaa4525a7165d139f_10000",
            "X-MS-SESSION-ID": session,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN"
        }
        url = host + "ms/api/setting/store/manager/van/line"

        resp = requests.get(url=url, headers=header, verify=False)
        #获取第一个站名ID 和第二个站名ID，存储到配置文件中

        # id_1 = resp.json()["data"]返回一个数组
        items = resp.json()["data"]
        for item in items:
            logging.info(item)
        logging.info("all datas")
        logging.info(items)
        #从env中获取第一个站点名称，再根据站点名称，去获取ID
        name = comm.each_parameter("station_name")
        for item in items:
            if item["name"] == name:
                id_1 = item["id"]

        id_2 = resp.json()["data"][1]["id"]

        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # session_path = curpath + "/conf/station_name.ini"
        # session_path = os.path.join(os.path.abspath(
        #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        #     "conf/station_name.ini")

        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/station_name.ini"
        #
        #
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("station_name")
        # cf.set("station_name", option="id_1", value=str(id_1))
        # cf.set("station_name", option="id_2", value=str(id_2))
        #
        # with open(session_path, "w+") as f:
        #     logging.info("后台10000号，获取第一个站名ID 和第二个站名ID，信息开始写入")
        #     cf.write(f)
        #     logging.info("后台10000号，获取第一个站名ID 和第二个站名ID，信息写入完成")
        #     logging.info(id)

        comm.write_parameter_to_redis("id_1",id_1)
        comm.write_parameter_to_redis("id_2",id_2)

        return resp