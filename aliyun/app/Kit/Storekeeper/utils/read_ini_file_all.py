# import configparser
# import logging
# import os
#
# #storekeeper_session_id
# logging.basicConfig(level=logging.INFO)
# logging.info(" storekeeper_session_id.ini文件")
# def read_all_ini(file_name,sections,option):
#     cf = configparser.ConfigParser()
#     # 2.从配置文件中读取数据
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # path_common = curpath + "/conf/"+"storekeeper_session_id"+".ini"
#     # path_common = curpath + "/conf/"+file_name+".ini"
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     path_common = root_path + "/app/Kit/Storekeeper/conf/" + file_name + ".ini"
#
#     # os.path.join(os.path.abspath(
#     #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
#     #     "conf/query_company_name.ini")
#     cf.read(path_common, encoding="UTF-8")
#     get_common = cf.get(sections, option)
#     logging.info("storekeeper_session_id.ini %s模块下的%s读取成功,读取到的值是%s"%(sections, option, get_common))
#     return get_common