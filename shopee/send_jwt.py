import json

import jwt
import time

import requests

expire_time = int(time.time() + 3600)
params = {
    "order": {  # order必填
        "reference_no": str(int(time.time())),
        "business_type": 1,  # 必填字段
        "total_weight": 1.0,
        "goods_value": "2.5"
    },
    "item_info": [{  # 这个字段数据非必填
        "item_name": "item1",
        "item_quantity": 1,  # 最大取值？
        "length": 12,  # 最大取值？
        "width": 9,  # 最大取值？
        "height": 5  # 最大取值？
    }],
    "sender_info": {
        "name": "shopee",  # 必填字段
        "company_name": "My shop",
        "sender_id": "AA0425",
        "email": "",
        "phone": "2516352482",  # 必填字段
        "country": "aa",  # 必填字段
        "state": "hebei",  # 必填字段
        "city": "อำเภอเมืองเชียงใหม่",  # 必填字段
        "district": "nanshan",
        "subdistrict": "",
        "street": "",
        "detail_address": "测试揽收",  # 必填字段
        "zip_code": "50100",
        "longitude": "",
        "latitude": "",
        "remark": "sender remark"  # 必填字段，可以为""
    },
    "receiver_info": {
        "name": "Mr R",  # 必填字段
        "email": "",
        "phone": "0135454545",  # 必填字段
        "country": "TH",  # 必填字段
        "state": "จังหวัดมุกดาหาร",  # 必填字段
        "city": "อำเภอหว้านใหญ่",  # 必填字段
        "district": "nanshan",
        "subdistrict": "",
        "street": "",
        "detail_address": "测试快递员揽收",  # 必填字段
        "zip_code": "49150",
        "longitude": "",
        "latitude": "",
        "remark": "receiver remark"  # 必填字段，可以为""
    },
    "service_info": {
        "service_types": "11",  # 必填字段
        "cod_amount": 0.0111111111
        # "schedule_pickup_date_time": expire_time
        # "schedule_pickup_timeslot": {
        #     "start_time": int(time.time()),
        #     "end_time": expire_time
        # }
    }
}
url = "http://192.168.0.231:8080/callback/shopee/order"
account = "AA0425"
secret = "123456789"


# class SendJWT(object):


def gen_jwt_data(data, secret):
    jwt_header = {"alg": "HS256",
                  "typ": "JWT",
                  "account": "AA0425"
                  }
    jwt_payload = {
        "data": data,
        "timestamp": int(time.time())
    }
    return {"jwt": jwt.encode(jwt_payload, secret, headers=jwt_header, algorithm="HS256").decode('utf-8')}


# def send_jwt_http_request(headers=None):
print("请求url:\n%s" % url)
headers = {"alg": "HS256",
           "typ": "JWT",
           "account": "AA0425",
           "content-type": "application/json"
           }
jwt_data = gen_jwt_data(params, secret)
# headers.update(jwt_data)
print("请求header:\n%s" % headers)
# params.update(jwt_data)
parameter = {"data": params, "timestamp": int(time.time())}
# params.update(parameter)
# print("params:\n%s" % params)
# parameter.update(jwt_data)
# parameter = json.dumps(parameter)
print("请求参数:\n%s" % parameter)
reply = requests.session().post(url, json=parameter, headers=headers, verify=False)
print(reply.json())
print(reply.json()["message"])
print(reply.status_code)
