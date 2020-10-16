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


@allure.feature('B客户对运送中的运单催单')
class Test_app_ka_sender_parcels_reminder_cn(object):

    @pytest.mark.parametrize("parameter", ["{'hurry_parcel_type': 1}"])
    @pytest.mark.parametrize("headers", [
        '{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_sender_login_cn_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address", [
        '/api/ka/v1/parcels/reminder/$kit_ka_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][2]["pno"]$'])
    @pytest.mark.run(order=331)
    def test_test_app_ka_sender_parcels_reminder_cn(self, parameter, headers, address):
        baseTest = BaseTestCase()

        _parameter = ["{'hurry_parcel_type': 1}"]

        _headers = [
            '{\'content-type\': \'application/json\', \'Accept-Language\': \'en-CN\', \'X-KA-SESSION-ID\': \'$app_ka_sender_login_cn_0_0_0_["data"]["sessionid"]$\'}']
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

        _address = [
            '/api/ka/v1/parcels/reminder/$kit_ka_sender_courier_ticket_pickups_cn_0_0_["data"]["collected_parcels"][2]["pno"]$']

        host = 'app_host'
        host = baseTest.get_host(host)
        url_data = host + address_new
        url = baseTest.parameter_parser(url_data)
        logging.info("url日志信息:")
        logging.info(url)
        if "application/json" in str(headers).lower():
            resp = requests.post(url=url, json=parameter_new, headers=headers_new, timeout=120, verify=False)
        else:
            resp = requests.post(url=url, data=parameter_new, headers=headers_new, timeout=120, verify=False)
        logging.info("请求头是：")
        logging.info(headers_new)
        logging.info("请求参数日志信息：")
        logging.info(parameter_new)
        logging.info("响应结果日志信息：")
        logging.info(resp.json())

        assert_that(baseTest.is_json(resp.text)).is_equal_to(True)

        assert_that(resp.status_code).is_equal_to(422)

        assert_that(resp.json()["code"]).is_equal_to(101870)

        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to(
                "Your parcel has been collected today and its on the way to the next station. Please check again the status tomorrow. ")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to(
                "Your parcel has been collected today and its on the way to the next station. Please check again the status tomorrow. ")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert "Your parcel has been collected today and its on the way to the next station" in resp.json()[
                "message"]

        logging.info("jsonschema文件path:../data/jsonschema/21_app_ka_sender_parcels_reminder_cn.json")
        with open("../data/jsonschema/21_app_ka_sender_parcels_reminder_cn.json", "r", encoding="utf-8") as f:
            shcema = json.load(f)
            res = validate(instance=resp.json(), schema=shcema)
            logging.info("jsonschema验证结果是： " + str(res))
        assert_that(res).is_none()
