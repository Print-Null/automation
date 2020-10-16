
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


@allure.feature('bi网点经理工单列表页面')
class Test_ms_work_order_list_page(object):

    @pytest.mark.parametrize("parameter",["{}"])
    @pytest.mark.parametrize("headers",["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_manager_PHPSESSID$'}"])
    @pytest.mark.parametrize("address",['workorder/mydealing_ajax?draw=1&columns[0][data]=speed_level&columns[0][name]=&columns[0][searchable]=false&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=status&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=title&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=order_type&columns[3][name]=&columns[3][searchable]=false&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=reply_time&columns[4][name]=&columns[4][searchable]=false&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=created_at&columns[5][name]=&columns[5][searchable]=false&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=reminder_pno_created_at&columns[6][name]=&columns[6][searchable]=false&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=reply_staff_info_name&columns[7][name]=&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=latest_deal_at&columns[8][name]=&columns[8][searchable]=false&columns[8][orderable]=false&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=staff_info_id&columns[9][name]=&columns[9][searchable]=false&columns[9][orderable]=false&columns[9][search][value]=&columns[9][search][regex]=false&columns[10][data]=worder_staff_store_name&columns[10][name]=&columns[10][searchable]=false&columns[10][orderable]=false&columns[10][search][value]=&columns[10][search][regex]=false&start=0&length=100&search[value]=$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$&search[regex]=false&f=my_dealing&date=$[python]str(datetime.date.today()) + " 00:00:00" +" - " + str(datetime.date.today()) + " 23:59:59"$&staff_id=&status=0'])
    @pytest.mark.run(order=178)
    def test_test_ms_work_order_list_page(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{}"]
        
        _headers = ["{'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN', 'BI-PLATFORM': None, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Cookie': '$indentifi_manager_PHPSESSID$'}"]
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)
        
        parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        address_new = baseTest.parameter_parser(address)
        if '[int]' in parameter_new:
            parameter_new = ast.literal_eval(parameter_new)
            for key in parameter_new:
                if '[int]' in str(parameter_new[key]):
                    parameter_new[key] = int(parameter_new[key][5:])
        else:
            parameter_new = ast.literal_eval(parameter_new)
                
        _address = ['workorder/mydealing_ajax?draw=1&columns[0][data]=speed_level&columns[0][name]=&columns[0][searchable]=false&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=status&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=title&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=order_type&columns[3][name]=&columns[3][searchable]=false&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=reply_time&columns[4][name]=&columns[4][searchable]=false&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=created_at&columns[5][name]=&columns[5][searchable]=false&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=reminder_pno_created_at&columns[6][name]=&columns[6][searchable]=false&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=reply_staff_info_name&columns[7][name]=&columns[7][searchable]=false&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=latest_deal_at&columns[8][name]=&columns[8][searchable]=false&columns[8][orderable]=false&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=staff_info_id&columns[9][name]=&columns[9][searchable]=false&columns[9][orderable]=false&columns[9][search][value]=&columns[9][search][regex]=false&columns[10][data]=worder_staff_store_name&columns[10][name]=&columns[10][searchable]=false&columns[10][orderable]=false&columns[10][search][value]=&columns[10][search][regex]=false&start=0&length=100&search[value]=$courier_write_order_0_0_0_["data"]["parcel_info"]["pno"]$&search[regex]=false&f=my_dealing&date=$[python]str(datetime.date.today()) + " 00:00:00" +" - " + str(datetime.date.today()) + " 23:59:59"$&staff_id=&status=0']
            
        host = 'fbi_host_domain'
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
        
        RedisBase().set('ms_work_order_list_page_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["DataList"][0]["pnos"]', resp.json()["data"]["DataList"][0]["pnos"], ex=6000)
        
        RedisBase().set('ms_work_order_list_page_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["DataList"][0]["order_id"]', resp.json()["data"]["DataList"][0]["order_id"], ex=6000)
        
        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        
        assert_that(resp.status_code).is_equal_to(200)
        
        assert_that(resp.json()["code"]).is_equal_to(1)
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["msg"]).is_equal_to("ok")
        