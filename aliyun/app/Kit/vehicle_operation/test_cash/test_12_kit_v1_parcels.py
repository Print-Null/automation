import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__)).split("/flash/")[0] + "/flash")
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


@allure.feature('复称-手动输入单号')
class Test_kit_v1_parcels(object):

    @pytest.mark.parametrize("headers", [
        '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}',
        '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}',
        '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address", [
        'api/courier/v1/parcels_v0/$kit_pickups_parcel_0_#headers#_0_["data"]["parcel_info"]["pno"]$'])
    @pytest.mark.run(order=12)
    def test_test_kit_v1_parcels(self, headers, address):
        baseTest = BaseTestCase()

        _parameter = []

        _headers = [
            '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'zh-CN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_0_0_["data"]["sessionid"]$\'}',
            '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'en-US\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_1_0_["data"]["sessionid"]$\'}',
            '{\'content-type\': \'application/json; charset=UTF-8\', \'Accept-Language\': \'th-TN\', \'X-FLE-SESSION-ID\': \'$kit_auth_new_device_login_1_2_0_["data"]["sessionid"]$\'}']
        headers_new = baseTest.parameter_parser(headers)
        headers_new = ast.literal_eval(headers_new)

        _address = ['api/courier/v1/parcels_v0/$kit_pickups_parcel_0_#headers#_0_["data"]["parcel_info"]["pno"]$']
        address_new = baseTest.parameter_parser(address, _headers, headers)

        host = 'kit_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        resp = requests.get(url=url, headers=headers_new, verify=False, timeout=120)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())

        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)

        assert_that(resp.status_code).is_equal_to(200)

        assert_that(resp.json()["code"]).is_equal_to(1)

        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")

        # logging.info("jsonschema文件path:../data/jsonschema/12_polysemy.json")
        # with open("../data/jsonschema/12_polysemy.json", "r", encoding="utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance=resp.json(), schema=shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
