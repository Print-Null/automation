import logging

import allure
import pytest
from assertpy import assert_that

# from Storekeeper.Script.package_seal_true import Package_seal_True
# from app.kit.Storekeeper.Script.package_seal_true import Package_seal_True
from app.Kit.Storekeeper.Script.package_seal_true import Package_seal_True


@allure.feature("集包接口-集包成功")
class Test_Package_Seal_True():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.seal = Package_seal_True()

    # list_i = [1, 2, 3, 4],去代码逻辑层修改list_i
    @allure.story("集包功能->集包成功")
    @pytest.mark.run(order=7)
    def test_package_seal_true(self):
        result = self.seal.package_seal_true()
        logging.info("集包返回结果为：")
        logging.info(result)
        first_res = result[0]
        sec_res = result[1]
        logging.info(first_res)
        logging.info(sec_res)
        assert_that(first_res["code"]).is_equal_to(1)
        assert_that(first_res["message"]).is_equal_to("success")
        assert_that(first_res["data"]).is_none()

        assert_that(sec_res["code"]).is_equal_to(1)
        assert_that(sec_res["message"]).is_equal_to("success")
        assert_that(sec_res["data"]).is_none()

