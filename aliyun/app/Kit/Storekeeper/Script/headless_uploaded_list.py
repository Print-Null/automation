import requests

# from Courier.Utils.read_common import read_common
# from Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session

#无头件已上传列表
# from app.kit.Courier.Utils.read_common import read_common
# from app.kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
# from app.kit.Util.common_data import Common_data
# from app.Kit.Storekeeper.utils.read_storekeeper_session_id_ini import read_storekeeper_session
from app.Kit.Util.common_data import Common_data


class Headless_Uploaded_List():

    def headless_uploaded_list(self):
        comm = Common_data()
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/headless/get_headless"
        # pno = read_request_data(sections="courier_pno_number", option="pno")

        url = host + "api/courier/v1/headless/get_headless"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        res = requests.get(url=url, headers=header, verify=False)
        return res