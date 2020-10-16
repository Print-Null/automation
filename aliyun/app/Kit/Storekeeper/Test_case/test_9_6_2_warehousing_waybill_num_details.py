import logging

import allure
import pytest
from assertpy import assert_that
from app.Kit.Storekeeper.Script.warehousing_waybill_num_details import Warehousing_Waybill_Num_Details


@allure.feature("到件入仓-输入运单号->快件详情")
class Test_Warehousing_Waybill_Num_Details():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ware = Warehousing_Waybill_Num_Details()

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    @pytest.mark.parametrize("i",list_i)
    @allure.story("到件入仓-输入运单号->快件详情")
    @pytest.mark.run(order=29)
    def test_warehousing_waybill_num_details(self,i):
        res = self.ware.warehousing_waybill_num_details(i)
        logging.info("到件入仓-输入运单号->快件详情,响应结果:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()

