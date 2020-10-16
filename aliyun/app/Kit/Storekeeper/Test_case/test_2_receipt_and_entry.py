import allure
import pytest

# from Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from Storekeeper.Script.receipt_and_entry import Receipt_And_Entry
from assertpy import assert_that

# from app.kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
# from app.kit.Storekeeper.Script.receipt_and_entry import Receipt_And_Entry
from app.Kit.Courier.Utils.jsonschema_valitate import Validate_jsonschema
from app.Kit.Storekeeper.Script.receipt_and_entry import Receipt_And_Entry


@allure.feature("收件入仓")
class Test_Receipt_and_entry():
    def setup(self):
        self.receipt = Receipt_And_Entry()

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    @allure.story("收件入仓")
    @pytest.mark.parametrize("i", list_i)
    @pytest.mark.run(order=5)
    def test_receipt_and_entry(self, i):
        resp = self.receipt.receipt_and_entry(i)
        assert_that(resp["code"]).is_equal_to(1)
        assert_that(resp["message"]).is_equal_to("success")
        assert_that(resp["data"]).is_not_empty()
        validata_res = Validate_jsonschema(resp, "receipt_and_entry.json")
        assert_that(validata_res).is_none ()