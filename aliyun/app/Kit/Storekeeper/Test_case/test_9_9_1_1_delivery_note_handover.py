import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.delivery_note_handover import Delivery_Note_Handover
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.delivery_note_handover import Delivery_Note_Handover
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.delivery_note_handover import Delivery_Note_Handover


@allure.feature("交接接口")
class Test_Delivery_Note_Handover():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.deliver = Delivery_Note_Handover()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # 1, 2, 3, 4, 5, 6, 7, 8,运单状态为 疑难件处理中 不允许交接
    list_i = [10, 11, 12, 13, 14, 15, 16, 17]
    @pytest.mark.parametrize("i", list_i)
    @allure.story("交接")
    @allure.title("交接")
    @pytest.mark.run(order=40)
    def test_delivery_note_handover(self,i):
        res = self.deliver.delivery_note_handover(i)
        logging.info("交接,接口响应结果:")
        logging.info(res)

        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "delivery_note_handover.json")
        assert_that(schema_res).is_none()