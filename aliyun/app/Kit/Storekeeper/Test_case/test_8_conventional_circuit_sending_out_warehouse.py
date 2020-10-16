import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.conventional_circuit_sending_out_warehouse import Conventional_Circuit_Sending_Out_Warehouse
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.conventional_circuit_sending_out_warehouse import \
#     Conventional_Circuit_Sending_Out_Warehouse
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.conventional_circuit_sending_out_warehouse import \
    Conventional_Circuit_Sending_Out_Warehouse


@allure.feature("常规线路发件出仓")
class Test_Conventional_Circuit_Sending_Out_Warehouse():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.conventional_circuit = Conventional_Circuit_Sending_Out_Warehouse()

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    @allure.story("常规线路发件出仓功能")
    @pytest.mark.parametrize("i", list_i)
    @pytest.mark.run(order=21)
    def test_conventional_circuit_sending_out_warehouse(self, i):
        resp = self.conventional_circuit.conventional_circuit_sending_out_warehouse(i)
        logging.info("常规线路发件出仓功能,响应结果是:")
        logging.info(resp)
        assert_that(resp["code"]).is_equal_to(1)
        assert_that(resp["message"]).is_equal_to("success")
        assert_that(resp["data"]).is_not_empty()
        schema_res = Validate_jsonschema(resp, "sending_out_warehouse.json")
        assert_that(schema_res).is_none()
