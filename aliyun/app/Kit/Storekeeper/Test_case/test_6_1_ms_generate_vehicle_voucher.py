import logging

import allure
import pytest

# from app.kit.Storekeeper.Script.ms_generate_vehicle_voucher_1 import Ms_Generate_Vehicle_Voucher_1
from app.Kit.Storekeeper.Script.ms_generate_vehicle_voucher_1 import Ms_Generate_Vehicle_Voucher_1


@allure.feature("网点车线任务列表")
class Test_Ms_Generate_Vehicle_Voucher_1():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ms = Ms_Generate_Vehicle_Voucher_1()

    @allure.story("网点车线任务列表")
    @pytest.mark.run(order=18)
    def test_ms_generate_vehicle_voucher_1(self):
        self.ms.generate_vehicle_voucher_1()