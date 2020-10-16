import logging

import pytest
from assertpy import assert_that
import allure
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.vehicle_departure import Vehicle_Departure


@allure.feature("车辆出港接口")
class Test_Vehicle_Departure():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.vehicle = Vehicle_Departure()
    @allure.story("车辆出港功能")
    @pytest.mark.run(order=23)
    def test_vehicle_departure(self):
        res = self.vehicle.vehicle_departure()
        logging.info("车辆出港接口返回:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "vehicle_departure.json")
        assert_that(schema_res).is_none()

