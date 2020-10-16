import logging

import allure
import pytest
from assertpy import assert_that

# from Storekeeper.Script.package_seal_false import Package_seal_False
# from app.kit.Storekeeper.Script.package_seal_false import Package_seal_False
from app.Kit.Storekeeper.Script.package_seal_false import Package_seal_False


@allure.feature("集包接口-将集包号设为无效")
class est_Package_Seal_False():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.seal = Package_seal_False()

    # list_i = [1, 2, 3, 4],去代码逻辑层修改list_i
    @allure.story("集包功能->集包成功")
    @pytest.mark.run(order=8)
    def est_package_seal_false(self):
        result = self.seal.package_seal_false()
        logging.info("集包返回结果为：")
        logging.info(result)
        assert_that(result["code"]).is_equal_to(1)
        assert_that(result["message"]).is_equal_to("success")
        assert_that(result["data"]).is_none()

