import logging

import allure
import pytest
from assertpy import assert_that
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.pre_delivery_detain_warehouse_inadequate import Pre_Delivery_Detain_Warehouse_Inadquate


@allure.feature("交接前-货件留仓-运力不足")
class Test_Pre_Delivery_Detain_Warehouse_Inadequate():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = Pre_Delivery_Detain_Warehouse_Inadquate()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     #将第一个订单，来进行此接口,不需要修改list_i
    list_i = [2]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接前-货件留仓-运力不足")
    @allure.story("交接前-货件留仓-运力不足")
    @pytest.mark.run(order=33)
    def test_pre_delivery_detain_warehouse_inadquate(self,i):
        res = self.pre.pre_delivery_detain_warehouse_inadquate(i)
        logging.info("交接前-货件留仓-运力不足,响应结果是：")
        logging.info(res.json())
        assert_that(res.status_code).is_equal_to(200)
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
        schema_res = Validate_jsonschema(res.json(), "pre_delivery_detain_warehouse_inadquate.json")
        assert_that(schema_res).is_none()

