import configparser
import json
import logging
import os
import requests
from app.Kit.Courier.Utils.read_common import read_common
from app.Kit.Courier.Utils.read_order_data_json import read_order_data_json
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id


class AA_2():

    def aa_aa(self, i):
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        false = False
        host = read_common("host")
        # ticket_pickup_id = read_request_data("ticket_pickup", "ticket_pickup_id")
        # url = host + "api/courier/v1/ticket/pickups/38315/confirm"
        url = host + "api/courier/v1/ticket/pickups/39228/confirm"
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type": "application/json"
        }
        data = read_order_data_json("write_order_data.json")

        res = requests.post(url=url, headers=header, json=data)
        logging.info("填单接口返回的结果是：")
        logging.info(json.dumps(res.json(), indent=4))
        curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        pickup_id_path = curpath + "/Config/xiadan_1.ini"
        ticket_pickup_id = res.json()["data"]["ticket_pickup_id"]
        cf = configparser.ConfigParser()
        # add section 添加section项
        # set(section,option,value) 给section项中写入键值对
        cf.add_section("ticket_pickup" + str(i))
        cf.add_section("courier_pno_number" + str(i))
        pno_num = res.json()["data"]["parcel_info"]["pno"]
        cf.set("courier_pno_number" + str(i), option="pno" + str(i), value=str(pno_num))
        cf.set("ticket_pickup" + str(i), option="ticket_pickup_id" + str(i), value=str(ticket_pickup_id))
        with open(pickup_id_path, "a+") as f:
            if str(pno_num).startswith("TH") and isinstance(ticket_pickup_id, int):
                logging.info("填写订单，截取订单号，开始写入文件request_data.ini")
                cf.write(f)
                logging.info("写入订单号是：")
                logging.info(pno_num)
                logging.info("写入ticket_pickup_id，是：")
                logging.info(ticket_pickup_id)
                logging.info("订单号写入成功")

            else:
                logging.info("订单写入失败，不是订单号")
        return res




