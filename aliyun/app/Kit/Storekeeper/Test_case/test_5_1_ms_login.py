import logging
import allure
import pytest
from assertpy import assert_that
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.ms_login import Ms_Login


@allure.feature("ms后台登入功能 ")
class Test_Ms_Login():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ms = Ms_Login()
    @allure.story("ms后台登入功能")
    @pytest.mark.run(order=9)
    def test_ms_login(self):
        resp = self.ms.ms_login()
        logging.info("ms后台登入接口,响应结果是:")
        logging.info(resp)
        assert_that(resp["code"]).is_equal_to(1)
        assert_that(resp["message"]).is_equal_to("success")
        assert_that(resp["data"]).is_not_empty()
        schema_res = Validate_jsonschema(resp, "ms_login.json")
        assert_that(schema_res).is_none()

