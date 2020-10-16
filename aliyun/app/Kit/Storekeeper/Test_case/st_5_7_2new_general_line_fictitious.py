import logging
import allure
import pytest
from assertpy import assert_that

# from app.kit.Storekeeper.Script.new_general_line_fictitious import New_General_Line_Fictitious
from app.Kit.Storekeeper.Script.new_general_line_fictitious import New_General_Line_Fictitious


@allure.feature("新建虚拟线路")
class est_New_General_Line_Fictitious():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.new = New_General_Line_Fictitious()

    @pytest.mark.run(order=16)
    def est_new_general_line_fictitious(self):
        res = self.new.new_general_line_fictitious()
        logging.info("虚拟线路，获取车牌号等信息，接口响应结果是:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")


