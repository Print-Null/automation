import logging
import allure
import pytest
from assertpy import assert_that
# from Storekeeper.Script.after_problem_piece_damaged_outer_package import After_Problem_Piece_Damaged_Outer_Package
# from app.kit.Storekeeper.Script.after_problem_piece_damaged_outer_package import \
    # After_Problem_Piece_Damaged_Outer_Package

from app.Kit.Storekeeper.Script.after_problem_piece_damaged_outer_package import \
    After_Problem_Piece_Damaged_Outer_Package


@allure.feature("交接后，外包装破损")
class Test_After_Problem_Piece_Damaged_Out_Package():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.pre = After_Problem_Piece_Damaged_Outer_Package()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口,不需要修改list_i
    list_i = [12]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("交接后，外包装破损")
    @allure.story("交接后，外包装破损")
    @pytest.mark.run(order=43)
    def test_after_problem_piece_damaged_outer_package(self,i):
        res = self.pre.after_problem_piece_damaged_outer_package(i)
        logging.info("交接后，外包装破损，接口响应结果是：")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()

