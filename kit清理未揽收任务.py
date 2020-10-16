import requests

url_get_ticket = "http://192.168.0.228:8080/api/courier/v1/ticket/simplified_list?abnormal_state=2"
header = {"Accept-Language": "zh-CN",
          "X-FLE-SESSION-ID": "1599465701_887f85aeff16776ebd166fde9d90e412d6c6752f95aec64e777257e4b9ab8411_20325"
          # "X-FLE-SESSION-ID": "1596096039_63f49455862b94856b56f61c9857d9bb4ed15874f294e5e10608cad384b40b0f_22173"
          # "X-FLE-SESSION-ID": "1596112995_36cd43c25cdd7727814111a2249278555356e9b3606849412f03db68bc0f8928_21207"
          }
req_ticket = requests.get(url=url_get_ticket, headers=header)
print(req_ticket.json()["data"]["pickup"])
pickups_list = req_ticket.json()["data"]["pickup"]
for i in pickups_list:
    # print(i)
    id = i["id"]
    if i["state"] != 1:
        continue
    else:
        if i["parcel_number"] == i["estimate_parcel_number"]:
            url_ticket = "http://192.168.0.228:8080/api/courier/v1/ticket/{0}".format(id)
            req_ticketed = requests.post(url=url_ticket, headers=header)
            print("订单{0}的所有包裹已揽收，可以完成揽收".format(id))
        else:
            print("订单{0}有未揽收的包裹，请先完成其他包裹的揽收".format(id))
            url_get_confirm = "http://192.168.0.228:8080/api/courier/v1/ticket/pickups/{0}".format(id)
            req_confirm = requests.get(url=url_get_confirm, headers=header)
            parcel_list = req_confirm.json()["data"]["not_collected_parcels"]
            try:
                for j in parcel_list:
                    order_id = j["user_order_id"]
                    params_ticket = {
                        "addr_core_ids": [], "width": 14, "weight": 5000, "user_order_id": order_id,
                        "src_province_code": "TH03", "dst_city_code": "TH2001", "dst_country_code": "TH",
                        "dst_detail_address": "24000的详细地址", "dst_district_code": "TH200101", "dst_name": "24000名字",
                        "dst_phone": "01346624000", "insured": False, "article_category": 0,
                        "dst_postal_code": "20000", "dst_province_code": "TH20", "src_postal_code": "11000",
                        "src_phone": "01346610260", "height": 6, "insure_declare_value": 0, "src_name": "10260姓名",
                        "length": 20, "request_ids": [], "src_district_code": "TH030101", "skipping_tips": [],
                        "src_city_code": "TH0301", "src_country_code": "TH", "src_detail_address": "10260详细地址",
                        "settlement_category": 1, "call_duration": 0, "freight_insure_enabled": False,
                        "express_category": 1, "cod_enabled": False, "total_amount": 5500, "cod_amount": 0
                    }
                    url_confirm = "http://192.168.0.228:8080/api/courier/v1/ticket/pickups/{0}/confirm".format(id)
                    print(url_confirm)
                    req_confirmed = requests.post(url=url_confirm, headers=header, json=params_ticket)
                    # print(req_confirmed.json())
                    print("order_id为{0}的包裹已揽收，运单号为{1}".format(order_id,
                                                              req_confirmed.json()["data"]["parcel_info"]["pno"]))
                url_ticket = "http://192.168.0.228:8080/api/courier/v1/ticket/{0}".format(id)
                req_ticketed = requests.post(url=url_ticket, headers=header)
                print("订单{0}的所有包裹已揽收完成".format(id))
            except Exception as e:
                print("未找到指定的包裹")
                raise e
            finally:
                continue
