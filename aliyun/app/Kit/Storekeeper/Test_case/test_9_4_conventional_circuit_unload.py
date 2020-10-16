
import logging

import allure

# from Storekeeper.Script.conventional_circuit_unload import Conventional_Circuit_Unload
import pytest
from assertpy import assert_that

# from app.kit.Storekeeper.Script.conventional_circuit_unload import Conventional_Circuit_Unload
from app.Kit.Storekeeper.Script.conventional_circuit_unload import Conventional_Circuit_Unload


@allure.feature("常规线路解车")
class Test_Conventional_Circuit_Unload():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.con = Conventional_Circuit_Unload()


    @allure.story("常规线路解车")
    @pytest.mark.run(order=26)
    def test_conventional_circuit_unload(self):
        res = self.con.conventional_circuit_unload()
        logging.info("常规线路解车, 响应结果是:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()

