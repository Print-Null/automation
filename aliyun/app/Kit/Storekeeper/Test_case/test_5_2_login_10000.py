import logging

import allure
import pytest
from assertpy import assert_that
# from app.kit.Storekeeper.Script.login_10000 import Login_10000
from app.Kit.Storekeeper.Script.login_10000 import Login_10000


@allure.feature("10000号登入")
class Test_Login_10000():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.login = Login_10000()

    @pytest.mark.run(order=10)
    def test_10000(self):
        res = self.login.login_10000()
        logging.info("10000号登入,响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")



