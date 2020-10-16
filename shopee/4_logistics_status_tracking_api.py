import random
import allure
import pytest
import requests

from shopee.base_api import BaseApi


class TestTracking(BaseApi):
    url = "http://192.168.0.231:8080/callback/shopee/status"

    header = {}

    @allure.feature("测试carrier_tn字段丢失")
    @pytest.mark.run(order=1)
    def test1_order_miss_carrier_tn(self):
        params = {"carrier_tn": "TH20111RKT0Z"}
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试order_carrier_tn字段的异常和正常输入")
    @pytest.mark.parametrize("carrier_tn", ["", None, random.randint(0, 999999999999999), "  ", "\n\t", "a", "maxlen",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenth",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlent",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlen",
                                            "คอนโดซอยลาดพคอนโดซอยล65", "คอนโดซอยลาดพคอนโดซอยล6", False, True,
                                            "คอนโดซอยลาดพคอนโดซอยล", "TH41111RH43Z"])
    @pytest.mark.run(order=2)
    def test2_order_carrier_tn_error_and_good_input(self, carrier_tn):
        params = {"carrier_tn": carrier_tn}
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)
