import configparser
import json
import logging
import os
import requests
from app.Kit.Courier.Utils.read_order_data_json import read_order_data_json
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data

logging.basicConfig(level=logging.INFO)

class Write_Order():
    #填单
    def write_order(self, i):
        comm = Common_data()

        # session_id = read_courier_session_id()
        session_id = read_courier_session_id("session_id")
        false = False
        # host = read_common("host")
        host = comm.each_parameter("host")
        url = host + "api/courier/v1/ticket/pickups/parcel"
        header = {
            "X-FLE-SESSION-ID":session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-DEVICE-ID": "8673510346528821571665712622",
            "Content-Type":"application/json"
        }
        data = read_order_data_json("write_order_data.json")


        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("填单接口返回的结果是：")
        logging.info(json.dumps(res.json(), indent=4))

        #将ticket_pickup_id, pno 写入redis
        Common_data().write_parameter_to_redis("ticket_pickup_id" + str(i), res.json()["data"]["ticket_pickup_id"])
        Common_data().write_parameter_to_redis("courier_pno_number" + str(i), res.json()["data"]["parcel_info"]["pno"])



        # # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # # pickup_id_path = curpath + "/Config/request_data.ini"
        #
        # # pickup_id_path = os.path.join(os.path.abspath(
        # #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
        # #     "Config/request_data.ini")
        # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
        # pickup_id_path = root_path + "/app/Kit/Courier/Config/request_data.ini"
        # # pickup_id_path = curpath + "/Config/request_data.ini"
        #
        #
        # ticket_pickup_id = res.json()["data"]["ticket_pickup_id"]
        # cf = configparser.ConfigParser()
        # # add section 添加section项
        # # set(section,option,value) 给section项中写入键值对
        # cf.add_section("ticket_pickup"+str(i))
        # cf.add_section("courier_pno_number"+str(i))
        # pno_num = res.json()["data"]["parcel_info"]["pno"]
        # cf.set("courier_pno_number" + str(i), option="pno" + str(i), value=str(pno_num))
        # cf.set("ticket_pickup" + str(i), option="ticket_pickup_id" + str(i), value=str(ticket_pickup_id))
        # with open(pickup_id_path, "a+") as f:
        #     if str(pno_num).startswith("TH") and isinstance(ticket_pickup_id, int):
        #         logging.info("填写订单，截取订单号，开始写入文件request_data.ini")
        #         cf.write(f)
        #         logging.info("写入订单号是：")
        #         logging.info(pno_num)
        #         logging.info("写入ticket_pickup_id，是：")
        #         logging.info(ticket_pickup_id)
        #         logging.info("订单号写入成功")
        #
        #     else:
        #         logging.info("订单写入失败，不是订单号")
        return res.json()



        # data = {
        #     "article_category": 99,
        #     "call_duration": 0,
        #     "client_id": "CA0546",
        #     "cod_amount": 0,
        #     "cod_enabled": false,
        #     "customer_type_category": 2,
        #     "dst_city_code": "TH0502",
        #     "dst_country_code": "TH",
        #     "dst_detail_address": "2",
        #     "dst_district_code": "TH050201",
        #     "dst_name": "2",
        #     "dst_phone": "1346999281",
        #     "dst_postal_code": "13130",
        #     "dst_province_code": "TH05",
        #     "express_category": 1,
        #     "freight_insure_enabled": false,
        #     "height": 1,
        #     "insure_declare_value": 0,
        #     "insured": false,
        #     "length": 1,
        #     "settlement_category": 1,
        #     "skipping_tips": [],
        #     "src_city_code": "TH1101",
        #     "src_country_code": "TH",
        #     "src_detail_address": "1",
        #     "src_district_code": "TH110101",
        #     "src_name": "1",
        #     "src_phone": "1232311232",
        #     "src_postal_code": "26000",
        #     "src_province_code": "TH11",
        #     "total_amount": 4000,
        #     "weight": 2000,
        #     "width": 1
        # }
        '''
        
        res = requests.post(url=url, headers=header, json=data)
        logging.info("填单接口返回的结果是：")
        logging.info(json.dumps(res.json(), indent=4))
        curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        pickup_id_path = curpath + "/Config/request_data.ini"
        ticket_pickup_id = res.json()["data"]["ticket_pickup_id"]
        cf = configparser.ConfigParser()
        # add section 添加section项
        # set(section,option,value) 给section项中写入键值对
        cf.add_section("ticket_pickup")
        cf.add_section("courier_pno_number")
        pno_num = res.json()["data"]["parcel_info"]["pno"]
        cf.set("courier_pno_number", option="pno", value=str(pno_num))
        cf.set("ticket_pickup", option="ticket_pickup_id", value=str(ticket_pickup_id))
        with open(pickup_id_path, "w+") as f:
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
        return res.json()
        '''


