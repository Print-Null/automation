import requests
#卖包材 -> S包材
from app.Kit.Util.common_data import Common_data


class Material_Sold():

    def material_sold(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/staff/material/sold"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        data = {
            "detail_add_forms": [
                {
                    "material_category": 1,
                    "number": 4,
                    "price": 1000
                }
            ]
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        return res.json()