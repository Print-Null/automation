import datetime

import requests
#无头件上传
from app.Kit.Util.common_data import Common_data


class Handless_Upload():

    def handless_upload(self):
        comm = Common_data()
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/headless/add"
        # pno = read_request_data(sections="courier_pno_number", option="pno")

        url = host + "api/courier/v1/headless/add"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        today = datetime.date.today()  # 生成今天的日期
        data={
            "height": 1,
            "length": 1,
            "parcel_describe": "无头件上传,ddffvhhhh the best time and effort and then delete your email address and contact the same problem with your company name",
            # "parcel_discover_date": "2020-04-23",
            "parcel_discover_date": str(today),
            "parcel_headless_category": 1,
            "parcel_image_url": [
                "headlessParcel/1587613811-3dbfc377605f457298bcadc36c041cb0.jpg"
            ],
            "weight": 2000,
            "width": 1
        }

        res = requests.post(url=url, headers=header, json=data, verify=False)
        return res