import json
import logging
import os
from jsonschema import validate
import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data
from assertpy import assert_that
from utils import redisbase


def return_data_all():
    # data = Common_data().get_parameter_from_redis("ticket_pickup_id")
    data = Common_data().get_parameter_from_redis("Kit_Storekeeper_ticket_pickup_id")
    # data=redisbase.RedisBase().get("Kit_Storekeeper_ticket_pickup_id")
    logging.info("aaaaa")
    logging.info(type(data))
    data_list = list(str(data).split(","))
    # data_list = list(data)
    logging.info(data_list)
    logging.info(type(data_list))
    # logging.info(data)
    # if type(data) is not bool :
    #     # redisObj = redisbase.RedisBase()
    #     # data = redisObj.get("ticket_pickup_id")
    #     logging.info("读取到的数据是：")
    #     logging.info(data)
    #     logging.info("数据类型是：")
    #     logging.info(type(data))
    #     data_list = list(data)
    #     logging.info(data_list)
    #     logging.info(type(data_list))
    # else:
    #     data_list = ["123"]
    logging.info(data)
    logging.info(data_list)
    return data_list
pick_data_num = return_data_all()

@allure.feature("下单所有类型,揽收完成")
class Test_Order_Type_All_Collect_Complete(object):
    logging.basicConfig(level=logging.INFO)
    @pytest.mark.parametrize("ticket_pickup_id", pick_data_num)
    @pytest.mark.run(order=110)
    def test_order_type_all_collect_complete(self, ticket_pickup_id):
        logging.info(ticket_pickup_id)
        logging.info("**"*88)
        if ticket_pickup_id != '' and ticket_pickup_id is not None and ticket_pickup_id != "123" and ticket_pickup_id != 123 and len(ticket_pickup_id) < 10:
            logging.info("")
            logging.info("读取到的ticket_pickup_id是：")
            logging.info(ticket_pickup_id)
            comm = Common_data()
            # session_id = read_courier_session_id()
            # session_id = read_courier_session_id("session_id")
            session_id = read_courier_session_id('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')
            # ticket_pickup_id = read_request_data("ticket_pickup" + str(i), "ticket_pickup_id" + str(i))
            url = "api/courier/v1/ticket/%s"%ticket_pickup_id
            logging.info("url")
            logging.info(url)
            header = {
                "X-FLE-SESSION-ID":session_id,
                "Accept-Language": "zh-CN",
                "By-Platform": "RB_KIT",
                "X-FLE-EQUIPMENT-TYPE": "kit"
            }
            # host = read_common("host")
            host = comm.each_parameter("host")
            logging.info(host)
            resp = requests.post(url=host+url, headers=header, verify=False)
            logging.info("揽收完成接口运行完毕")
            logging.info("揽收完成接口,响应结果是:")
            logging.info(resp.json())
            assert_that(resp.json()["code"]).is_equal_to(1)
            assert_that(resp.json()["message"]).is_equal_to("success")
            assert_that(resp.json()["data"]).is_none()
            # logging.info("jsonschema文件path:../data/jsonschema/100_order_type_all_collect_complete.json")
            # with open("../data/jsonschema/100_order_type_all_collect_complete.json", "r", encoding="utf-8") as f:
            #     shcema = json.load(f)
            #     res = validate(instance=resp.json(), schema=shcema)
            #     logging.info("jsonschema验证结果是： " + str(res))
            # assert_that(res).is_none()