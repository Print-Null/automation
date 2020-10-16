import json
import random
import requests

# 数据库取出来的未揽收的运单号
pno_list = ["TH46061RHZ3Z", "TH46061RHZ0Z", "TH46061RHS0Z", "TH46061RHP9Z", "TH46061RHP2Z", "TH46061RHP0Z",
            "TH46061RHN9Z", "TH46061RHN8Z", "TH47221RHN7Z", "TH47221RH92Z", "TH41111RH42Z", "TH41111RH40Z",
            "TH41111RH41Z", "TH41111RH39Z", "TH41111RH38Z", "TH41111RH36Z", "TH41111RH37Z", "TH41111RH34Z",
            "TH41111RH35Z", "TH41111RH32Z"]

for i in pno_list:
    url = "http://192.168.0.228:8080/api/courier/v1/t3/create_parcel"
    header = {
        "Accept-Language": "zh-CN",
        "Content-Type": "application/json; charset=UTF-8",
        "X-FLE-SESSION-ID": "1599134601_ffe2f86fc43faf9c2fb1dd1b026ee94374904fb5a6d9fb5b2b4122597f1dbb11_20325"
    }
    params = {
        "article_category": random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 99]),
        "cod_amount": random.randrange(100, 5000000, 100),
        "cod_enabled": True,
        "customer_id": "AA0316",
        "customer_type_category": 2,
        "dst_city_code": "TH4722",
        "dst_country_code": "TH",
        "dst_name": "Mr R",
        "dst_postal_code": "50360",
        "dst_province_code": "TH47",
        "express_category": 1,
        "freight_insure_enabled": True,
        "height": 100,
        "insure_declare_value": random.randrange(100, 5000000, 100),
        "insured": True,
        "length": 100,
        "mobile": "0861234567",
        "parcel_bar_code": i,
        "same_province": 1,
        "skipping_tips": [],
        "ticket_pickup_id": 115322,  # kit上的pickup_id
        "weight": random.randint(1, 50000),
        "width": 80
    }
    res = requests.post(url=url, headers=header, json=params)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
