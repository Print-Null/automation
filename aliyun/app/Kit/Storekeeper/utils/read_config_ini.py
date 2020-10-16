# import configparser
# import logging
# import os
#
# logging.basicConfig(level=logging.INFO)
# logging.info("读取 config目录下的文件")
# def read_config_ini(file_name,sections,option):
#     cf = configparser.ConfigParser()
#     # 2.从配置文件中读取数据
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # # path_common = curpath + "/conf/vehicle_voucher.ini"
#     # path_common = curpath + "/conf/"+file_name+".ini"
#
#
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     path_common = root_path + "/app/Kit/Storekeeper/conf/"+file_name+".ini"
#
#
#     cf.read(path_common, encoding="UTF-8")
#     get_common = cf.get(sections, option)
#     logging.info("config目录下文件名%s: %s文件的%s读取成功,读取到的值是%s"%(file_name, sections, option, get_common))
#
#     return get_common