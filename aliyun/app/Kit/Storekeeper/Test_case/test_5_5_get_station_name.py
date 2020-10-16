import logging

import pytest
from assertpy import assert_that
import allure

# from app.kit.Storekeeper.Script.get_station_name import Get_Station_Name
from app.Kit.Storekeeper.Script.get_station_name import Get_Station_Name


@allure.feature("获取站名")
class Test_Get_Station_Name():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.name = Get_Station_Name()

    @pytest.mark.run(order=13)
    def test_get_station_name(self):
        res = self.name.get_station_name()
        logging.info("获取站名,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_empty()

