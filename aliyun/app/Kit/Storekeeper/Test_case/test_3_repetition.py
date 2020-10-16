import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.repetition import Repetition
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.repetition import Repetition
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.repetition import Repetition


@allure.feature("复称接口")
class Test_Repetition():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.rep = Repetition()

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @allure.story("复称功能")
    @pytest.mark.parametrize("i", list_i)
    @pytest.mark.run(order=6)
    def test_repetition(self, i):
        result = self.rep.repetition(i)
        logging.info("复称接口响应结果是：")
        logging.info(result)
        assert_that(result["code"]).is_equal_to(1)
        assert_that(result["message"]).is_equal_to("success")
        assert_that(result["data"]).is_not_empty()
        schema_res = Validate_jsonschema(response_result=result, schema_file_name="repetition.json")
        assert_that(schema_res).is_none()



