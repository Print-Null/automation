import logging
import os

import allure
import pytest
import requests
from assertpy import assert_that
from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data
from utils import redisbase


@allure.feature("下单所有类型,揽收完成")
class Test_Order_Type_All_Collect_Complete(object):
    logging.basicConfig(level=logging.INFO)


    def return_data_all():

        data = Common_data().get_parameter_from_redis("ticket_pickup_id")
        if type(data) is not bool :
            # redisObj = redisbase.RedisBase()
            # data = redisObj.get("ticket_pickup_id")
            logging.info("读取到的数据是：")
            logging.info(data)
            logging.info("数据类型是：")
            logging.info(type(data))
            data_list = list(data)
            logging.info(data_list)
            logging.info(type(data_list))
        else:
            data_list = ["123"]
        return data_list


    pick_data_num = return_data_all()
    @pytest.mark.parametrize("ticket_pickup_id", pick_data_num)
    @pytest.mark.run(order=110)
    def test_order_type_all_collect_complete(self, ticket_pickup_id):
        logging.info(ticket_pickup_id)
        logging.info("**"*88)
        if ticket_pickup_id != '' and ticket_pickup_id is not None and ticket_pickup_id != "123" and ticket_pickup_id != 123:
            logging.info("")
            logging.info("读取到的ticket_pickup_id是：")
            logging.info(ticket_pickup_id)
            comm = Common_data()
            # session_id = read_courier_session_id()
            session_id = read_courier_session_id("session_id")
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