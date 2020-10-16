# import configparser
# import logging
# import os
#
# logging.basicConfig(level=logging.INFO)
# logging.info("读取 获取车牌号等信息，plate_number.ini文件")
# def read_plate_number(sections,option):
#     cf = configparser.ConfigParser()
#     # 2.从配置文件中读取数据
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # path_common = curpath + "/conf/plate_number.ini"
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     path_common = root_path + "/app/Kit/Storekeeper/conf/plate_number.ini"
#
#     cf.read(path_common, encoding="UTF-8")
#     get_common = cf.get(sections, option)
#     logging.info("读取获取车牌号等信息，plate_number.ini %s模块下的%s读取成功,读取到的值是%s"%(sections, option, get_common))
#     return get_common
