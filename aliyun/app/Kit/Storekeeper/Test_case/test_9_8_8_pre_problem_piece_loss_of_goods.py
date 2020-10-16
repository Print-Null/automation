import logging

import allure
import pytest
from assertpy import assert_that
from app.Kit.Storekeeper.Script.pre_problem_piece_loss_of_goods import Pre_Problem_Piece_Loss_Of_Goods


@allure.feature("交接前，问题件提交，货物丢失")
class Test_Pre_Problem_Piece_Loss_Of_goods():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = Pre_Problem_Piece_Loss_Of_Goods()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [7]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接前，问题件提交，货物丢失")
    @allure.story("交接前，问题件提交，货物丢失")
    @pytest.mark.run(order=38)
    def test_pre_problem_piece_loss_of_goods(self,i):
        res = self.pre.pre_problem_piece_loss_of_goods(i)
        logging.info("交接前，问题件提交，货物丢失")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()
