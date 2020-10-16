import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Script.collect_complete import Collect_Complete
# from app.kit.Courier.Script.collect_complete import Collect_Complete
from app.Kit.Courier.Script.collect_complete import Collect_Complete


@allure.feature("揽收完成")
class Test_Collect_Complete():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.collect = Collect_Complete()

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @pytest.mark.parametrize("i",list_i)
    @allure.story("揽收完成")
    @pytest.mark.run(order=3)
    def test_collect_complete(self, i):
        res = self.collect.collect_complete(i)
        logging.info("揽收完成接口,响应结果是:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["message"]).is_equal_to("success")
        assert_that(res["data"]).is_none()