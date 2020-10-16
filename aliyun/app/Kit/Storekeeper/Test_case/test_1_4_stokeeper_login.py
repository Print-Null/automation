import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.storekeeper_login import Storekeeper_Login
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.storekeeper_login import Storekeeper_Login
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.storekeeper_login import Storekeeper_Login


@allure.feature("仓管员登入")
class Test_Storekeeper_Login():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.storekeeper = Storekeeper_Login()
    @allure.story("仓管员登入")
    @pytest.mark.run(order=4)
    def test_storekeeper_login(self):
        response = self.storekeeper.storekeeper_login()
        logging.info("仓管员登入成功,响应结果是:")
        logging.info(response)
        assert_that(response["code"]).is_equal_to(1)
        assert_that(response["message"]).is_equal_to("success")
        assert_that(response["data"]).is_not_empty()
        schema_res = Validate_jsonschema(response, "storekeeper_login.json")
        assert_that(schema_res).is_none()




