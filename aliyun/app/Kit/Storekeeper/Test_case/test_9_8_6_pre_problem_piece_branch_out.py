import logging

import allure
import pytest
from assertpy import assert_that
from app.Kit.Storekeeper.Script.pre_problem_piece_branch_out import Pre_Problem_Piece_Branch_Out


@allure.feature("交接前，问题件提交，分错网点")
class Test_Pre_Problem_Piece_Branch_Out():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = Pre_Problem_Piece_Branch_Out()


    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [5]
    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接前，问题件提交，分错网点")
    @allure.story("交接前，问题件提交，分错网点")
    @pytest.mark.run(order=36)
    def test_pro_problem_piece_branch_out(self, i):
        res = self.pre.pro_problem_piece_branch_out(i)
        logging.info("交接前，问题件提交，分错网点,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()
