# #courier，快递员登入的session返回
# import logging
# import os
#
# from ruamel import yaml
#
# # from Courier.Script.courier_login import Login
# # from app.kit.Courier.Script.courier_login import Login
# from app.Kit.Courier.Script.courier_login import Login
#
# logging.basicConfig(level=logging.INFO)
#
# #快递员session 写入文件/Config/session_courier.yaml
# logging.info("快递员session 写入文件/Config/session_courier.yaml")
# def courier_session_id%%():
#     login = Login()
#     resp = login.login()
#     print(resp["data"]["sessionid"])
#     session_id = {
#         "courier_session_id": resp["data"]["sessionid"]
#     }
#
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # print(curpath)
#     # yamlpath = curpath + "/Config/session_courier.yaml"
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     yamlpath = root_path + "/app/Kit/Courier/Config/session_courier.yaml"
#
#     # 写入到yaml文件
#     with open(yamlpath, 'w+', encoding="utf-8") as f:
#         yaml.dump(session_id, f, Dumper=yaml.RoundTripDumper)
#         logging.info("快递员session_id写入文件成功")
#
# # if __name__ == '__main__':
#     courier_session_id()