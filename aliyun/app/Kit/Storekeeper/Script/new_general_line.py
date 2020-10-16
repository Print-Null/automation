import time

import requests
#新建常规线路
# from app.Kit.Storekeeper.utils.read_plate_number import read_plate_number
# from app.Kit.Storekeeper.utils.read_station_name import read_station_name
from app.Kit.Util.common_data import Common_data


class New_General_Line():

    def new_general_line(self):
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
        name = str(time.time()).split(".")[0]
        # fleet_id = read_plate_number("plate_number", "fleet_id")
        fleet_id = comm.get_parameter_from_redis("fleet_id")
        # plate_id = read_plate_number("plate_number", "id")
        plate_id = comm.get_parameter_from_redis("id")
        # station_name1 = read_station_name("station_name", "id_1")
        station_name1 = comm.get_parameter_from_redis("id_1")
        # station_name2 = read_station_name("station_name", "id_2")
        station_name2 = comm.get_parameter_from_redis("id_2")
        data = {
                "name": "auto" + name,
                "area": "",
                "type": 0,
                "mode": 1,
                "period": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "price": 2200,
                # "fleet_id": "5eb4cb1b2d738a07c837ff43",
                "fleet_id": fleet_id,
                # "plate_id": "5eb4cc212d738a07c837ff53",
                "plate_id": plate_id,
                "plate_type": 100,
                "driver": "autotest",
                "driver_phone": "1111111111",
                "time_tables": [
                    {
                        "order_no": 1,
                        # "store_id": "TH01010244",
                        "store_id": station_name1,
                        "estimate_end_time": "960",
                        "estimate_start_time": "990",
                        "running_mileage": ""
                    },
                    {
                        "order_no": 2,
                        # "store_id": "TH05050603",
                        "store_id": station_name2,
                        "running_mileage": "111",
                        "estimate_start_time": null,
                        "estimate_end_time": "1086"
                    }
                ],
                "sorting_no": "B"
            }

        resp =requests.post(url=url,headers=header,json=data, verify=False)
        return resp






        '''
        data = {
            "name": "auto1427",  #线路名称  （写死 auto+time）
            "area": "",
            "type": 0, #线路类型 干线 1 支线 手动填写 （写死） （三种规格）
            "mode": 1, #常规线路  手动填写（写死）
            "period": [  #运行周期 （写死）
                1,
                2,
                3,
                4,
                5,
                6,
                7
            ],
            "price": 2200,  #价格 （写死）
            "fleet_id": "5d2edf202d738a490871c919", 根据车牌号接口，返回fleet_id （自动获取）
            "plate_id": "5ea7a3b57bf6b7357ef66d34", #根据车牌号接口，返回id （自动获取）
            "plate_type": 100,  #车辆类型/车型 （写死） （多种规格）
            "driver": "autoname",  #司机姓名（写死）
            "driver_phone": "1111111111", #司机电话（写死）
            "time_tables": [
                {
                    "order_no": 1, #站次1 （写死）
                    "store_id": "TH05010194", #根据站名接口ID （自动获取）
                    "estimate_end_time": "900", #计划到达时间 当前时间距离0点的分钟数
                    "estimate_start_time": "960", #计划出发时间 当前时间距离0点的分钟数
                    "running_mileage": ""
                },
                {
                    "order_no": 2, #站次2
                    "store_id": "TH05010186", #根据站名接口ID
                    "running_mileage": "100",  #里程
                    "estimate_start_time": null, #计划出发时间
                    "estimate_end_time": "1407" #计划到达时间 当前时间距离0点的分钟数
                }
            ],
            "sorting_no": "B" #区域  （多种规格）
        }

                '''

