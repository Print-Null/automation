import json
import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.check_pieces import Check_Piece
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.check_pieces import Check_Piece
from app.Kit.Storekeeper.Script.check_pieces import Check_Piece


@allure.feature("查单")
class Test_Check_Piece():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.check = Check_Piece()

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("查单")
    @allure.story("查单")
    @pytest.mark.run(order=53)
    def test_check_piece(self,i):
        res = self.check.check_piece(i)
        logging.info("查单,接口响应结果是：")
        logging.info(json.dumps(res.json(), indent=4))
        # logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()


