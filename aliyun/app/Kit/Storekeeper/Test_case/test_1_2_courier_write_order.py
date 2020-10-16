import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Script.write_order import Write_Order
# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Courier.Script.write_order import Write_Order
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Courier.Script.write_order import Write_Order
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema


@allure.feature("填单接口")
class Test_courier_write_order():
    logging.basicConfig(level=logging.INFO)
    # list_i = [1]
    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @pytest.mark.parametrize("i", list_i)
    @allure.title("填单接口")
    @pytest.mark.run(order=2)
    def test_courier_write_order(self, i):
        writeorder = Write_Order()
        resp = writeorder.write_order(i)
        logging.info("填单接口,响应结果是:")
        logging.info(resp)
        assert_that(resp["code"]).is_equal_to(1)
        assert_that(resp["message"]).is_equal_to("success")
        assert_that(resp["data"]).is_not_empty()
        schema_res = Validate_jsonschema(response_result=resp,schema_file_name="write_order.json")
        assert_that(schema_res).is_none()