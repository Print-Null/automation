url = "/api/webhook/billing/([a-zA-Z0-9_\-]+)"
params = {
    "carrier_tn": "abcdefg",  # Y,下单接口返回的承运商单号
    "chargeable_weight": int,  # N,计费重量，克
    "shipping_fee": ""  # N,字符串，只允许数字和小数点，实际运费
}

