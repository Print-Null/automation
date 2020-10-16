# url = "/api/webhook/tracking/([a-zA-Z0-9_\-]+)"
params = {
    "carrier_tn": "asgxzzvv",  # Y,下单接口返回的承运商单号
    "current_status": "3",  # Y,当前物流商最新状态码，trackings中也需要包含
    "trackings": [
        {
            "status": "1",  # Y,物流商状态码
            "sub_status": "",
            "reason": "reason a",
            "description": "description",  # Y,物流商状态描述
            "location": "xxxxxxx",  # Y,站点地址或站点名称，没有可以传空
            "operator": "",  # Y,状态更新时间，时间戳
            "operator_phone": "",
            "update_time": 1569310602,
            "extend_fields": {
                "license_plate_number": "BA-1234"
            }
        },
        {
            "status": "3",
            "sub_status": "",
            "reason": "reason b",
            "description": "description",
            "location": "xxxxxxx",
            "update_time": 1569910602
        }
    ]
}

