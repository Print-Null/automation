import datetime
import json
import logging
import os
import requests

#生成出车凭证
# from app.Kit.Storekeeper.utils.read_ms_session import read_ms_session
from app.Kit.Util.common_data import Common_data


class Ms_Generate_Vehicle_Voucher_1():
    logging.basicConfig(level=logging.INFO)
    def generate_vehicle_voucher_1(self):
        comm = Common_data()
        # host = read_common("ms_host")
        host = comm.each_parameter("ms_host")
        today = datetime.date.today()
        # url = host + "ms/api/fleet/van/line/task?type=1&startDate=2020-06-02&pageNum=1&pageSize=20"
        url = host + "ms/api/fleet/van/line/task?type=1&startDate="+str(today)+"&pageNum=1&pageSize=20"
        # SESSION_ID = read_ms_session("ms", "ms_session")
        SESSION_ID = comm.get_parameter_from_redis("ms_session")
        header={
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"zh-CN",
            "Content-Type":"application/json;charset=UTF-8",
            # "Origin":"http://192.168.0.222",
            # "Referer":"http://192.168.0.222/",
            "X-MS-SESSION-ID":SESSION_ID
                    }
        resp = requests.get(url=url, headers=header, verify=False)
        dat = resp.json()["data"]["items"][0]
        logging.info("接口响应结果是：")
        logging.info(dat)
        # # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # # session_path = curpath + "\conf\ms_generate_vehicle_voucher_actual.json"
        #
        # # session_path = os.path.join(os.path.abspath(
        # #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        # #     "conf\ms_generate_vehicle_voucher_actual.json")
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # session_path = root_path + "/app/Kit/Storekeeper/conf/ms_generate_vehicle_voucher_actual.json"
        # with open(session_path, encoding="utf-8", mode='w') as f:
        #     json.dump(dat, f)

        comm.write_parameter_to_redis("ms_generate_vehicle_voucher_actual",str(dat))




