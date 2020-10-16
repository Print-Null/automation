import logging

import allure
import pytest
from assertpy import assert_that

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.delivery_confirm_deliveryReward import Delivery_Confirm_DeliveryReward
# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.delivery_confirm_deliveryReward import Delivery_Confirm_DeliveryReward
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.delivery_confirm_deliveryReward import Delivery_Confirm_DeliveryReward


@allure.feature("确认妥投后-收入金额提示")
class Test_Delivery_Confirm_DeliveryReward():
    logging.basicConfig(level=logging.INFO)
    def setup(self):
        self.reward = Delivery_Confirm_DeliveryReward()

    # list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 将第一个订单，来进行此接口

    list_i = [17]

    @pytest.mark.parametrize("i", list_i)
    @allure.story("确认妥投后-收入金额提示")
    @allure.title("确认妥投后-收入金额提示")
    @pytest.mark.run(order=50)
    def test_delivery_confirm_deliveryReward(self,i):
        res = self.reward.delivery_confirm_deliveryReward(i)
        logging.info("确认妥投后-收入金额提示,接口响应结果是:")
        logging.info(res)
        assert_that(res["code"]).is_equal_to(1)
        assert_that(res["msg"]).is_equal_to("成功")
        assert_that(res["data"]).is_not_none()
        schema_res = Validate_jsonschema(res, "delivery_confirm_deliveryReward.json")
        assert_that(schema_res).is_none()

