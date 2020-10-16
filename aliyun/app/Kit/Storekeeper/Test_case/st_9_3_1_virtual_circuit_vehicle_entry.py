import logging

import allure
import pytest
from assertpy import assert_that
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.virtual_circuit_vehicle_entry import Virtual_Circuit_Vehicle_Entry

logging.basicConfig(level=logging.INFO)
@allure.feature("虚拟线路车辆入港")
class est_Virtual_Circuit_Vehicle_Entry():

    def setup(self):
        self.con = Virtual_Circuit_Vehicle_Entry()

    @pytest.mark.run(order=24)
    @allure.story("虚拟线路车辆入港")
    def est_virtual_circuit_vehicle_entry(self):
        res = self.con.Virtual_circuit_vehicle_entry()
        logging.info("虚拟线路车辆入港响应结果是:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "virtual_circuit_vehicle_entry.json")
        assert_that(schema_res).is_none()