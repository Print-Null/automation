import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.warehousing_vehicle_voucher_check import Warehousing_Vehicle_Voucher_Check
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.warehousing_vehicle_voucher_check import Warehousing_Vehicle_Voucher_Check
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.warehousing_vehicle_voucher_check import Warehousing_Vehicle_Voucher_Check


@allure.feature("到件入仓")
class Test_Warehousing_Vehicle_Voucher_Check():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.ware = Warehousing_Vehicle_Voucher_Check()
    @allure.story("到件入仓->出车凭证校验")
    @pytest.mark.run(order=27)
    def test_warehousing_vehicle_voucher_check(self):
        res = self.ware.warehousing_vehicle_voucher_check()
        logging.info("到件入仓->出车凭证校验,响应结果:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_not_empty()
        schema_res = Validate_jsonschema(res, "warehousing_vehicle_voucher_check.json")
        assert_that(schema_res).is_none()