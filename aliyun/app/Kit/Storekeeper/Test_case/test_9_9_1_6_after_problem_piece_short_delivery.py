import logging
import allure
import pytest
from assertpy import assert_that
# from Storekeeper.Script.after_problem_piece_short_delivery import After_Problem_Piece_Short_Delivery
# from app.kit.Storekeeper.Script.after_problem_piece_short_delivery import After_Problem_Piece_Short_Delivery
from app.Kit.Storekeeper.Script.after_problem_piece_short_delivery import After_Problem_Piece_Short_Delivery


@allure.feature("交接后，货物短少")
class Test_After_Problem_Piece_Short_Delivery():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = After_Problem_Piece_Short_Delivery()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [14]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接后，货物短少")
    @allure.story("交接后，货物短少")
    @pytest.mark.run(order=45)
    def test_after_problem_piece_short_delivery(self,i):
        res = self.pre.after_problem_piece_short_delivery(i)
        logging.info("交接后，货物短少,接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()