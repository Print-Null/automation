import logging
import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.vehicle_departure_check import Vehicle_Departure_Check
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.vehicle_departure_check import Vehicle_Departure_Check
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.vehicle_departure_check import Vehicle_Departure_Check


@allure.feature("车辆出港接口->出车凭证线路校验")
class Test_Vehicle_Departure_Check():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.vehicle = Vehicle_Departure_Check()
    @allure.story("车辆出港功能->出车凭证线路校验")
    @pytest.mark.run(order=22)
    def test_vehicle_departure_check(self):
        resp = self.vehicle.vehicle_departure_check()
        logging.info("车辆出港功能->出车凭证线路校验,响应结果是:")
        logging.info(resp)
        assert_that(resp["code"]).is_equal_to(1)
        assert_that(resp["message"]).is_equal_to("success")
        assert_that(resp["data"]).is_not_none()
        schema_res = Validate_jsonschema(resp, "vehicle_departure_check.json")
        assert_that(schema_res).is_none()


