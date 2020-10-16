
import sys,os

from app.Kit.Courier.Utils.read_session_courier import read_courier_session_id
from app.Kit.Util.common_data import Common_data

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


@allure.feature('揽收完成')
class Test_collect_complete(object):

    list_i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
              30, 31, 32, 33, 34]

    @pytest.mark.parametrize("i", list_i)
    @allure.story("揽收完成")
    @pytest.mark.run(order=3)
    def test_test_collect_complete(self, i):

        comm = Common_data()
        # session_id = read_courier_session_id()
        session_id = read_courier_session_id('courier_login_0_0_0_["data"]["sessionid"]')
        # ticket_pickup_id = read_request_data("ticket_pickup" + str(i), "ticket_pickup_id" + str(i))
        ticket_pickup_id = read_courier_session_id("ticket_pickup_id" + str(i))
        url = "api/courier/v1/ticket/%s" % ticket_pickup_id
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        # host = read_common("host")
        host = comm.each_parameter("host")
        resp = requests.post(url=host + url, headers=header, verify=False)
        logging.info("揽收完成接口运行完毕")
        logging.info("请求头是：")
        logging.info(header)
        logging.info("请求url日志信息：")
        logging.info(host + url)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())
        assert_that(resp.json()["message"]).is_equal_to("success")
        assert_that(resp.status_code).is_equal_to(200)
        assert_that(resp.json()["code"]).is_equal_to(1)
        logging.info("jsonschema文件path:../data/jsonschema/2courier_write_order.json")
        # with open("../data/jsonschema/3collect_complete.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()







        # baseTest = BaseTestCase()
        #
        # _parameter = ["{'article_category': 99, 'call_duration': 0, 'client_id': '$[config]client_id$', 'cod_amount': 0, 'cod_enabled': False, 'customer_type_category': 2, 'dst_city_code': 'TH0502', 'dst_country_code': 'TH', 'dst_detail_address': '2', 'dst_district_code': 'TH050201', 'dst_name': '2', 'dst_phone': '1346999281', 'dst_postal_code': '13130', 'dst_province_code': 'TH05', 'express_category': 1, 'freight_insure_enabled': False, 'height': 1, 'insure_declare_value': 0, 'insured': False, 'length': 1, 'settlement_category': 1, 'skipping_tips': [], 'src_city_code': 'TH1101', 'src_country_code': 'TH', 'src_detail_address': '1', 'src_district_code': 'TH110101', 'src_name': '1', 'src_phone': '1232311232', 'src_postal_code': '26000', 'src_province_code': 'TH11', 'total_amount': 4000, 'weight': 2000, 'width': 1}"]
        #
        # _headers = ['{\'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$courier_login_0_0_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-DEVICE-ID\': \'8673510346528821571665712622\', \'Content-Type\': \'application/json\'}', '{\'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$courier_login_0_0_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-DEVICE-ID\': \'8673510346528821571665712622\', \'Content-Type\': \'application/json\'}', '{\'Accept-Language\': \'th-CN\', \'X-FLE-SESSION-ID\': \'$courier_login_0_0_0_["data"]["sessionid"]$\', \'By-Platform\': \'RB_KIT\', \'X-DEVICE-ID\': \'8673510346528821571665712622\', \'Content-Type\': \'application/json\'}']
        # headers_new = baseTest.parameter_parser(headers)
        # headers_new = ast.literal_eval(headers_new)
        #
        # parameter_new = baseTest.parameter_parser(parameter, _headers, headers)
        # address_new = baseTest.parameter_parser(address)
        # if '[int]' in parameter_new:
        #     parameter_new = ast.literal_eval(parameter_new)
        #     for key in parameter_new:
        #         if '[int]' in str(parameter_new[key]):
        #             parameter_new[key] = int(parameter_new[key][5:])
        # else:
        #     parameter_new = ast.literal_eval(parameter_new)
        #
        # _address = ['api/courier/v1/ticket/']
        #
        # host = 'host'
        # host = baseTest.get_host(host)
        # url_data = host + address_new
        # url = baseTest.parameter_parser(url_data)
        # logging.info("url日志信息:")
        # logging.info(url)
        # if "application/json" in str(headers).lower():
        #     resp = requests.post(url = url, json = parameter_new, headers = headers_new, timeout = 120, verify = False)
        # else:
        #     resp = requests.post(url = url, data = parameter_new, headers = headers_new, timeout = 120, verify = False)
        # logging.info("请求头是：")
        # logging.info(headers_new)
        # logging.info("请求参数日志信息：")
        # logging.info(parameter_new)
        # logging.info("响应结果日志信息：")
        # logging.info(resp.json())
        #
        # RedisBase().set('collect_complete_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["ticket_pickup_id"]', resp.json()["data"]["ticket_pickup_id"], ex=6000)
        #
        # RedisBase().set('collect_complete_' + str(_parameter.index(parameter)) + '_' + str(_headers.index(headers)) + '_' + str(_address.index(address)) + '_["data"]["parcel_info"]["pno"]', resp.json()["data"]["parcel_info"]["pno"], ex=6000)
        #
        # assert_that(baseTest.is_json(resp.text)).is_equal_to(True)
        #
        # assert_that(resp.status_code).is_equal_to(200)
        #
        # assert_that(resp.json()["code"]).is_equal_to(1)
        #
        # if "zh" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        # elif "th" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        # elif "en" in eval(headers)["Accept-Language"].lower():
        #     assert_that(resp.json()["message"]).is_equal_to("success")
        #
        # logging.info("jsonschema文件path:../data/jsonschema/2courier_write_order.json")
        # with open("../data/jsonschema/2courier_write_order.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
        