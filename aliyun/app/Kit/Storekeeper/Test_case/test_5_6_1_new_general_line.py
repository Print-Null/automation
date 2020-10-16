import logging
import allure
import pytest
from assertpy import assert_that
# from app.kit.Storekeeper.Script.new_general_line import New_General_Line
from app.Kit.Storekeeper.Script.new_general_line import New_General_Line


@allure.feature("新建常规线路")
class Test_New_General_Line():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.new = New_General_Line()

    @pytest.mark.run(order=14)
    def test_new_general_line(self):
        res = self.new.new_general_line()
        logging.info("新建常规线路，接口响应结果是:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")

