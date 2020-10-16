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
from utils.redisbase import RedisBase


@allure.feature('kit-数据清理')
class Test_Order_Type_All_Collect_Complete(object):
    logging.basicConfig(level=logging.INFO)

    @pytest.mark.run(order=111)
    def test_order_type_all_collect_complete(self):
        # 判断是否存在
        if RedisBase().exists("Kit_Storekeeper_ticket_pickup_id"):
        #从redis里取Kit_Storekeeper_ticket_pickup_id并删除
            print("Kit_Storekeeper_ticket_pickup_id需要清理")
            # RedisBase().delete_keys("Kit_Storekeeper_ticket_pickup_id")
            RedisBase().delete("Kit_Storekeeper_ticket_pickup_id")

            print("数据清理完成")
        else:
            print("Kit_Storekeeper_ticket_pickup_id不需要清理")