# import configparser
# import logging
# import os
#
# logging.basicConfig(level=logging.INFO)
# logging.info("填写数据到ini文件中")
# def write_config_ini(file_name, section, option, value):
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # print(curpath)
#     # # session_path = curpath + "/conf/vehicle_voucher.ini"
#     # session_path = curpath + "/conf/" + file_name + ".ini"
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     session_path = root_path + "/app/Kit/Storekeeper/conf/"+ file_name + ".ini"
#
#     cf = configparser.ConfigParser()
#     # add section 添加section项
#     # set(section,option,value) 给section项中写入键值对
#     cf.add_section(str(section))
#     cf.set(str(section), option=str(option), value=str(value))
#     with open(session_path, "w+") as f:
#
#         cf.write(f)
#
#     logging.info("数据写入到文件%s.ini中:[section]是:%s,option=%s,value=%s"%(file_name,section,option,value))
