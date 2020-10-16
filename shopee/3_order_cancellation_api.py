import random
import allure
import pytest
import requests
from common import base
from common.base import BaseTestCase
from shopee.base_api import BaseApi


class TestOrderCancel(BaseApi):
    url = "http://192.168.0.231:8080/callback/shopee/cancel"
    header = {"alg": "HS256",
              "typ": "JWT",
              "account": "AA0425",
              "content-type": "application/json"
              }

    @allure.feature("测试carrier_tn字段丢失")
    @pytest.mark.run(order=1)
    def test1_order_miss_carrier_tn(self):
        params = {"carrier_tn": "TH41111RH43Z"}
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试order_carrier_tn字段的异常和正常输入")
    @pytest.mark.parametrize("carrier_tn", ["", None, random.randint(0, 999999999999999), "  ", "\n\t", "a", "maxlen",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenth",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlent",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlen",
                                            "คอนโดซอยลาดพคอนโดซอยล65", "คอนโดซอยลาดพคอนโดซอยล6", False, True,
                                            "คอนโดซอยลาดพคอนโดซอยล", "TH47221RD39Z"])
    @pytest.mark.run(order=2)
    def test2_order_carrier_tn_error_and_good_input(self, carrier_tn):
        params = {
            "carrier_tn": carrier_tn
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("取消已揽收的订单")
    @pytest.mark.run(order=38)
    def test38_modify_pickup_order(self):
        url_order = "http://192.168.0.231:8080/callback/shopee/order"
        params_order = {
            "order": {
                "reference_no": "a3b4c5999",
                "business_type": 1,
                "total_weight": 1.0,
                "goods_value": "2.5"
            },
            "item_info": [{
                "item_name": "item1",
                "item_quantity": 1,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "shopee",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "2516352482",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "123123",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "0135454545",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": 0.0111111111
            }
        }
        self.send_assert_and_save(url=url_order, headers=self.header, data=params_order)
        order_id = base.RedisBase().get("order_creation_api_0")
        staff_info_id = self.get_staff_info_id(order_id)
        kit_login_url = "http://192.168.0.228:8080/api/courier/v1/auth/new_device_login"
        kit_login_header = {"Accept-Language": "zh-CN",
                            "content-type": "application/json; charset=UTF-8"}
        kit_login_params = {
            "login": staff_info_id,
            "password": 123456,
            "clientid": "8627020338716801594109392016",
            "clientsd": "1594109392016",
            "os": "android",
            "version": "3.2.5"
        }
        kit_res = requests.post(url=kit_login_url, headers=kit_login_header, json=kit_login_params)
        session_id = kit_res.json()["data"]["sessionid"]

    @allure.feature("取消已取消的订单")
    @pytest.mark.run(order=38)
    def test38_modify_pickup_order(self):
        url_order = "http://192.168.0.231:8080/callback/shopee/order"
        params_order = {
            "order": {
                "reference_no": "a3b4c5999",
                "business_type": 1,
                "total_weight": 1.0,
                "goods_value": "2.5"
            },
            "item_info": [{
                "item_name": "item1",
                "item_quantity": 1,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "shopee",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "2516352482",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "123123",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "0135454545",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": 0.0111111111
            }
        }
        self.send_assert_and_save(url=url_order, headers=self.header, data=params_order)
        order_id = base.RedisBase().get("order_creation_api_0")
        print(order_id)
        params_cancel = {"carrier_tn": order_id}
        self.send_assert_and_save(url=self.url, headers=self.header, data=params_cancel)
        print("取消已取消订单的失败提示:%s" % self.send_assert_and_save(url=self.url, headers=self.header, data=params_cancel))
