import requests
#查集包
# from app.Kit.Storekeeper.utils.pack_no_range import read_pack_num_only
from app.Kit.Util.common_data import Common_data


class Search_Pachage():

    def search_package(self):
        comm = Common_data()
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/pack/get_pack/p5838"
        # pno = read_request_data(sections="courier_pno_number", option="pno")
        # num_pack_old = read_pack_num_only("pack_no", "pack_num")
        # num_pack_old = comm.get_parameter_from_redis("pack_no")
        # num_pack_new = int(num_pack_old) - 1
        # pack_num = "p" + str(num_pack_new)
        pack_num = comm.get_parameter_from_redis("pack_no")

        url = host + "api/courier/v1/pack/get_pack/"+str(pack_num)
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }

        res = requests.get(url=url, headers=header, verify=False)
        return res
