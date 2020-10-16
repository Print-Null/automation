import datetime

import requests

# from Courier.Utils.read_common import read_common
# from Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session

#已卖包材详情列表
# from app.kit.Courier.Utils.read_common import read_common
# from app.kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
# from app.kit.Util.common_data import Common_data
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


class Material_Sold_Details():

    def material_sold_details(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        today = datetime.date.today()  # 生成今天的日期
        # url = host + "api/courier/v1/staff/material/desc?itemCode=4&businessDate=2020-04-20&pageNum=1&pageSize=20"
        url = host + "api/courier/v1/staff/material/desc?itemCode=4&businessDate="+str(today)+"&pageNum=1&pageSize=20"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url,headers=header, verify=False)
        return res.json()