import random
import time
import allure
import pytest
import requests

from common import base
import pymysql

from shopee.base_api import BaseApi


class TestOrderUpdate(BaseApi):
    url = "http://192.168.0.231:8080/callback/shopee/update"
    header = {"alg": "HS256",
              "typ": "JWT",
              "account": "AA0425",
              "Accept - Language": "zh-CN",
              "content-type": "application/json"
              }
    carrier_tn = "TH47221RGU6Z"

    # 必填字段测试
    @allure.feature("测试carrier_tn字段丢失")
    @pytest.mark.run(order=1)
    def test1_order_miss_carrier_tn(self):
        params = {
            "carrier_tn": "TH41111RH43Z",
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",  # Y,str,1024
                "cod_amount": "22.2"
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试order_carrier_tn字段的异常和正常输入")
    @pytest.mark.parametrize("carrier_tn", ["", None, random.randint(0, 999999999999999), "  ", "\n\t", "a", "maxlen",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenth",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlent",
                                            "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlen",
                                            "คอนโดซอยลาดพคอนโดซอยล65", "คอนโดซอยลาดพคอนโดซอยล6", False, True,
                                            "คอนโดซอยลาดพคอนโดซอยล", carrier_tn])
    @pytest.mark.run(order=2)
    def test2_order_carrier_tn_error_and_good_input(self, carrier_tn):
        params = {
            "carrier_tn": carrier_tn,  # Y,str,64
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "21",  # Y,str,1024
                "schedule_pickup_date_time": 123456789
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_service_types字段丢失")
    @pytest.mark.run(order=3)
    def test3_miss_service_info_service_types(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_service_types字段的异常和正常输入")
    @pytest.mark.parametrize("service_info_service_types",
                             ["", None, 11, 21, 22, 42, 43, "   ", "\n\t", False, True, random.uniform(0, 9999),
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64c",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64",
                              "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth6",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&^",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&",
                              "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด",
                              "ab", "88", "11", "12", "13", "21", "22", "23", "24", "31", "32", "33", "34", "35", "36",
                              "41", "42", "43", "11,21"])
    @pytest.mark.run(order=4)
    def test4_service_info_service_types_error_and_good_input(self, service_info_service_types):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": service_info_service_types,
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_start_time字段丢失")
    @pytest.mark.run(order=5)
    def test5_miss_service_info_start_time(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
                "schedule_pickup_timeslot": {
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_start_time字段的异常和正常输入")
    @pytest.mark.parametrize("service_info_start_time",
                             ["", None, random.randint(1, 999999999), "  ", "\n\t", False, True, "character", "โดซอยล",
                              "1597931523", int(time.time()), random.uniform(0, 999999), str(random.uniform(0, 99999))])
    @pytest.mark.run(order=6)
    def test6_service_info_start_time_error_and_good_input(self, service_info_start_time):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
                "schedule_pickup_timeslot": {
                    "start_time": service_info_start_time,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_end_time字段丢失")
    @pytest.mark.run(order=7)
    def test7_miss_service_info_end_time(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试service_info_end_time字段的异常和正常输入")
    @pytest.mark.parametrize("service_info_end_time",
                             ["", None, random.randint(1, 999999999), "  ", "\n\t", False, True, "character", "โดซอยล",
                              "1597931523", int(time.time()), random.uniform(0, 999999), str(random.uniform(0, 99999))])
    @pytest.mark.run(order=8)
    def test8_service_info_end_time_error_and_good_input(self, service_info_end_time):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
                "schedule_pickup_timeslot": {
                    "start_time": 11111111,
                    "end_time": service_info_end_time
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试start_time大于end_time")
    @pytest.mark.parametrize("start_time,end_time",
                             [(int(time.time()), int(time.time() - 300))])
    @pytest.mark.run(order=9)
    def test9_service_info_start_time_greater_end_time(self, start_time, end_time):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "21",
                "schedule_pickup_timeslot": {
                    "start_time": start_time,
                    "end_time": end_time
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    # 非必填字段测试
    @allure.feature("测试sender_info_name字段丢失")
    @pytest.mark.run(order=10)
    def test10_miss_sender_info_name(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_name字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_name", ["", None, random.randint(0, 9999999999999999), "   ", "\n\t", "a",
                                                  "sender name", "123456789", "@#$%^^&&*%##%%^", False, True,
                                                  "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64c",
                                                  "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64",
                                                  "Maxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64characterMaxlenthMaxlenth64characterMaxlenth64characterMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth64cMaxlenth6",
                                                  "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด&^",
                                                  "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดa",
                                                  "คอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโดซอยลาดพคอนโด"
                                                  ])
    @pytest.mark.run(order=11)
    def test11_sender_info_name_error_and_good_input(self, sender_info_name):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": sender_info_name,
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_email字段丢失")
    @pytest.mark.run(order=12)
    def test12_miss_sender_info_email(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
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
    @pytest.mark.run(order=13)
    def test13_sender_info_email_error_and_good_input(self, sender_info_email):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": sender_info_email,
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_phone字段丢失")
    @pytest.mark.run(order=14)
    def test14_miss_sender_info_phone(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_phone字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_phone",
                             ["", None, random.randint(0, 999999999999999999), "   ", "\n\t", "phone", "a",
                              "Maxlenth64characterMaxlen", "Maxlenth64characterMaxle", "Maxlenth64characterMaxl", True,
                              "คอนโดซอย?", "คอนโดซอย", "คอนโดซอ?", "012345678901234567890123", "1", "12", "013", False,
                              "01234567890123456789012", "0134665470", "0123456789012345678901234",
                              12345678901234567890123, 123456789012345678901234, 1234567890123456789012345])
    @pytest.mark.run(order=15)
    def test15_sender_info_phone_error_and_good_input(self, sender_info_phone):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": sender_info_phone,
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_country字段丢失")
    @pytest.mark.run(order=16)
    def test16_miss_sender_info_country(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
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
    @pytest.mark.run(order=17)
    def test17_sender_info_country_error_and_good_input(self, sender_info_country):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": sender_info_country,
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
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_state字段丢失")
    @pytest.mark.run(order=18)
    def test18_miss_sender_info_state(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
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
                              False, True, "real state"])
    @pytest.mark.run(order=19)
    def test19_sender_info_state_error_and_good_input(self, sender_info_state):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": sender_info_state,
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
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_city字段丢失")
    @pytest.mark.run(order=20)
    def test20_miss_sender_info_city(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
            },
            "service_info": {
                "service_types": "11",
                "cod_amount": "111",
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
                              False, True, "อำเภอไทยเจริญ"])
    @pytest.mark.run(order=21)
    def test21_sender_info_city_error_and_good_input(self, sender_info_city):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": sender_info_city,
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_district字段丢失")
    @pytest.mark.run(order=22)
    def test22_miss_sender_info_district(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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
    @pytest.mark.run(order=23)
    def test23_sender_info_district_error_and_good_input(self, sender_info_district):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": sender_info_district,
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_subdistrict字段丢失")
    @pytest.mark.run(order=24)
    def test24_miss_sender_info_subdistrict(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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
    @pytest.mark.run(order=25)
    def test25_sender_info_subdistrict_error_and_good_input(self, sender_info_subdistrict):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": sender_info_subdistrict,
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_street字段丢失")
    @pytest.mark.run(order=26)
    def test26_miss_sender_info_street(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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
    @pytest.mark.run(order=27)
    def test27_sender_info_street_error_and_good_input(self, sender_info_street):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": sender_info_street,
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_detail_address字段丢失")
    @pytest.mark.run(order=28)
    def test28_miss_sender_info_detail_address(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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
    @pytest.mark.run(order=29)
    def test29_sender_info_detail_address_error_and_good_input(self, sender_info_detail_address):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": sender_info_detail_address,
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_zip_code字段丢失")
    @pytest.mark.run(order=30)
    def test30_miss_sender_info_zip_code(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
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
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        self.send_assert_and_save(url=self.url, headers=self.header, data=params)

    @allure.feature("测试sender_info_zip_code字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_zip_code",
                             ["", None, random.randint(0, 99999), random.uniform(0, 99999), "  ", "\n\t", False,
                              True, "Maxlenth64charact", "Maxlenth64charac", "Maxlenth64chara", "คอนโด16", "คอนโด1",
                              "คอนโด", "888888", "zipcode", "35120", 35120])
    @pytest.mark.run(order=31)
    def test31_sender_info_zip_code_error_and_good_input(self, sender_info_zip_code):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": sender_info_zip_code,
                "longitude": "",
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_longitude字段丢失")
    @pytest.mark.run(order=32)
    def test32_miss_sender_info_longitude(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_longitude字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_longitude",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              False, True, "real state"])
    @pytest.mark.run(order=33)
    def test33_sender_info_longitude_error_and_good_input(self, sender_info_longitude):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": sender_info_longitude,
                "latitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_latitude字段丢失")
    @pytest.mark.run(order=34)
    def test34_miss_sender_info_latitude(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_latitude字段的异常和正常输入")
    @pytest.mark.parametrize("sender_info_latitude",
                             ["", None, random.randint(0, 999999), random.uniform(0, 999999), "  ", "\n\t", "a", "a23",
                              False, True, "real state"])
    @pytest.mark.run(order=35)
    def test35_sender_info_latitude_error_and_good_input(self, sender_info_latitude):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": sender_info_latitude,
                "remark": "sender remark"
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

    @allure.feature("测试sender_info_remark字段丢失")
    @pytest.mark.run(order=36)
    def test36_miss_sender_info_remark(self):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": ""
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
    @pytest.mark.run(order=37)
    def test37_sender_info_remark_error_and_good_input(self, sender_info_remark):
        params = {
            "carrier_tn": self.carrier_tn,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": sender_info_remark
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

    @allure.feature("修改已揽收的订单")
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
        pno = base.RedisBase().get("order_creation_api_0")
        order_id = self.get_staff_info_id(pno)[1]
        print("待揽收订单号：%s" % order_id)
        staff_info_id = self.get_staff_info_id(pno)[1]
        print("快递员工号：%s" % staff_info_id)
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

    @allure.feature("修改已取消的订单")
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
        url_cancel = "http://192.168.0.231:8080/callback/shopee/cancel"
        params_cancel = {"carrier_tn": order_id}
        self.send_assert_and_save(url=url_cancel, headers=self.header, data=params_cancel)
        params_modify = {
            "carrier_tn": order_id,
            "sender_info": {
                "name": "Mr O",
                "email": "",
                "phone": "+86 1234567",
                "country": "CN",
                "state": "จังหวัดยโสธร",
                "city": "อำเภอไทยเจริญ",
                "district": "nanshan",
                "subdistrict": "",
                "street": "",
                "detail_address": "abc xyz",
                "zip_code": "35120",
                "longitude": "",
                "latitude": "",
                "remark": "sender_info_remark"
            },
            "service_info": {
                "service_types": "11",
                "schedule_pickup_timeslot": {
                    "start_time": 1569310602,
                    "end_time": 1569328602
                }
            }
        }
        print("修改已取消订单的失败提示:%s" % self.send_assert_and_save(url=self.url, headers=self.header, data=params_modify))
