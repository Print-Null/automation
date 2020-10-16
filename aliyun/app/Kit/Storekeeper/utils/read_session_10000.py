# import configparser
# import logging
# import os
#
# #storekeeper_session_id
# logging.basicConfig(level=logging.INFO)
# logging.info("读取 后台10000号，session_10000.ini文件")
# def read_session_10000(sections,option):
#     cf = configparser.ConfigParser()
#     # 2.从配置文件中读取数据
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # path_common = curpath + "/conf/session_10000.ini"
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     path_common = root_path + "/app/Kit/Storekeeper/conf/session_10000.ini"
#
#     cf.read(path_common, encoding="UTF-8")
#     get_common = cf.get(sections, option)
#     logging.info("后台10000号，session_10000.ini %s模块下的%s读取成功,读取到的值是%s"%(sections, option, get_common))
#     return get_common
