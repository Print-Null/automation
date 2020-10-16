# import configparser
# import os
#
#
# def pack_no_range(sections, option):
#     #先读取数字
#     cf = configparser.ConfigParser()
#     # 2.从配置文件中读取数据
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # path_common = curpath + "/conf/pack_number.ini"
#     # path_common = os.path.join(os.path.abspath(
#     #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
#     #     "conf/pack_number.ini")
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     path_common = root_path + "/app/Kit/Storekeeper/conf/pack_number.ini"
#
#
#     cf.read(path_common, encoding="UTF-8")
#     get_common = cf.get(sections, option)
#     print(get_common)
#     #将数字+1重新写入
#
#     value = int(get_common)+1
#     print(value)
#     cf.set(sections, option, str(value))
#     with open(path_common, 'w') as f:
#         cf.write(f)
#
#     return get_common
#
# def read_pack_num_only(sections, option):
#     # 先读取数字
#     cf = configparser.ConfigParser()
#     # 2.从配置文件中读取数据
#     # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#     # path_common = curpath + "/conf/pack_number.ini"
#
#     # path_common = os.path.join(os.path.abspath(
#     #     os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/app/Kit/Storekeeper/"),
#     #     "conf/pack_number.ini")
#
#     root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
#     path_common = root_path + "/app/Kit/Storekeeper/conf/pack_number.ini"
#
#     cf.read(path_common, encoding="UTF-8")
#     get_common_ = cf.get(sections, option)
#     print(get_common_)
#     return get_common_
#
#
# if __name__ == '__main__':
#     read_pack_num_only("pack_no", "pack_num")