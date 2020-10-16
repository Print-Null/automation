import random
import requests
#新建虚拟线路
from app.Kit.Util.common_data import Common_data


class New_General_Line_Fictitious():

    def new_general_line_fictitious(self):
        null = None
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
        url = host + "ms/api/fleet/van/line"
        # name = str(time.time()).split(".")[0]
        # fleet_id = read_plate_number("plate_number", "fleet_id")
        # plate_id = read_plate_number("plate_number", "id")
        # station_name1 = read_station_name("station_name", "id_1")
        station_name1 = comm.get_parameter_from_redis("id_1")
        # station_name2 = read_station_name("station_name", "id_2")
        station_name2 = comm.get_parameter_from_redis("id_2")

        data = {
            "name": "autov" + str(random.randint(10000, 100000)),
            "mode": 3,
            "time_tables": [
                {
                    "order_no": 1,
                    "store_id": station_name1,
                    "estimate_end_time": "924",
                    "estimate_start_time": "984",
                    "running_mileage": ""
                },
                {
                    "order_no": 2,
                    "store_id": station_name2,
                    "running_mileage": "100",
                    "estimate_start_time": null,
                    "estimate_end_time": "1044"
                }
            ]
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)
        return resp
        # data1 = {
        #         "name": "auto" + name,
        #         "area": "",
        #         "type": 0,
        #         "mode": 1,
        #         "period": [
        #             1,
        #             2,
        #             3,
        #             4,
        #             5,
        #             6,
        #             7
        #         ],
        #         "price": 2200,
        #         # "fleet_id": "5eb4cb1b2d738a07c837ff43",
        #         "fleet_id": fleet_id,
        #         # "plate_id": "5eb4cc212d738a07c837ff53",
        #         "plate_id": plate_id,
        #         "plate_type": 100,
        #         "driver": "autotest",
        #         "driver_phone": "1111111111",
        #         "time_tables": [
        #             {
        #                 "order_no": 1,
        #                 # "store_id": "TH01010244",
        #                 "store_id": station_name1,
        #                 "estimate_end_time": "960",
        #                 "estimate_start_time": "990",
        #                 "running_mileage": ""
        #             },
        #             {
        #                 "order_no": 2,
        #                 # "store_id": "TH05050603",
        #                 "store_id": station_name2,
        #                 "running_mileage": "111",
        #                 "estimate_start_time": null,
        #                 "estimate_end_time": "1086"
        #             }
        #         ],
        #         "sorting_no": "B"
        #     }



