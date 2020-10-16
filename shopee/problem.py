import random
import time

import requests

header = {
    "content-type": "application/json; charset=UTF-8",
    "Accept-Language": "zh-CN",
    "X-FLE-SESSION-ID": "1599473637_4b208a3dc70a384900c4c65802760be27973660e412f57a5e30f28ce029ab244_22479"
}
# TH20071RK71E TH20071RK70E
url1 = "http://192.168.0.228:8080/api/courier/v1/parcels/TH20111RKT0Z/problem_submission"
url2 = "http://192.168.0.228:8080/api/courier/v1/parcels/TH20111RKT0Z/detain_warehouse?isFromScanner=false"

# # 问题件：收件人电话号码是空号
# params1 = {
#     "difficulty_marker_category": 29,
#     "image_keys": ["difficulty/1598869570-b33860a2366d4b9da4af674049452927.jpg"],
#     "remark": "收件人电话号码是空号"
# }
# res1 = requests.post(url=url1, headers=header, json=params1)
# print(res1.json())
#
# # 问题件：货物破损
# params2 = {
#     "difficulty_marker_category": 20,
#     "image_keys": ["difficulty/1598869570-b33860a2366d4b9da4af674049452927.jpg"],
#     "remark": "货物破损"
# }
# res2 = requests.post(url=url1, headers=header, json=params2)
# print(res2.json())
#
# # 问题件：货物缺少
# params3 = {
#     "difficulty_marker_category": 21,
#     "image_keys": ["difficulty/1598869570-b33860a2366d4b9da4af674049452927.jpg"],
#     "remark": "货物缺少"
# }
# res3 = requests.post(url=url1, headers=header, json=params3)
# print(res3.json())
#
# # 问题件：COD金额不正确
# params4 = {
#     "difficulty_marker_category": 26,
#     "image_keys": ["difficulty/1598869570-b33860a2366d4b9da4af674049452927.jpg"],
#     "remark": "COD金额不正确"
# }
# res4 = requests.post(url=url1, headers=header, json=params4)
# print(res4.json())
#
# # 问题件：货物丢失
# params5 = {
#     "difficulty_marker_category": 22,
#     "remark": "货物丢失"
# }
# res5 = requests.post(url=url1, headers=header, json=params5)
# print(res5.json())
#
# # 问题件：收件人/地址不清晰或不正确
# params6 = {
#     "difficulty_marker_category": 23,
#     "image_keys": ["difficulty/1598869570-b33860a2366d4b9da4af674049452927.jpg"],
#     "remark": "收件人/地址不清晰或不正确"
# }
# res6 = requests.post(url=url1, headers=header, json=params6)
# print(res6.json())
#
# # 问题件：收件人电话号码错误
# params7 = {
#     "difficulty_marker_category": 25,
#     "image_keys": ["difficulty/1598869570-b33860a2366d4b9da4af674049452927.jpg"],
#     "remark": "收件人电话号码错误"
# }
# res7 = requests.post(url=url1, headers=header, json=params7)
# print(res7.json())
#
# # 问题件：收件人拒收
# params8 = {
#     "difficulty_marker_category": 17,
#     "image_keys": ["difficulty/1598869570-b33860a2366d4b9da4af674049452927.jpg"],
#     "remark": "收件人拒收",
#     "rejection_category": 2  # 1.未购买商品,2.商品不满意
# }
# res8 = requests.post(url=url1, headers=header, json=params8)
# print(res8.json())
#
# # 问题件：分错网点-运输错误
# params9 = {
#     "difficulty_marker_category": 30
# }
# res9 = requests.post(url=url1, headers=header, json=params9)
# print(res9.json())
#
# # 问题件：分错网点-地址错误(接口参数不全)
# params9 = {
#     "difficulty_marker_category": 31
# }
# res9 = requests.post(url=url1, headers=header, json=params9)
# print(res9.json())
#
# # 问题件：仅外包装破损
# params10 = {
#     "difficulty_marker_category": 19,
#     "image_keys": ["difficulty/PRE-1598935413-0e12f3f137224a1a976793b7258e8c09.jpg",
#                    "difficulty/AFT-1598935416-8bb58b7f4f5f442c8f669a7ecd3ad17c.jpg"],
#     "remark": "仅外包装破损"
# }
# res10 = requests.post(url=url1, headers=header, json=params10)
# print(res10.json())
#
# # 货件留仓：当日运力不足，无法配送
# params11 = {
#     "detained_marker_category": 15,
#     "from_scanner": "false",
#     "image_keys": ["parcelManualImport/1598876104-f16cf4a1116343a2ab0a75a1b22da8ff.jpg"],
#     "parcel_scan_manual_import_category": 0,
#     "skipped_enabled": False
# }
# res11 = requests.post(url=url2, headers=header, json=params11)
# print(res11.json())
#
# # 货件留仓：错过班车时间
# params12 = {
#     "detained_marker_category": 41,
#     "from_scanner": "false",
#     "image_keys": ["parcelManualImport/1598876104-f16cf4a1116343a2ab0a75a1b20da7ff.jpg"],
#     "parcel_scan_manual_import_category": 99,
#     "skipped_enabled": False
# }
# res12 = requests.post(url=url2, headers=header, json=params12)
# print(res12.json())
#
# # 货件留仓：偏远地区
# params13 = {
#     "detained_marker_category": 42,
#     "from_scanner": "false",
#     "image_keys": ["parcelManualImport/1598876104-f16cf4a1116343a2ab0a75a1b20da9ff.jpg"],
#     "parcel_scan_manual_import_category": 0,
#     "skipped_enabled": False
# }
# res13 = requests.post(url=url2, headers=header, json=params13)
# print(res13.json())
#
# # 货件留仓：目的地是岛屿
# params14 = {
#     "detained_marker_category": 43,
#     "from_scanner": "false",
#     "image_keys": ["parcelManualImport/1598876104-f16cf4a1116343a2ab0a75a1b20da6ff.jpg"],
#     "parcel_scan_manual_import_category": 99,
#     "skipped_enabled": False
# }
# res14 = requests.post(url=url2, headers=header, json=params14)
# print(res14.json())
#
# # 货件留仓：客户改约时间
# params15 = {
#     "detained_marker_category": 14,
#     "from_scanner": "false",
#     "image_keys": ["parcelManualImport/1598876104-f16cf4a1116363a2ab0a75a1b20da6ff.jpg"],
#     "parcel_scan_manual_import_category": 99,
#     "skipped_enabled": False,
#     "desired_at": int(time.time())+86400
# }
# res15 = requests.post(url=url2, headers=header, json=params15)
# print(res15.json())
#
# # 货件留仓：客户不在家/电话无人接听
# params16 = {
#     "detained_marker_category": 40,
#     "from_scanner": "false",
#     "image_keys": ["parcelManualImport/1598876104-f16cf4a1116353a2ab0a75a1b21da7ff.jpg"],
#     "parcel_scan_manual_import_category": 99,
#     "skipped_enabled": False
# }
# res16 = requests.post(url=url2, headers=header, json=params16)
# print(res16.json())
