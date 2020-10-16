import logging

import allure
import pytest
from assertpy import assert_that
# from Storekeeper.Script.after_storage_of_goods_inadequate import After_Storage_Of_Goods_Inadequate
# from app.kit.Storekeeper.Script.after_storage_of_goods_inadequate import After_Storage_Of_Goods_Inadequate
from app.Kit.Storekeeper.Script.after_storage_of_goods_inadequate import After_Storage_Of_Goods_Inadequate


@allure.feature("交接后-货件留仓-运力不足-快递员角色")
class Test_After_Storage_Of_Goods_Inadequate():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.af = After_Storage_Of_Goods_Inadequate()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #将第一个订单，来进行此接口,不需要修改list_i
    list_i = [10]

    @pytest.mark.parametrize("i", list_i)
    @allure.title("运力不足")
    @allure.story("交接后-货件留仓-运力不足")
    @pytest.mark.run(order=41)
    def test_after_storage_of_goods_inadequate(self, i):
        res = self.af.after_storage_of_goods_inadequate(i)
        logging.info("交接后-货件留仓-运力不足-快递员，接口响应结果是：")
        logging.info(res.json())
        assert_that(res.status_code).is_equal_to(200)
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_none()

