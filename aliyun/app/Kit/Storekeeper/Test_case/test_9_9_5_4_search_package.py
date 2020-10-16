import logging
import allure
import pytest
from assertpy import assert_that
# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.search_package import Search_Pachage
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.search_package import Search_Pachage
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.search_package import Search_Pachage


@allure.feature("查集包")
class Test_Search_Package():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ser = Search_Pachage()
    @allure.title("查集包")
    @allure.story("查集包")
    @pytest.mark.run(order=54)
    def test_search_package(self):
        res = self.ser.search_package()
        logging.info("查集包，接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
        # schema_res = Validate_jsonschema(res.json(), "search_package.json")
        # assert_that(schema_res).is_none()


