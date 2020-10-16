import base64
import hashlib
import hmac

import jwt
import json
import time

# data1 = {
#     "sender_info": {
#         "sender_id": "5555111",
#         "phone": "6622820618",
#         "city": "อำเภอบางพลี",
#         "remark": "test1",
#         "name": "aCommerce, Inc. - Johnson & Johnson",
#         "latitude": "",
#         "country": "TH",
#         "longitude": "",
#         "state": "จังหวัดสมุทรปราการ",
#         "company_name": "sss",
#         "detail_address": "10 P. Antonio St. , Pasig City, Metro Manila",
#         "email": "handsome.xu@shopee.com",
#         "zip_code": "1604"
#     },
#     "receiver_info": {
#         "phone": "66662313434",
#         "city": "เขตทุ่งครุ",
#         "remark": "test2",
#         "name": "Super Xu",
#         "latitude": "13.222",
#         "country": "TH",
#         "longitude": "13.222",
#         "state": "จังหวัดกรุงเทพมหานคร",
#         "detail_address": "Lot 4850-A Molino Blvd., Niog 3, Bacoor, Cavite (along molino blvd. road, white gate with green bottles on top near NOMO)",
#         "email": "xu.handsome@shopee.com",
#         "zip_code": "8647"
#     },
#     "service_info": {
#         "service_types": "11,22",
#         "cod_amount": "121",
#         "schedule_pickup_timeslot": {
#             "start_time": 1598949820,
#             "end_time": 1599036220
#         }
#     },
#     "order": {
#         "business_type": 1,
#         "estimate_chargeable_weight": 12120,
#         "reference_no": "20200831164340TEST",
#         "carrier_tn": "",
#         "total_weight": 48480,
#         "goods_value": "10"
#     },
#     "item_info": [
#         {
#             "category": "aaa",
#             "item_price": 144,
#             "item_name": "Lamborghini",
#             "sub_sub_category": "ccc",
#             "height": 10,
#             "width": 15,
#             "length": 20,
#             "item_quantity": 2,
#             "sub_category": "bbb"
#         },
#         {
#             "category": "yyy",
#             "item_price": 114,
#             "item_name": "Lamborghini",
#             "sub_sub_category": "qqq",
#             "height": 10,
#             "width": 15,
#             "length": 20,
#             "item_quantity": 2,
#             "sub_category": "rrr"
#         }
#     ]
# }
#
#
# def gen_jwt_data(data, secret, timestamp):
#     jwt_header = {"alg": "HS256",
#                   "account": "AA0425",
#                   "typ": "JWT"
#                   }
#     jwt_payload = {
#         "data": data,
#         "timestamp": timestamp
#     }
#     return {"jwt": jwt.encode(jwt_payload, secret, headers=jwt_header, algorithm="HS256").decode("utf-8")}


#
#
# def get_data(jwt_token):
#     data = None
#     try:
#         data = jwt.decode(jwt_token, "123456789", algorithms=["HS256"])
#     except Exception as e:
#         print(e)
#     return data
#
#
# jwt_token = "eyJhbGciOiJIUzI1NiIsImFjY291bnQiOiJBQTA0MjUiLCJ0eXAiOiJKV1QifQ.eyJ0aW1lc3RhbXAiOjE1OTg4NjM0MjQsImRhdGEiOnsic2VuZGVyX2luZm8iOnsic2VuZGVyX2lkIjoiNTU1NTExMSIsInBob25lIjoiNjYyMjgyMDYxOCIsImNpdHkiOiJcdTBlMmRcdTBlMzNcdTBlNDBcdTBlMjBcdTBlMmRcdTBlMWFcdTBlMzJcdTBlMDdcdTBlMWVcdTBlMjVcdTBlMzUiLCJyZW1hcmsiOiJ0ZXN0MSIsIm5hbWUiOiJhQ29tbWVyY2UsIEluYy4gLSBKb2huc29uICYgSm9obnNvbiIsImxhdGl0dWRlIjoiIiwiY291bnRyeSI6IlRIIiwibG9uZ2l0dWRlIjoiIiwic3RhdGUiOiJcdTBlMDhcdTBlMzFcdTBlMDdcdTBlMmJcdTBlMjdcdTBlMzFcdTBlMTRcdTBlMmFcdTBlMjFcdTBlMzhcdTBlMTdcdTBlMjNcdTBlMWJcdTBlMjNcdTBlMzJcdTBlMDFcdTBlMzJcdTBlMjMiLCJjb21wYW55X25hbWUiOiJzc3MiLCJkZXRhaWxfYWRkcmVzcyI6IjEwIFAuIEFudG9uaW8gU3QuICwgUGFzaWcgQ2l0eSwgTWV0cm8gTWFuaWxhIiwiZW1haWwiOiJoYW5kc29tZS54dUBzaG9wZWUuY29tIiwiemlwX2NvZGUiOiIxNjA0In0sInJlY2VpdmVyX2luZm8iOnsicGhvbmUiOiI2NjY2MjMxMzQzNCIsImNpdHkiOiJcdTBlNDBcdTBlMDJcdTBlMTVcdTBlMTdcdTBlMzhcdTBlNDhcdTBlMDdcdTBlMDRcdTBlMjNcdTBlMzgiLCJyZW1hcmsiOiJ0ZXN0MiIsIm5hbWUiOiJTdXBlciBYdSIsImxhdGl0dWRlIjoiMTMuMjIyIiwiY291bnRyeSI6IlRIIiwibG9uZ2l0dWRlIjoiMTMuMjIyIiwic3RhdGUiOiJcdTBlMDhcdTBlMzFcdTBlMDdcdTBlMmJcdTBlMjdcdTBlMzFcdTBlMTRcdTBlMDFcdTBlMjNcdTBlMzhcdTBlMDdcdTBlNDBcdTBlMTdcdTBlMWVcdTBlMjFcdTBlMmJcdTBlMzJcdTBlMTlcdTBlMDRcdTBlMjMiLCJkZXRhaWxfYWRkcmVzcyI6IkxvdCA0ODUwLUEgTW9saW5vIEJsdmQuLCBOaW9nIDMsIEJhY29vciwgQ2F2aXRlIChhbG9uZyBtb2xpbm8gYmx2ZC4gcm9hZCwgd2hpdGUgZ2F0ZSB3aXRoIGdyZWVuIGJvdHRsZXMgb24gdG9wIG5lYXIgTk9NTykiLCJlbWFpbCI6Inh1LmhhbmRzb21lQHNob3BlZS5jb20iLCJ6aXBfY29kZSI6Ijg2NDcifSwic2VydmljZV9pbmZvIjp7InNlcnZpY2VfdHlwZXMiOiIxMSwyMiIsImNvZF9hbW91bnQiOiIxMjEiLCJzY2hlZHVsZV9waWNrdXBfdGltZXNsb3QiOnsic3RhcnRfdGltZSI6MTU5ODk0OTgyMCwiZW5kX3RpbWUiOjE1OTkwMzYyMjB9fSwib3JkZXIiOnsiYnVzaW5lc3NfdHlwZSI6MSwiZXN0aW1hdGVfY2hhcmdlYWJsZV93ZWlnaHQiOjEyMTIwLCJyZWZlcmVuY2Vfbm8iOiIyMDIwMDgzMTE2NDM0MFRFU1QiLCJjYXJyaWVyX3RuIjoiIiwidG90YWxfd2VpZ2h0Ijo0ODQ4MCwiZ29vZHNfdmFsdWUiOiIxMCJ9LCJpdGVtX2luZm8iOlt7ImNhdGVnb3J5IjoiYWFhIiwiaXRlbV9wcmljZSI6MTQ0LCJpdGVtX25hbWUiOiJMYW1ib3JnaGluaSIsInN1Yl9zdWJfY2F0ZWdvcnkiOiJjY2MiLCJoZWlnaHQiOjEwLCJ3aWR0aCI6MTUsImxlbmd0aCI6MjAsIml0ZW1fcXVhbnRpdHkiOjIsInN1Yl9jYXRlZ29yeSI6ImJiYiJ9LHsiY2F0ZWdvcnkiOiJ5eXkiLCJpdGVtX3ByaWNlIjoxMTQsIml0ZW1fbmFtZSI6IkxhbWJvcmdoaW5pIiwic3ViX3N1Yl9jYXRlZ29yeSI6InFxcSIsImhlaWdodCI6MTAsIndpZHRoIjoxNSwibGVuZ3RoIjoyMCwiaXRlbV9xdWFudGl0eSI6Miwic3ViX2NhdGVnb3J5IjoicnJyIn1dfX0.AHRiKSO2xLvkq5r7SYAanGwAw2PJQWmNQZyekBphkBk"
# data = get_data(jwt_token)
# b = "eyJhbGciOiJIUzI1NiIsImFjY291bnQiOiJBQTA0MjUiLCJ0eXAiOiJKV1QifQ==".encode()
# print(b)
# h = base64.b64decode(b).decode()
# print(h)
# print(data)
# timestamp = 1598863424
# token = gen_jwt_data(data=data1, secret="123456789", timestamp=timestamp)
# print(token)

# secret = "123456789"
# header = {
#     "alg": "HS256",
#     "account": "AA0425",
#     "typ": "JWT"
# }
# pay_load = {
#     "data": data1,
#     "timestamp": 1598863424
# }
# stringA = base64.b64encode(json.dumps(header).encode()).decode()
# print(stringA)
# stringB = base64.b64encode(json.dumps(pay_load).encode()).decode()
# print(stringB)
# message = stringA + "." + stringB
# h_obj = hmac.new(message.encode("utf-8"), secret.encode("utf-8"), hashlib.sha256)
# sign = h_obj.hexdigest()
# # sha256 = hashlib.sha256(stringA + "." + stringB + secret)
# # sha256.update((stringA + "." + stringB + secret).encode("utf-8"))
# # sign = sha256.hexdigest()
# # print(sign)
# jwt_token = message + "." + sign
# print(jwt_token)

list1 = [22, 33, 54, 65, 78, 55, 34, 21]
list2 = []
# for i in range(len(list1) - 1):
#     for j in range(len(list1) - 1):
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
# print(list1)
for i in range(len(list1)-1):
    minIndex = i
    for j in range(i + 1, len(list1)):
        if list1[minIndex] > list1[j]:
            minIndex = j
    if i != minIndex:
        list1[i], list1[minIndex] = list1[minIndex], list1[i]
print(list1)
