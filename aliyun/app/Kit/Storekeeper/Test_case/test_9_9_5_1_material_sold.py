import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.material_sold import Material_Sold
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.material_sold import Material_Sold
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.material_sold import Material_Sold


@allure.feature("卖包材 -> S包材")
class Test_Material_Sold():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.material = Material_Sold()

    @allure.story("卖包材 -> S包材")
    @pytest.mark.run(order=51)
    def test_material_sold(self):
        res = self.material.material_sold()
        logging.info("卖包材 -> S包材，接口响应结果是：")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "material_sold.json")
        assert_that(schema_res).is_none()




