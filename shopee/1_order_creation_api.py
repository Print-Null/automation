import random
import time
import allure
import pytest

from shopee.base_api import BaseApi


class TestOrder(BaseApi):
    url = "http://192.168.0.231:8080/callback/shopee/order"
    header = {"alg": "HS256",
              "typ": "JWT",
              "account": "AA0425",
              "content-type": "application/json"
              }
    expire_time = int(time.time() + 7200)

    @allure.feature("测试reference_no字段丢失")  # 必填参数丢失报错 -10005,'Parameter logic error'
    @pytest.mark.run(order=1)
    def test1_miss_reference_no(self):
        params = {
            "order": {
                # "reference_no": "a3b4c6",
                "business_type": 1,
                "total_weight": 121.5,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 1,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshangongyuan",
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
                "cod_amount": "50000",
                "schedule_pickup_timeslot": {
                    "start_time": int(time.time()),
                    "end_time": self.expire_time
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试reference_no字段的异常和正常输入")  #
    @pytest.mark.parametrize("reference_no", ["", None, random.randint(0, 999999999999999), "  ", "\n\t", "a", "maxlen",
                                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenth",
                                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlent",
                                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlen",
                                              "คอนโดซอยลาดพคอนโดซอยล65", "คอนโดซอยลาดพคอนโดซอยล6", False, True,
                                              "คอนโดซอยลาดพคอนโดซอยล"])
    @pytest.mark.run(order=2)
    def test2_reference_no_error_and_good_input(self, reference_no):
        params = {
            "order": {
                "reference_no": reference_no,
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试business_type字段丢失")
    @pytest.mark.run(order=3)
    def test3_miss_business_type(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试business_type字段的异常和正常输入")
    @pytest.mark.parametrize("business_type",
                             ["1", "3", "55", None, 0, 1, 2, 3, 5, 6, "", "  ", False, True, "test", "คอน"])
    @pytest.mark.run(order=4)
    def test4_business_type_error_and_good_input(self, business_type):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": business_type,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_name字段丢失")
    @pytest.mark.run(order=5)
    def test5_miss_sender_info_name(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_name字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_name", ["", None, random.randint(0, 9999999999999999), "   ", "\n\t", "a",
                                                  "sender name", "123456789", "@#$%^^&&*%##%%^", False, True, 0, 1, 99,
                                                  "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64c",
                                                  "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64",
                                                  "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth6",
                                                  "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&^",
                                                  "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดa",
                                                  "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด"
                                                  ])
    @pytest.mark.run(order=6)
    def test6_sender_info_name_error_and_good_input(self, sender_info_name):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": sender_info_name,
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยะลา",
                "city": "อำเภอรามัน",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "95140",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยะลา",
                "city": "อำเภอเมืองยะลา",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "95160",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_phone字段丢失")
    @pytest.mark.run(order=7)
    def test7_miss_sender_info_phone(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_phone字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_phone",
                             ["", None, random.randint(0, 999999999999999999999999), "   ", "\n\t",
                              "phonephonephonephon", "a",
                              "Maxlenth64characterM", "Maxlenth64characterMaxle", "Maxlenth64characterMaxl", True,
                              "คอนโดซอย?", "คอนโดซอย", "คอนโดซอ?", "012345678901234567890123", "1", "12", "013", False,
                              "01234567890123456789012", "0123456789012345678901234", "0134665470"])
    @pytest.mark.run(order=8)
    def test8_sender_info_phone_error_and_good_input(self, sender_info_phone):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": sender_info_phone,
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_country字段丢失")
    @pytest.mark.run(order=9)
    def test9_miss_sender_info_country(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_country字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_country",
                             ["", None, random.randint(0, 99), " ", "Max", "ค", "a", "pb", "cn", "Cn", "TH", False,
                              True])
    @pytest.mark.run(order=10)
    def test10_sender_info_country_error_and_good_input(self, sender_info_country):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": sender_info_country,
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_state字段丢失")
    @pytest.mark.run(order=11)
    def test11_miss_sender_info_state(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_state字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_state",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "จังหวัดมหาสารคาม"])
    @pytest.mark.run(order=12)
    def test12_sender_info_state_error_and_good_input(self, sender_info_state):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": sender_info_state,
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_city字段丢失")
    @pytest.mark.run(order=13)
    def test13_miss_sender_info_city(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr yyy",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_city字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_city",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "b58",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "อำเภอหว้านใหญ่"])
    @pytest.mark.run(order=14)
    def test14_sender_info_city_error_and_good_input(self, sender_info_city):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": sender_info_city,
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_detail_address字段丢失")
    @pytest.mark.run(order=15)
    def test15_miss_sender_info_detail_address(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_detail_address字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_detail_address",
                             ["", None, random.randint(0, 9999999999), random.uniform(0, 99999999999), "   ", "\n\t",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64c",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth6",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&^",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด",
                              False, True, "a", "address", "real address"])
    @pytest.mark.run(order=16)
    def test16_sender_info_detail_address_error_and_good_input(self, sender_info_detail_address):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": sender_info_detail_address,
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_remark字段丢失")
    @pytest.mark.run(order=17)
    def test17_miss_sender_info_remark(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": ""
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_remark字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_remark",
                             [None, random.randint(0, 99999), random.uniform(0, 99999), "   ", "\n\t", False, True,
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterM",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64character",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characte",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอน",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอ12",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอ1",
                              "a", "1", "this ia a remark"])
    @pytest.mark.run(order=18)
    def test18_sender_info_remark_error_and_good_input(self, sender_info_remark):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": sender_info_remark
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_name字段丢失")
    @pytest.mark.run(order=19)
    def test19_miss_receiver_info_name(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_name字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_name",
                             ["", None, random.randint(0, 9999999), random.uniform(0, 9999999), "   ", "\n\t", False,
                              True, "receiver name", "a", "1", "123456", "real name",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64c",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth6",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&^",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด"])
    @pytest.mark.run(order=20)
    def test20_receiver_info_name_error_and_good_input(self, receiver_info_name):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": receiver_info_name,
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_phone字段丢失")
    @pytest.mark.run(order=21)
    def test21_miss_receiver_info_phone(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr right",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_phone字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_phone",
                             ["", None, random.randint(0, 999999999999999999999999), "   ", "\n\t",
                              "phonephonephonephon", "a",
                              "Maxlenth64characterM", "Maxlenth64characterMaxle", "Maxlenth64characterMaxl", True,
                              "คอนโดซอย?", "คอนโดซอย", "คอนโดซอ?", "012345678901234567890123", "1", "12", "013", False,
                              "01234567890123456789012", "0123456789012345678901234", "0134665470"])
    @pytest.mark.run(order=22)
    def test22_receiver_info_phone_error_and_good_input(self, receiver_info_phone):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "0134665555",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": receiver_info_phone,
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_country字段丢失")
    @pytest.mark.run(order=23)
    def test23_miss_receiver_info_country(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_country字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_country",
                             ["", None, random.randint(0, 99), " ", "Max", "ค", "a", "pb", "cn", "Cn", "TH", False,
                              True])
    @pytest.mark.run(order=24)
    def test24_receiver_info_country_error_and_good_input(self, receiver_info_country):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": receiver_info_country,
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_state字段丢失")
    @pytest.mark.run(order=25)
    def test25_miss_receiver_info_state(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr yyy",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_state字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_state",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "จังหวัดมหาสารคาม"])
    @pytest.mark.run(order=26)
    def test26_receiver_info_state_error_and_good_input(self, receiver_info_state):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": receiver_info_state,
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_city字段丢失")
    @pytest.mark.run(order=27)
    def test27_miss_receiver_info_city(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr fff",  # Y
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",  # Y
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_city字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_city",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "b58",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "อำเภอหว้านใหญ่"])
    @pytest.mark.run(order=28)
    def test28_receiver_info_city_error_and_good_input(self, receiver_info_city):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": receiver_info_city,
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_detail_address字段丢失")
    @pytest.mark.run(order=29)
    def test29_miss_receiver_info_detail_address(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_detail_address字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_detail_address",
                             ["", None, random.randint(0, 9999999999), random.uniform(0, 99999999999), "   ", "\n\t",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64c",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth6",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&^",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด",
                              False, True, "a", "address", "real address"])
    @pytest.mark.run(order=30)
    def test30_receiver_info_detail_address_error_and_good_input(self, receiver_info_detail_address):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": receiver_info_detail_address,
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_remark字段丢失")
    @pytest.mark.run(order=31)
    def test31_miss_receiver_info_remark(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,  # Y
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",  # Y
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"  # Y
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": ""
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_remark字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_remark",
                             [None, random.randint(0, 99999), random.uniform(0, 99999), "   ", "\n\t", False, True,
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterM",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64character",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characte",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอน",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอ12",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอ1",
                              "a", "1", "this ia a remark"])
    @pytest.mark.run(order=32)
    def test32_receiver_info_remark_error_and_good_input(self, receiver_info_remark):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender_info_remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": receiver_info_remark
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_district字段丢失")
    @pytest.mark.run(order=33)
    def test33_miss_receiver_info_district(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,  # Y
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",  # Y
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"  # Y
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "test"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_district字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_district",
                             ["", None, random.randint(0, 999999), random.uniform(0, 99999), "  ", "\n\t", False, True,
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              "a", "1", "real district"])
    @pytest.mark.run(order=34)
    def test34_receiver_info_district_error_and_good_input(self, receiver_info_district):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender_info_remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": receiver_info_district,
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver_info_remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_zip_code字段丢失")
    @pytest.mark.run(order=35)
    def test35_miss_receiver_info_zip_code(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,  # Y
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",  # Y
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"  # Y
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "longitude": "",
                "latitude": "",
                "remark": "test"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_zip_code字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_zip_code",
                             ["", None, random.randint(0, 99999), random.uniform(0, 99999), "  ", "\n\t", False, 49150,
                              True, "Maxlenth64charact", "Maxlenth64charac", "Maxlenth64chara", "คอนโด16", "คอนโด1",
                              "คอนโด", "888888", "zipcode", "49150"])
    @pytest.mark.run(order=36)
    def test36_receiver_info_zip_code_error_and_good_input(self, receiver_info_zip_code):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender_info_remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "receiver_info_district",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": receiver_info_zip_code,
                "longitude": "",
                "latitude": "",
                "remark": "receiver_info_remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_district字段丢失")
    @pytest.mark.run(order=37)
    def test37_miss_sender_info_district(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,  # Y
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",  # Y
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"  # Y
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "test"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_district字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_district",
                             ["", None, random.randint(0, 999999), random.uniform(0, 99999), "  ", "\n\t", False, True,
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              "a", "1", "real district"])
    @pytest.mark.run(order=38)
    def test38_sender_info_district_error_and_good_input(self, sender_info_district):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": sender_info_district,
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender_info_remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "receiver_info_district",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver_info_remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_zip_code字段丢失")
    @pytest.mark.run(order=39)
    def test39_miss_sender_info_zip_code(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "test"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_zip_code字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_zip_code",
                             ["", None, random.randint(0, 99999), random.uniform(0, 99999), "  ", "\n\t", False, 49150,
                              True, "Maxlenth64charact", "Maxlenth64charac", "Maxlenth64chara", "คอนโด16", "คอนโด1",
                              "คอนโด", "888888", "zipcode", "49150"])
    @pytest.mark.run(order=40)
    def test40_sender_info_zip_code_error_and_good_input(self, sender_info_zip_code):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": sender_info_zip_code,
                "longitude": "",
                "latitude": "",
                "remark": "sender_info_remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "receiver_info_district",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver_info_remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_service_types字段丢失")
    @pytest.mark.run(order=41)
    def test41_miss_service_info_service_types(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,  # Y
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_service_types字段的异常和正常输入")
    @pytest.mark.parametrize("service_info_service_types",
                             ["", None, 11, 12, 13, 21, 22, 23, 24, 31, 32, 33, 34, 35, 36, 41, 42, 43, "   ", "\n\t",
                              False, True, random.uniform(0, 9999), random.randint(1, 99),
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64c",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth6",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&^",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด",
                              "ab", "88", "11", "12", "13", "21", "22", "23", "24", "31", "32", "33", "34", "35", "36",
                              "41", "42", "43", "11,21"])
    @pytest.mark.run(order=42)
    def test42_service_info_service_types_error_and_good_input(self, service_info_service_types):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "receiver_info_detail_address",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": service_info_service_types,
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_start_time字段丢失")
    @pytest.mark.run(order=43)
    def test43_miss_service_info_start_time(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,  # Y
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",  # Y
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "22",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_start_time字段的异常和正常输入")
    @pytest.mark.parametrize("service_info_start_time",
                             ["", None, random.randint(1, 999999999), "   ", "\n\t", False, True, "character", "โดซอยล",
                              "1597931523", int(time.time())])
    @pytest.mark.run(order=44)
    def test44_service_info_start_time_error_and_good_input(self, service_info_start_time):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "receiver_info_detail_address",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": service_info_start_time,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_end_time字段丢失")
    @pytest.mark.run(order=45)
    def test45_miss_service_info_end_time(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "service_types": "11,21",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_end_time字段的异常和正常输入")
    @pytest.mark.parametrize("service_info_end_time",
                             ["", None, random.randint(1, 999999999), "   ", "\n\t", False, True, "character", "โดซอยล",
                              "1597931523", int(time.time()) + 1000])
    @pytest.mark.run(order=46)
    def test46_service_info_end_time_error_and_good_input(self, service_info_end_time):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "sender_info_detail_address",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "receiver_info_detail_address",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": service_info_end_time
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试start_time大于end_time")
    @pytest.mark.parametrize("start_time,end_time",
                             [(int(time.time()), int(time.time() - 300))])
    @pytest.mark.run(order=47)
    def test47_service_info_start_time_greater_end_time(self, start_time, end_time):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": start_time,
                    "end_time": end_time
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试寄件人行政区划信息不一致")
    @pytest.mark.parametrize(
        "sender_info_country,sender_info_state,sender_info_city,sender_info_district,sender_info_zip_code",
        [("CN", "จังหวัดเชียงใหม่", "อำเภอแม่วาง", "chaoyang", "50360"),
         ("CN", "จังหวัดเชียงใหม่", "อำเภอแม่วาง", "chaoyang", "10260"),
         ("TH", "hebei", "zhangjiajie", "chaoyang", "50360"),
         ("TH", "จังหวัดเชียงใหม่", "zhangjiajie", "chaoyang", "50360"),
         ("TH", "hebei", "อำเภอแม่วาง", "chaoyang", "50360"),
         ("TH", "จังหวัดเชียงใหม่", "อำเภอแม่วาง", "chaoyang", "50360")
         ])
    @pytest.mark.run(order=48)
    def test48_sender_info_information_different(self, sender_info_country, sender_info_state, sender_info_city,
                                                 sender_info_district, sender_info_zip_code):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": sender_info_country,
                "state": sender_info_state,
                "city": sender_info_city,
                "district": sender_info_district,
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": sender_info_zip_code,
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试收件人行政区划信息不一致")
    @pytest.mark.parametrize(
        "receiver_info_country,receiver_info_state,receiver_info_city,receiver_info_district,receiver_info_zip_code",
        [("CN", "จังหวัดเชียงใหม่", "อำเภอแม่วาง", "chaoyang", "50360"),
         ("CN", "จังหวัดเชียงใหม่", "อำเภอแม่วาง", "chaoyang", "10260"),
         ("TH", "hebei", "zhangjiajie", "chaoyang", "50360"),
         ("TH", "จังหวัดเชียงใหม่", "zhangjiajie", "chaoyang", "50360"),
         ("TH", "hebei", "อำเภอแม่วาง", "chaoyang", "50360"),
         ("TH", "จังหวัดเชียงใหม่", "อำเภอแม่วาง", "chaoyang", "50360")])
    @pytest.mark.run(order=49)
    def test49_receiver_info_information_different(self, receiver_info_country, receiver_info_state, receiver_info_city,
                                                   receiver_info_district, receiver_info_zip_code):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "yxf",
                "company_name": "My shop",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "US",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "sender_info_district",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": receiver_info_country,
                "state": receiver_info_state,
                "city": receiver_info_city,
                "district": receiver_info_district,
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": receiver_info_zip_code,
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    # 非必填字段
    @allure.feature("测试carrier_tn字段丢失")
    @pytest.mark.run(order=50)
    def test50_order_miss_carrier_tn(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试order_carrier_tn字段的异常和正常输入")
    @pytest.mark.parametrize("carrier_tn", ["", None, random.randint(0, 999999999999999), "  ", "\n\t", "a", "maxlen",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenth",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlent",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlen",
                                            "คอนโดซอยลาดพคอนโดซอยล65", "คอนโดซอยลาดพคอนโดซอยล6", False, True,
                                            "คอนโดซอยลาดพคอนโดซอยล"])
    @pytest.mark.run(order=51)
    def test51_order_carrier_tn_error_and_good_input(self, carrier_tn):
        params = {
            "order": {
                "reference_no": "reference_no",
                "carrier_tn": carrier_tn,
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试total_weight字段丢失")
    @pytest.mark.run(order=52)
    def test52_order_miss_total_weight(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "carrier_tn": "abc",
                "business_type": 1,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试order_total_weight字段的异常和正常输入")
    @pytest.mark.parametrize("total_weight", ["", None, str(random.randrange(10, 50000, 10)), "  ", "\n\t", "a", "max",
                                              False, True, "0", str(round(random.uniform(0, 50000), 2)), 0, 1, 10, "1",
                                              49999, 50000, 50001, "49999", "50000", "50001", 122.1, 155.55, "122.1",
                                              "155.55"])
    @pytest.mark.run(order=53)
    def test53_order_total_weight_error_and_good_input(self, total_weight):
        params = {
            "order": {
                "reference_no": "reference_no",
                "carrier_tn": "carrier_tn",
                "business_type": 1,
                "total_weight": total_weight,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    # goods_value改为必填字段
    @allure.feature("测试goods_value字段丢失")
    @pytest.mark.run(order=54)
    def test54_order_miss_goods_value(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "carrier_tn": "abc",
                "business_type": 1,
                "total_weight": 195.5
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试order_goods_value字段的异常和正常输入")
    @pytest.mark.parametrize("goods_value",
                             ["", None, str(random.randrange(10, 50000, 10)), "  ", "\n\t", "a", "max", "122.1",
                              False, True, "0", str(round(random.uniform(0, 50000), 2)), 0, 0.01, "0.01", 0.02, "0.02",
                              "0", 1, "1", 49999, 50000, 50001, "49999", "50000", "50001", 122.1, 155.55, "155.55"])
    @pytest.mark.run(order=55)
    def test55_order_goods_value_error_and_good_input(self, goods_value):
        params = {
            "order": {
                "reference_no": "reference_no",
                "carrier_tn": "carrier_tn",
                "business_type": 1,
                "total_weight": 155,
                "goods_value": goods_value
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "My shop",
                "sender_id": "AA0425",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
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
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_company_name字段丢失")
    @pytest.mark.run(order=56)
    def test56_miss_sender_info_company_name(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_company_name字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_company_name",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=57)
    def test57_sender_info_company_name_error_and_good_input(self, sender_info_company_name):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": sender_info_company_name,
                "sender_id": "abc12367",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอเมืองเชียงใหม่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50200",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_sender_id字段丢失")
    @pytest.mark.run(order=58)
    def test58_miss_sender_info_sender_id(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",  # Y
                "email": "",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_sender_id字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_sender_id",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=59)
    def test59_sender_info_sender_id_error_and_good_input(self, sender_info_sender_id):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": sender_info_sender_id,
                "email": "",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_email字段丢失")
    @pytest.mark.run(order=60)
    def test60_miss_sender_info_email(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_email字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_email",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=61)
    def test61_sender_info_email_error_and_good_input(self, sender_info_email):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": sender_info_email,
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_subdistrict字段丢失")
    @pytest.mark.run(order=62)
    def test62_miss_sender_info_subdistrict(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_subdistrict字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_subdistrict",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=63)
    def test63_sender_info_subdistrict_error_and_good_input(self, sender_info_subdistrict):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": sender_info_subdistrict,
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_street字段丢失")
    @pytest.mark.run(order=64)
    def test64_miss_sender_info_street(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",  # Y
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_street字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_street",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=65)
    def test65_sender_info_street_error_and_good_input(self, sender_info_street):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",  # Y
                "subdistrict": "sender_info_subdistrict",
                "street": sender_info_street,
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_longitude字段丢失")
    @pytest.mark.run(order=66)
    def test66_miss_sender_info_longitude(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_longitude字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_longitude",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              False, True, "real state"])
    @pytest.mark.run(order=67)
    def test67_sender_info_longitude_error_and_good_input(self, sender_info_longitude):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",  # Y
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": sender_info_longitude,
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_latitude字段丢失")
    @pytest.mark.run(order=68)
    def test68_miss_sender_info_latitude(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_latitude字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_latitude",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              False, True, "real state"])
    @pytest.mark.run(order=69)
    def test69_sender_info_latitude_error_and_good_input(self, sender_info_latitude):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",  # Y
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "sender_info_longitude",
                "latitude": sender_info_latitude,
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_email字段丢失")
    @pytest.mark.run(order=70)
    def test70_miss_receiver_info_email(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_email字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_email",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=71)
    def test71_receiver_info_email_error_and_good_input(self, receiver_info_email):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
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
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": receiver_info_email,
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_subdistrict字段丢失")
    @pytest.mark.run(order=72)
    def test72_miss_receiver_info_subdistrict(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_subdistrict字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_subdistrict",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=73)
    def test73_receiver_info_subdistrict_error_and_good_input(self, receiver_info_subdistrict):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": receiver_info_subdistrict,
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_street字段丢失")
    @pytest.mark.run(order=74)
    def test74_miss_receiver_info_street(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_street字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_street",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxle",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxl",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMax",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคab",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคa",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพค",
                              False, True, "real state"])
    @pytest.mark.run(order=75)
    def test75_receiver_info_street_error_and_good_input(self, receiver_info_street):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": receiver_info_street,
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_longitude字段丢失")
    @pytest.mark.run(order=76)
    def test76_miss_receiver_info_longitude(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",  # Y
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",  # Y
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_longitude字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_longitude",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              False, True, "real state"])
    @pytest.mark.run(order=77)
    def test77_receiver_info_longitude_error_and_good_input(self, receiver_info_longitude):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "sender_info_longitude",
                "latitude": "",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": receiver_info_longitude,
                "latitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_latitude字段丢失")
    @pytest.mark.run(order=78)
    def test78_miss_receiver_info_latitude(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_latitude字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_latitude",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              False, True, "real state"])
    @pytest.mark.run(order=79)
    def test79_receiver_info_latitude_error_and_good_input(self, receiver_info_latitude):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "longitude": "sender_info_longitude",
                "latitude": "sender_info_latitude",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": receiver_info_latitude,
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_branch_id字段丢失")
    @pytest.mark.run(order=80)
    def test80_miss_receiver_info_branch_id(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试receiver_info_branch_id字段的异常和正常输入")
    @pytest.mark.parametrize("receiver_info_branch_id",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              False, True, "real state"])
    @pytest.mark.run(order=81)
    def test81_receiver_info_branch_id_error_and_good_input(self, receiver_info_branch_id):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "sender_info_longitude",
                "latitude": "sender_info_latitude",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "receiver_info_latitude",
                "remark": "receiver remark",
                "branch_id": receiver_info_branch_id
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": round(random.uniform(0.01, 50000), 2),
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    # cod_amount是必填字段
    @allure.feature("测试service_info_cod_amount字段丢失")
    @pytest.mark.run(order=82)
    def test82_miss_service_info_cod_amount(self):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr xxx",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมุกดาหาร",
                "city": "อำเภอหว้านใหญ่",
                "district": "nanshan",
                "detail_address": "abc xyz",
                "zip_code": "49150",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "remark": "receiver remark"
            },
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_cod_amount字段的异常和正常输入")
    @pytest.mark.parametrize("service_info_cod_amount",
                             ["", None, random.randint(0, 50000), round(random.uniform(0.01, 50000), 2), "  ", "\n\t",
                              "a", "a23", str(random.randint(0, 50000)), str(round(random.uniform(0.01, 50000), 2)),
                              False, True, "real state", 0, "0", "0.00", 0.00, 0.01, "0.01", 49999, "49999", 50000,
                              "50000", 50001, "50001", 50002, "50002", 60000, "88888"])
    @pytest.mark.run(order=83)
    def test83_service_info_cod_amount_error_and_good_input(self, service_info_cod_amount):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "sender_info_longitude",
                "latitude": "sender_info_latitude",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "receiver_info_latitude",
                "remark": "receiver remark",
                "branch_id": "receiver_info_branch_id"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": service_info_cod_amount,
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("service_info_service_types为11,cod_amount字段必传(cod取值0.01-50000或者'0.01-50000')")
    @pytest.mark.parametrize("service_info_service_types,service_info_cod_amount",
                             [(11, random.uniform(0.01, 50000)), ("11", str(random.uniform(0.01, 50000))),
                              (11, str(random.uniform(0.01, 50000))), ("11", random.uniform(0.01, 50000))])
    @pytest.mark.run(order=84)
    def test84_service_info_cod_amount_error_and_good_input(self, service_info_service_types, service_info_cod_amount):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "sender_info_longitude",
                "latitude": "sender_info_latitude",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "receiver_info_latitude",
                "remark": "receiver remark",
                "branch_id": "receiver_info_branch_id"
            },
            "service_info": {
                "service_types": service_info_service_types,
                "cod_amount": service_info_cod_amount
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("service_info_service_types为21,schedule_pickup_date_time字段必传")
    @pytest.mark.parametrize("service_types,schedule_pickup_date_time",
                             [(21, random.uniform(0.01, 50000)), ("21", str(random.uniform(0.01, 50000))),
                              (21, str(random.uniform(0.01, 50000))), ("21", random.uniform(0.01, 50000)),
                              ("98", "aaaaa"), (188, "123456789"), ("aa", "55.5"), ("aa", 55.5), ("bb", "565")
                              ])
    @pytest.mark.run(order=85)
    def test85_service_info_cod_amount_error_and_good_input(self, service_types, schedule_pickup_date_time):
        params = {
            "order": {
                "reference_no": "aaaabbbbcccc",
                "business_type": 1,
                "total_weight": 121,
                "goods_value": "22.1"
            },
            "item_info": [{
                "item_name": "example",
                "item_quantity": 2,
                "length": 12,
                "width": 9,
                "height": 5
            }],
            "sender_info": {
                "name": "Mr O",
                "company_name": "sender_info_company_name",
                "sender_id": "sender_info_sender_id",
                "email": "sender_info_email",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดเชียงใหม่",
                "city": "อำเภอแม่วาง",
                "district": "nanshan",
                "subdistrict": "sender_info_subdistrict",
                "street": "sender_info_street",
                "detail_address": "abc xyz",
                "zip_code": "50360",
                "longitude": "sender_info_longitude",
                "latitude": "sender_info_latitude",
                "remark": "sender remark"
            },
            "receiver_info": {
                "name": "Mr R",
                "email": "",
                "phone": "+86 1234567",
                "country": "TH",
                "state": "จังหวัดมหาสารคาม",
                "city": "อำเภอยางสีสุราช",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "44210",
                "longitude": "",
                "latitude": "receiver_info_latitude",
                "remark": "receiver remark",
                "branch_id": "receiver_info_branch_id"
            },
            "service_info": {
                "service_types": service_types,
                "schedule_pickup_date_time": schedule_pickup_date_time
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)
