import logging

import allure
import pytest
from assertpy import assert_that
# from app.kit.Storekeeper.Script.get_plate_number import Get_Plate_Number
from app.Kit.Storekeeper.Script.get_plate_number import Get_Plate_Number


@allure.feature("获取车牌号等信息")
class Test_Get_Plate_Number():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.num = Get_Plate_Number()

    @pytest.mark.run(order=12)
    def test_get_plate_number(self):
        res = self.num.get_plate_number()
        logging.info("获取车牌号等信息，接口响应结果是:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_empty()


