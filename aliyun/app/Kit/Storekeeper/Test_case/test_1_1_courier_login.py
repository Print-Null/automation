
from app.Kit.Courier.Script.courier_login import Login
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
import logging
import allure
import pytest
from assertpy import assert_that
logging.basicConfig(level=logging.INFO)


@allure.feature("登入接口")
class Test_Login():

    @allure.title("登入接口")
    @pytest.mark.run(order=1)
    def test_login(self):
        login = Login()
        res = login.login()
        logging.info("快递员登入成功,响应结果是：")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_empty()
        schema_res = Validate_jsonschema(response_result=res, schema_file_name="login.json")
        assert_that(schema_res).is_none()

