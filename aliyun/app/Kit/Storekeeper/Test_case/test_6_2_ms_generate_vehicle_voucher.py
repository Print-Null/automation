import logging
import allure
import pytest
from assertpy import assert_that
# from app.kit.Storekeeper.Script.ms_generate_vehicle_voucher import Ms_Generate_Vehicle_Voucher
from app.Kit.Storekeeper.Script.ms_generate_vehicle_voucher import Ms_Generate_Vehicle_Voucher


@allure.feature("生成出车凭证")
class Test_Ms_Generate_Vehicle_Voucher():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ms = Ms_Generate_Vehicle_Voucher()
    @allure.story("生成出车凭证功能")
    @pytest.mark.run(order=19)
    def test_ms_generate_vehicle_voucher(self):
        res = self.ms.generate_vehicle_voucher()
        logging.info("常规线路生成出车凭证接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")