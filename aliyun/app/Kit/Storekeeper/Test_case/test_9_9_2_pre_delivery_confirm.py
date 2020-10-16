import logging

import pytest
from assertpy import assert_that
import allure

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.pre_delivery_confirm import Pre_Delivery_Confirm
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.pre_delivery_confirm import Pre_Delivery_Confirm
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.pre_delivery_confirm import Pre_Delivery_Confirm


@allure.feature("妥投前确认")
class Test_Pre_Delivery_Confirm():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = Pre_Delivery_Confirm()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i

    list_i = [17]

    @pytest.mark.parametrize("i", list_i)
    @allure.story("妥投前确认")
    @allure.title("妥投前确认")
    @pytest.mark.run(order=48)
    def test_pre_delivery_confirm(self,i):
        res = self.pre.pre_delivery_confirm(i)
        logging.info("妥投前确认接口,响应结果是:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "pre_delivery_confirm.json")
        assert_that(schema_res).is_none()



