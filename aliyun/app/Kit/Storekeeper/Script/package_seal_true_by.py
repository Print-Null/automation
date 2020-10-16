import logging

import requests

#集包by
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Storekeeper.utils.pack_no_range import pack_no_range
from app.Kit.Util.common_data import Common_data


class Package_seal_True_by():
    logging.basicConfig(level=logging.INFO)
    def package_seal_true_by(self):
        comm = Common_data()
        pno_list_By = []
        true = True
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/pack/seal"
        # session_id = read_storekeeper_session("storekeeper_session", "session_id")
        session_id = comm.get_parameter_from_redis("storekeeper_session")
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # 修改 list_i
        list_i = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        for i in range(len(list_i)):
            pno_by = read_request_data("courier_pno_number"+str(i+18), "pno"+str(i+18))
            # logging.info("11"*88)
            # logging.info(type(pno))
            pno_list_By.append(pno_by)
            # logging.info("11" * 88)

        # pno = read_request_data("courier_pno_number", "pno")

        logging.info("订单号读取结果是：")
        logging.info(pno_list_By)
        pack_num = pack_no_range("pack_no", "pack_num")


        pack_no = "p" + str(pack_num)
        logging.info("集包号读取结果是：")
        logging.info(pack_no)
        # data = {
        #         "direction_store_code": "C",
        #         "pack_category": 1,
        #         # "pack_no": "p5701",
        #         "pack_no": pack_no,
        #         "recent_pnos": [
        #             str(list_pno_str)
        #         ],
        #         "valid_parcel": false
        #     }

        data = {
            "direction_store_code": "C",
            "pack_category": 1,
            # "pack_no": "p5041",
            "pack_no": pack_no,
            "recent_pnos":
                pno_list_By,
            #     [
            #     list_pno_str
            #     # "TH050219y92a",
            #     # "TH050219y91a",
            #     # "TH050219y90a",
            #     # "TH050219y89a"
            # ],
            "valid_parcel": true
        }
        resp = requests.post(url=url, headers=header, json=data)
        return resp.json()