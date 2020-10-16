import json
import datetime
import logging
import os

import requests
#常规线路管理列表

from app.Kit.Util.common_data import Common_data


class General_Route_Management_List():
    logging.basicConfig(level=logging.INFO)
    def general_route_management_list(self):
        null = None
        comm = Common_data()
        host = comm.each_parameter("host_10000")
        url = host + "ms/api/fleet/van/line?sortingNo=&type=&originStoreId=&targetStoreId=&ms_houtai_login_user=&pageSize=20&pageNum=1&passStoreId="
        # session = read_session_10000("ms_10000", "ms_session")
        session = comm.get_parameter_from_redis("login_10000")
        header = {
            # "X-MS-SESSION-ID": "1589437386_e231ab71d33749205743fcc8bf0933e1e9d0cc80184ecaeeaa4525a7165d139f_10000",
            "X-MS-SESSION-ID": session,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN"
        }
        res = requests.get(url=url, headers=header, verify=False)
        data_item = res.json()["data"]["items"][0]
        # logging.info(res.json())
        #获取最新一条数据[0]
        datas = res.json()["data"]["items"][0]["time_tables"][0]["estimate_start_time"]
        logging.info(datas)
        # logging.info("datas ")
        # logging.info(datas)
        # 将以下数据保存到文件中
        '''
        {
            "id": null,
            "fleet_id": "5d2edf122d738a490871c918",
            "van_line_id": "5d1dc8642d738a29e93034e9",
            "fleet_name": "我有两个车",
            "driver": "2",
            "plate_id": "5e8759522ff36f3edb3cef8f",
            "driver_phone": "2221212121",
            "departure_time": "2020-04-17 10:35"
        }
        '''
        today = datetime.date.today()
        min = int(datas)
        hour = min // 60
        print(hour)
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = hour
        fenzhong = min % 60
        if fenzhong < 10:
            fenzhong = "0" + str(fenzhong)
        else:
            fenzhong = fenzhong
        departure_time = str(today) + " " + str(hour) + ":" + str(fenzhong)

        new_dict1 = {
            "id": null,
            "fleet_id": data_item["fleet_id"],
            "van_line_id": data_item["id"],
            "fleet_name": data_item["fleet_name"],
            "driver": data_item["fleet_name"],
            "plate_id": data_item["plate_id"],
            "driver_phone": data_item["driver_phone"],
            "departure_time": departure_time
        }
        new_dict={
            "id": null,
            "fleet_id": null,
            "van_line_id": data_item["id"],
            "fleet_name": null,
            "driver": null,
            "plate_id": null,
            "driver_phone": null,
            "departure_time": departure_time
        }
        # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # print(curpath)
        # # pickup_id_path = curpath + "/conf/ms_generate_vehicle_voucher_virtual.json"
        # # pickup_id_path = os.path.join(os.path.abspath(
        # #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        # #     "conf/ms_generate_vehicle_voucher_virtual.json")
        #
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # pickup_id_path = root_path + "/app/Kit/Storekeeper/conf/ms_generate_vehicle_voucher_virtual.json"
        #
        # with open(pickup_id_path, "w+", encoding="utf-8") as f:
        #
        #     json.dump(new_dict, f)
        #
        # print("加载入文件完成...")
        comm.write_parameter_to_redis("ms_generate_vehicle_voucher_virtual",str(new_dict))


        return res


# if __name__ == '__main__':
#     ge = General_Route_Management_List()
#     ge.general_route_management_list()