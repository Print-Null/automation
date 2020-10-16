import logging

import allure
import pytest
from assertpy import assert_that
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.pre_delivery_note_handover_cargo_storage_Inadequate import \
    Pre_Delivery_Note_Handover_Cargo_Storage_Inadequate_Check


@allure.feature("交接前，货件留仓->运单检查")
class Test_Pre_Delivery_Note_Handover_Cargo_Storage_Inadequate_Check():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = Pre_Delivery_Note_Handover_Cargo_Storage_Inadequate_Check()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #将第一个订单，来进行此接口,不需要修改list_i
    list_i = [1]

    @allure.title("货件留仓->运单检查")
    @allure.story("交接前，货件留仓->运单检查")
    @pytest.mark.parametrize("i",list_i)
    @pytest.mark.run(order=32)
    def test_pre_delivery_note_handover_cargo_storage_inadequate_check(self,i):
        res = self.pre.pre_delivery_note_handover_cargo_storage_inadequate_check(i)
        logging.info(res.text)
        logging.info("交接前，货件留仓->运力不足，响应结果是：")
        assert_that(res.status_code).is_equal_to(200)
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
        schema_res = Validate_jsonschema(res.json(), "pre_delivery_note_handover_cargo_storage_inadequate_check.json")
        assert_that(schema_res).is_none()


