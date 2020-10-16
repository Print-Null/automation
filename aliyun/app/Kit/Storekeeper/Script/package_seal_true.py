import logging
import random
import requests
#集包
from app.Kit.Courier.Utils.read_request_data import read_request_data
from app.Kit.Util.common_data import Common_data


class Package_seal_True():
    logging.basicConfig(level=logging.INFO)
    def package_seal_true(self):
        comm = Common_data()
        pno_list = []
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
        list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        for i in range(len(list_i)):
            # pno = read_request_data("courier_pno_number"+str(i+1), "pno"+str(i+1))
            pno = read_request_data("courier_pno_number" + str(i+1))
            # logging.info("11"*88)
            # logging.info(type(pno))
            pno_list.append(pno)
            # logging.info("11" * 88)

        # pno = read_request_data("courier_pno_number", "pno")

        logging.info("订单号读取结果是：")
        logging.info(pno_list)
        #集包号读取结果是
        # pack_num = pack_no_range("pack_no", "pack_num")
        pack_no = "p" + str(random.randint(1000,9999))
        logging.info("集包号生成结果是：")
        logging.info(pack_no)
        data = {
            "direction_store_code": "C",
            "pack_category": 1,
            # "pack_no": "p5041",
            "pack_no": pack_no,
            "recent_pnos":
                pno_list,
            "valid_parcel": true
        }
        resp = requests.post(url=url, headers=header, json=data, verify=False)


        #集包检查 设置为false
        # 修改 list_i
        list_i_F = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        for i in range(len(list_i_F)):
            # pno_F = read_request_data("courier_pno_number" + str(i + 1), "pno" + str(i + 1))
            pno_F = read_request_data("courier_pno_number" + str(i+1))
            pno_list.append(pno_F)
        logging.info("订单号读取结果是：")
        logging.info(pno_list)
        # pack_num = pack_no_range("pack_no", "pack_num")
        # pack_no = "p" + str(pack_num)
        logging.info("集包号读取结果是：")
        logging.info(pack_no)

        data1 = {
            "direction_store_code": "C",
            "pack_category": 1,
            # "pack_no": "p5041",
            "pack_no": pack_no,
            "recent_pnos":
                pno_list,
            "valid_parcel": false
        }
        comm.write_parameter_to_redis("pack_no", pack_no)
        resp1 = requests.post(url=url, headers=header, json=data1, verify=False)
        return resp.json(), resp1.json()