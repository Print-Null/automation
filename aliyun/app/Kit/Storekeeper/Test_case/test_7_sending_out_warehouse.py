import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.sending_out_warehouse import Sending_Out_Warehouse
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.sending_out_warehouse import Sending_Out_Warehouse
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.sending_out_warehouse import Sending_Out_Warehouse


@allure.feature("虚拟线路发件出仓接口")
class est_Sending_Out_Warehouse():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.sending = Sending_Out_Warehouse()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    list_i = [9]
    @pytest.mark.parametrize("i",list_i)
    @allure.story("虚拟线路发件出仓功能")
    @pytest.mark.run(order=20)
    def est_sending_out_warehouse(self, i):
        resp = self.sending.sending_out_warehouse(i)
        logging.info("虚拟线路发件出仓功能,响应结果是:")
        logging.info(resp)
        assert_that(resp["code"]).is_equal_to(1)
        assert_that(resp["message"]).is_equal_to("success")
        assert_that(resp["data"]).is_not_empty()
        schema_res = Validate_jsonschema(resp, "sending_out_warehouse.json")
        assert_that(schema_res).is_none()


