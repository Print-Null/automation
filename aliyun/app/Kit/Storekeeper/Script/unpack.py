import logging

import requests
#拆包
from app.Kit.Courier.Utils.read_request_data import read_request_data
# from app.Kit.Storekeeper.utils.pack_no_range import read_pack_num_only
from app.Kit.Util.common_data import Common_data


class Unpack():

    def unpack(self):
        comm = Common_data()
        pno_list =[]
        true = True
        # host = read_common("host")
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/unseal"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # num_pack_old = read_pack_num_only("pack_no", "pack_num")
        # num_pack_new = int(num_pack_old) - 1
        # pack_num = "p" + str(num_pack_new)
        pack_num = comm.get_parameter_from_redis("pack_no")
        #修改 list_i
        list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        for i in range(len(list_i)):
            pno = read_request_data("courier_pno_number" + str(i + 1))
            # logging.info(type(pno))
            pno_list.append(pno)
        logging.info("订单号读取结果是：")
        logging.info(pno_list)

        data = {
            "continue_flag": true,
            # "pack_no": "P5712",
            "pack_no": pack_num,
            "recent_pnos": pno_list
        }
        resp = requests.post(url=url,headers=header,json=data, verify=False)
        return resp.json()