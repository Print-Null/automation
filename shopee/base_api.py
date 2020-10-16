import json
import time
import jwt
import pymysql
import requests
from common import base

number = 0


class BaseApi(object):
    expire_time = int(time.time() + 7200)  # 2小时后超时

    def gen_jwt_data(self, data, secret):
        jwt_header = {"alg": "HS256",
                      "typ": "JWT",
                      "account": "AA0425"
                      }
        jwt_payload = {
            "data": data,
            "timestamp": self.expire_time
        }
        return {"jwt": jwt.encode(jwt_payload, secret, headers=jwt_header, algorithm="HS256").decode('utf-8')}

    def send_assert_and_save(self, url, data, headers):
        # error_list = ["Parameter logic error", "Servicer error"]
        print("请求地址:\n%s" % url)
        print("请求头:\n%s" % headers)
        parameter = {"data": data, "timestamp": int(time.time())}
        print("请求参数:\n%s" % parameter)
        # jwt_data = self.gen_jwt_data(account, data, secret)
        # print("jwt_data:\n%s" % jwt_data)
        reply = requests.session().post(url, json=parameter, headers=headers, verify=False)
        print("响应体：\n%s" % json.dumps(reply.json(), indent=2, ensure_ascii=False))
        if reply.status_code == 200:
            if reply.json()["retcode"] == 0:
                assert reply.json()["message"] == "SUCCESS"
                if reply.json()["data"] is None:
                    pass
                else:
                    global number
                    base.RedisBase().set("order_creation_api_" + str(number), reply.json()["data"]["carrier_tn"],
                                         ex=6000)
                    number = number + 1
            elif reply.json()["retcode"] == -10005:
                assert reply.json()["message"] == "Parameter logic error"
            elif reply.json()["retcode"] == -100002:
                assert reply.json()["message"] == "Servicer error"
            elif reply.json()["retcode"] == -110004:
                assert reply.json()["message"] == "Shipment no. not found"
            elif reply.json()["retcode"] == -300001:
                assert reply.json()[
                           "message"] == \
                       "The shipment order cannot be updated, due to the current shipment order status."
            elif reply.json()["retcode"] == -400001:
                assert reply.json()[
                           "message"] == \
                       "The shipment order cannot be cancelled, due to the current shipment order status."
        return reply.json()

    def get_staff_info_id(self, pno):
        connection = None
        cursor = None
        try:
            connection = pymysql.connect("192.168.0.229", "fle_development", "123456", "fle_development")
            cursor = connection.cursor()  # 创建操作数据库的实例
            sql = 'select id,staff_info_id from ticket_pickup where ka_warehouse_id = ' \
                  '(SELECT ka_warehouse_id from order_info where pno="{0}")'.format(pno)  # 创建执行的数据库语句
            try:
                cursor.execute(sql)  # 执行数据库语句
                emp = cursor.fetchall()
                for i in emp:
                    order_id = i[0]
                    staff_info_id = i[1]
                    return [order_id, staff_info_id]
            except Exception as ex:
                print(ex)
        except Exception as ex:
            print(ex)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
