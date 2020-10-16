import logging
import allure
import pytest
from assertpy import assert_that
from app.Kit.Storekeeper.Script.pre_problem_piece_COD_price_err import Pre_Problem_Piece_COD_Price_Err


@allure.feature("交接前，问题件提交,COD金额不正确")
class Test_Pre_Problem_Piece_COD_Price_err():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = Pre_Problem_Piece_COD_Price_Err()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #将第一个订单，来进行此接口,不需要修改list_i
    list_i = [6]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接前，问题件提交,COD金额不正确")
    @allure.story("交接前，问题件提交,COD金额不正确")
    @pytest.mark.run(order=37)
    def test_pre_problem_piece_cod_price_err(self,i):
        res = self.pre.pre_problem_piece_cod_price_err(i)
        logging.info("交接前，问题件提交,COD金额不正确,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()
