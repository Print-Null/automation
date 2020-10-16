import ast
import base64
import datetime
import hashlib
import urllib.parse
import random
import time
import requests
import json

import yaml

url = "http://192.168.0.228:8181/ka/api/orders/exportIds"
header = {'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'zh-CN',
          "Content-Type": "application/json;charset=UTF-8",
          'X-KA-SESSION-ID': '1597837646_66f9300c13ebbe9a6ebead1bfcaf3049b35bd4fdd0c005ee453a07f366d9dfbb_AA0586'}
params = ["5f377c0f2d738a0f836871fe", "5f377c0f2d738a0f836871ff", "5f377c0f2d738a0f83687200",
          "5f377c0f2d738a0f83687201", "5f377c0f2d738a0f83687202", "5f377c0f2d738a0f83687203",
          "5f377c0f2d738a0f83687204", "5f377c0f2d738a0f83687205", "5f377c0f2d738a0f83687206",
          "5f377c0f2d738a0f83687207", "5f377c0f2d738a0f83687208", "5f377c0f2d738a0f83687209", "5f377c0a2d738a0f8368"]
print(params)
req = requests.post(url=url, headers=header, json=params)
print(req.ok,req.raise_for_status(),req.status_code,req.raw)
# print(req.json())
# print(json.dumps(req.json(), indent=2, ensure_ascii=False))
# package_infos = [
#     {"packageId": str(random.randint(100000000, 999999999)),
#      "weight": 5,
#      "volume": "",git
#      "lenght": "",
#      "width": "",
#      "height": ""}]
# sender = {
#     "name": "Bangkok Sorting",
#     "mobile": "0135" + str(random.randint(100000, 999999)),
#     "province": "Samut Prakan",
#     "city": "Bang Phli",
#     "county": "Bang Pla",
#     "town": "",
#     "address": "333/9-12 Moo.3Bang Sao Thong， Samut Prakan 10540",
#     "zipCode": "10540"
# }
# receiver = {
#     "name": "อรจิรา",
#     "mobile": "0134" + str(random.randint(100000, 999999)),
#     "province": "Bangkok",
#     "city": "Pom Prap Sattru Phai",
#     "county": "Khlong Maha Nak",
#     "town": "",
#     "address": "3333 Bang Khae Nuea ",
#     "zipCode": "10110",
#     "email": ""
# }
# order_datail = {
#     "orderCreateTime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
#     "orderType": 1,
#     "gotStartTime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
#     "gotEndTime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
#     "goodsValue": 200,
#     "totalFee": "",
#     "insuranceValue": "",
#     "totalServiceFee": "",
#     "codSplitFee": "",
#     "sch eduleType": ""
# }
# logistics_info = {
#     "logisticsProviderCode": "Flash",
#     "country": "th",
#     "createSiteName": "BBK",
#     "waybillCode": "",
#     "orderId": str(random.randint(100000000, 999999999)),
#     "packageInfos": package_infos,
#     "sender": sender,
#     "receiver": receiver,
#     "orderDetail": order_datail,
#     "extendFields": [
#         {
#             "key": "vendorId",
#             "value": "106"
#         },
#         {
#             "key": " serviceLevel",
#             "value": "JDExpress"
#         }
#     ],
#     "remark": ""
# }
# url = "http://192.168.0.228:8080/callback/jd/order"
# times_tamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# print(times_tamp)
# jd_key = "123456"
# logistics_info_str = json.dumps(logistics_info)
# print(logistics_info_str, end="\n")
# logisticsInfo = urllib.parse.quote(logistics_info_str, encoding="utf-8")
# print("URL encode后的logisticsInfo：\n%s" % logisticsInfo)
#
# # 生成encrypt_data
# signature_content = logistics_info_str + times_tamp + jd_key
# md5_str = hashlib.md5()
# md5_str.update(signature_content.encode("utf-8"))
# sign_str = md5_str.hexdigest()
# print("MD5加密字符串：\n%s" % sign_str)
#
# base64_str = str(base64.b64encode(sign_str.encode("utf-8")), "utf-8")
# print("转化成base64字符串：\n%s" % base64_str)
#
# encrypt_data = urllib.parse.quote(base64_str, encoding="utf-8")
# print("URL encode后的encrypt_data：\n%s" % encrypt_data)
#
# parameter = {
#     "logistics_info": "{}".format(logisticsInfo),
#     "timestamp": "{}".format(times_tamp),
#     "encrypt_data": "{}".format(encrypt_data)
# }
# print("请求参数为：\n%s" % parameter)
# header = {"Content-Type": "application/x-www-form-urlencoded"}
# req = requests.post(url=url, headers=header, data=parameter)
# print("响应结果日志：\n%s" % req.json())
# class TestNotification(object):
#     def test_notification(self):
#         url = "http://192.168.0.228:8080/open/v1/notifications"
#         header = {
#             'content-type': 'application/x-www-form-urlencoded', 'Charset': 'UTF-8', 'Accept-Language': 'ZH-CN'
#         }
#         date = str(datetime.date.today())
#         parameter = str({
#             'nonceStr': '1596699444',
#             'sign': 'sha256',
#             'mchId': 'BA0260',
#             'date': '{}'.format(date)
#         })
#         parameter_new = ast.literal_eval(self.create_sign(parameter))
#         req = requests.post(url=url, headers=header, json=parameter_new)
#         print(req.json())
#
#     def create_sign(self, parameter_new: str):
#         key = "a8f67ded589b84993ab2d14caf808b93d6769a2c70512f9ad98054b7f1cd7143"
#         parameter_dict = ast.literal_eval(parameter_new)
#         argument_list = []
#         for k, v in parameter_dict.items():
#             if v != "" and k != "sign":
#                 argument_list.append(k)
#         argument_list.sort()
#         sha_string_list = []
#         for i in argument_list:
#             sha_string_list.append(i)
#             sha_string_list.append("=")
#             sha_string_list.append(str(parameter_dict[i]))
#             sha_string_list.append("&")
#         sha_string = "".join(sha_string_list)
#         string_sign_temp = sha_string + "key=" + key
#         sha256 = hashlib.sha256()
#         sha256.update(string_sign_temp.encode("utf-8"))
#         sign = sha256.hexdigest().upper()
#         parameter_new = parameter_new.replace("sha256", sign)
#         return parameter_new
