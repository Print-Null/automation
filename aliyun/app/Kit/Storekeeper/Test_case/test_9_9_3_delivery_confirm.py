import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.delivery_confirm import Deliver_Confirm
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.delivery_confirm import Deliver_Confirm
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.delivery_confirm import Deliver_Confirm


@allure.feature("确认妥投接口")
class Test_Delivery_Perfirm():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.delivery = Deliver_Confirm()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [17]

    @pytest.mark.parametrize("i", list_i)
    @allure.story("确认妥投")
    @allure.title("确认妥投")
    @pytest.mark.run(order=49)
    def test_delivery_confirm(self,i):
        res = self.delivery.delivery_confirm(i)
        logging.info("确认妥投,接口响应结果:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_empty()
        schema_res = Validate_jsonschema(res, "delivery_confirm.json")
        assert_that(schema_res).is_none()



