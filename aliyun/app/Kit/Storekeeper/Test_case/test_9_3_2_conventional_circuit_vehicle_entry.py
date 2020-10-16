import logging

import allure
import pytest
from assertpy import assert_that
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.conventional_circuit_vehicle_entry import Conventional_Circuit_Vehicle_Entry

logging.basicConfig(level=logging.INFO)
@allure.feature("常规线路车辆入港")
class Test_Conventional_Circuit_Vehicle_Entry():

    def setup(self):
        self.con = Conventional_Circuit_Vehicle_Entry()
    @allure.story("常规线路车辆入港")
    @pytest.mark.run(order=25)
    def test_conventional_circuit_vehicle_entry(self):
        res = self.con.conventional_circuit_vehicle_entry()
        logging.info("常规线路车辆入港响应结果是:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "conventional_circuit_vehicle_entry.json")
        assert_that(schema_res).is_none()



