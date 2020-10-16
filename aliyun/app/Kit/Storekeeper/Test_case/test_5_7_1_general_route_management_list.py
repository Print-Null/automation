import logging

import pytest
from assertpy import assert_that
import allure

# from app.kit.Storekeeper.Script.general_route_management_list import General_Route_Management_List
from app.Kit.Storekeeper.Script.general_route_management_list import General_Route_Management_List


@allure.feature("常规线路管理列表")
class Test_General_Route_Management_List():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.gen = General_Route_Management_List()

    @pytest.mark.run(order=15)
    def test_general_route_management_list(self):
        res = self.gen.general_route_management_list()
        logging.info("常规线路管理列表,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")

