
import sys,os

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


@pytest.mark.run(order=72)
@allure.feature('车辆出港接口by')
class Test_vehicle_departure_by(object):
    def test_vehicle_departure_by(self):
        comm = Common_data()
        host = comm.each_parameter("host")
        conventional_circuit_id = comm.get_parameter_from_redis("vehicle_voucher_by_id")
        url = host + "api/courier/v1/fleet/proof/outbound/new/%s"%conventional_circuit_id
        session_id = comm.get_parameter_from_redis('backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]')
        header = {
            "X-FLE-SESSION-ID": session_id,
            "Accept-Language": "zh-CN",
            "By-Platform": "RB_KIT",
            "X-FLE-EQUIPMENT-TYPE": "kit"
        }
        Car_seal_code= comm.get_parameter_from_redis("car_seal_code")
        data={
            "fleet_bound_images": [
                {
                    "image_url": "fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg",
                    "img": "https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg",
                    "sealing_number": Car_seal_code
                    # "sealing_number": "p1000000012"
                }
            ],
            "outbound_image": {
                "image_key": "fleetOutbound/1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg",
                "image_name": "1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg"
            }
        }
        res = requests.post(url=url, headers=header, json=data, verify=False)
        logging.info("车辆出港接口返回:")
        logging.info(res.json())
        assert_that(res.json()["code"]).is_equal_to(1)
        assert_that(res.json()["message"]).is_equal_to("success")
        assert_that(res.json()["data"]).is_not_none()
        # logging.info("jsonschema文件path:../data/jsonschema/72vehicle_departure_by.json")
        # with open("../data/jsonschema/72vehicle_departure_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = res.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()


    '''

    @pytest.mark.parametrize("parameter",["{'fleet_bound_images': [{'image_url': 'fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg', 'img': 'https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg', 'sealing_number': '$car_seal_code$'}], 'outbound_image': {'image_key': 'fleetOutbound/1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg', 'image_name': '1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg'}}"])
    @pytest.mark.parametrize("headers",['{\'Accept-Language\': \'zh-CN\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\', \'X-FLE-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}'])
    @pytest.mark.parametrize("address",['api/courier/v1/fleet/proof/outbound/new/$vehicle_voucher_by_id$'])
    @pytest.mark.run(order=72)
    def test_test_vehicle_departure_by(self, parameter,headers,address):
        baseTest = BaseTestCase()
    
        _parameter = ["{'fleet_bound_images': [{'image_url': 'fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg', 'img': 'https://fle-staging-asset-internal.oss-ap-southeast-1.aliyuncs.com/fleetSealing/1586938648-4547be7a613443bfaa60df7f34c313e0.jpg', 'sealing_number': '$car_seal_code$'}], 'outbound_image': {'image_key': 'fleetOutbound/1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg', 'image_name': '1586938615-cf2b70bc28004f9ab4c37b24fb4745e5.jpg'}}"]
        
        _headers = ['{\'Accept-Language\': \'zh-CN\', \'By-Platform\': \'RB_KIT\', \'X-FLE-EQUIPMENT-TYPE\': \'kit\', \'X-FLE-SESSION-ID\': \'$backyard_overtime_car_auth_new_device_login_0_0_0_["data"]["sessionid"]$\'}']
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
                
        _address = ['api/courier/v1/fleet/proof/outbound/new/$vehicle_voucher_by_id$']
        
        host = 'host'
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
        
        if "zh" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "th" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        elif "en" in eval(headers)["Accept-Language"].lower():
            assert_that(resp.json()["message"]).is_equal_to("success")
        
        # logging.info("jsonschema文件path:../data/jsonschema/72vehicle_departure_by.json")
        # with open("../data/jsonschema/72vehicle_departure_by.json", "r", encoding = "utf-8") as f:
        #     shcema = json.load(f)
        #     res = validate(instance = resp.json(), schema = shcema)
        #     logging.info("jsonschema验证结果是： " + str(res))
        # assert_that(res).is_none()
    '''