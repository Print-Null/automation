import logging

import pytest
from assertpy import assert_that
import allure
from app.Kit.Storekeeper.Script.unpacking_pack_num_check import Unpacking_Pack_Num_Check


@allure.feature("拆包功能->集包号码检查")
class Test_Unpacking_Pack_Num_Check():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.unpack = Unpacking_Pack_Num_Check()

    @allure.story("拆包功能->集包号码检查")
    @pytest.mark.run(order=30)
    def test_unpacking_pack_num_check(self):
        res = self.unpack.unpacking_pack_num_check()
        logging.info("拆包功能->集包号码检查,响应结果是:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_none()
        # schema_res = Validate_jsonschema(res, "unpacking_pack_num_check.json")
        # assert_that(schema_res).is_none()


