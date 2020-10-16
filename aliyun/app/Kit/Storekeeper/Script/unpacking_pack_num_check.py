import logging

import requests

#拆包->集包号码检查
# from app.Kit.Storekeeper.utils.pack_no_range import read_pack_num_only
from app.Kit.Util.common_data import Common_data


class Unpacking_Pack_Num_Check():
    logging.basicConfig(level=logging.INFO)
    def unpacking_pack_num_check(self):
        comm = Common_data()
        # host = read_common("host")
        host = comm.each_parameter("host")
        # url = host + "api/courier/v1/pack/unseal/verify/p5712"
        # num_pack_old = read_pack_num_only("pack_no", "pack_num")
        # num_pack_old = comm.get_parameter_from_redis("pack_no")
        # num_pack_new = int(num_pack_old) - 1
        # pack_num = "p" + str(num_pack_new)
        pack_num = comm.get_parameter_from_redis("pack_no")
        logging.info("读取到的真实集包号是：")
        logging.info(pack_num)
        url = host + "api/courier/v1/pack/unseal/verify/"+str(pack_num)
        logging.info("url拼接结果是：")
        logging.info(url)
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        res = requests.get(url=url, headers=header, verify=False)
        return res.json()

