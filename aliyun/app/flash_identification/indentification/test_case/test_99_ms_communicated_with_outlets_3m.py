
import sys,os
sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0]+"/flash")
import allure
from assertpy import assert_that
import requests
import logging
import ast
import json
import time
import pytest
from common.base import BaseTestCase
from utils.redisbase import RedisBase
from jsonschema import validate
                
logging.basicConfig(level=logging.INFO)


@allure.feature('待网点沟通，等待3分钟定时任务后，状态改变')
class Test_ms_communicated_with_outlets_3m(object):
    def setup_class(cls):
        time.sleep(200)
        logging.info("三分钟等待完成")

    @pytest.mark.parametrize("parameter",['{\'states\': [], \'pno\': \'$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          '{\'states\': [], \'pno\': \'$courier_write_order_1_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_2_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_3_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_4_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_5_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_6_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_7_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_8_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_9_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_10_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_11_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_12_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # ？'{\'states\': [], \'pno\': \'$courier_write_order_13_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          #？ '{\'states\': [], \'pno\': \'$courier_write_order_14_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_15_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_16_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_17_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_18_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                                          # '{\'states\': [], \'pno\': \'$courier_write_order_19_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}'
                                          ])
    @pytest.mark.parametrize("headers",['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_collection_outlets_login_0_0_0_["data"]["session_id"]$\'}'])
    @pytest.mark.parametrize("address",['ms/api/store/pickup_diff_tickets'])
    @pytest.mark.run(order=99)
    def test_test_ms_communicated_with_outlets_3m(self, parameter,headers,address):
        baseTest = BaseTestCase()
        # time.sleep(200)
        _parameter = ['{\'states\': [], \'pno\': \'$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      '{\'states\': [], \'pno\': \'$courier_write_order_1_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_2_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_3_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_4_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_5_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_6_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_7_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_8_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_9_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_10_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_11_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_12_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # ?'{\'states\': [], \'pno\': \'$courier_write_order_13_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # ?'{\'states\': [], \'pno\': \'$courier_write_order_14_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_15_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_16_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_17_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_18_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}',
                      # '{\'states\': [], \'pno\': \'$courier_write_order_19_0_0_["data"]["parcel_info"]["pno"]$\', \'page_size\': 100, \'page_num\': 1, \'start_time\': \'$[python]datetime.date.today()$\', \'end_time\': \'$[python]datetime.date.today()$\'}'
                      ]
        parameter_new = baseTest.parameter_parser(parameter)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
        
        _headers = ['{\'Accept\': \'application/json, text/plain, */*\', \'Accept-Language\': \'zh-CN\', \'Content-Type\': \'application/json;charset=UTF-8\', \'X-MS-SESSION-ID\': \'$ms_collection_outlets_login_0_0_0_["data"]["session_id"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        _address = ['ms/api/store/pickup_diff_tickets']
            
        host = 'ms_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        if "application/json" in str(headers).lower():
            resp = requests.post(url = url, json = parameter_new, headers = headers_new, timeout = 120, verify = False)
        else:
            resp = requests.post(url = url, data = parameter_new, headers = headers_new, timeout = 120, verify = False)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("请求参数日志信息：")
        logging.info(parameter_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        if resp.json()["data"]["items"][-1]["state_text"]:
            if resp.json()["data"]["items"][-1]["state_text"] == "转交闪速系统(丢失类)":
                assert_that(resp.json()["data"]["items"][-1]["state_text"] == "转交闪速系统(丢失类)").is_true()
            elif resp.json()["data"]["items"][-1]["state_text"] == "已处理":
                assert_that(resp.json()["data"]["items"][-1]["state_text"] == "已处理").is_true()
            else:
                assert_that(resp.json()["data"]["items"][-1]["state_text"]).is_equal_to(1)
                logging.info("没有查询到此订单")
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        