import logging

import allure
import pytest
from assertpy import assert_that
# from Storekeeper.Script.unpack import Unpack
# from app.kit.Storekeeper.Script.unpack import Unpack
from app.Kit.Storekeeper.Script.unpack import Unpack


@allure.feature("拆包")
class Test_Unpack():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.unpack = Unpack()

    # list_i = [1, 2, 3, 4]
    #去代码逻辑里修改list_i
    @allure.story("拆包")
    @pytest.mark.run(order=31)
    def test_unpack(self):
        unpack = self.unpack.unpack()
        logging.info("拆包接口响应结果是:")
        logging.info(unpack)
        assert_that(unpack["code"]).is_equal_to(1)
        assert_that(unpack["message"]).is_equal_to("success")
        assert_that(unpack["data"]).is_none()

