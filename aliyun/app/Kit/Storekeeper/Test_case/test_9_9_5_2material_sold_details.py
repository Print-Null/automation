import logging

import allure
#
# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.material_sold_details import Material_Sold_Details
import pytest
from assertpy import assert_that

# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.material_sold_details import Material_Sold_Details
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.material_sold_details import Material_Sold_Details


@allure.feature("已售卖包材列表")
class Test_Material_Sold_Details():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.material = Material_Sold_Details()
    @allure.story("已售卖包材列表")
    @pytest.mark.run(order=52)
    def test_material_sold_details(self):
        res = self.material.material_sold_details()
        logging.info("已售卖包材列表，响应结果是：")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "material_sold_details.json")
        assert_that(schema_res).is_none()
