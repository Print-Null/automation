import configparser
import json
import logging
import os

#读取common文件
logging.basicConfig(level=logging.INFO)
logging.info(" 开始读取Common.ini文件")
def read_common(data):
    cf = configparser.ConfigParser()
    # 2.从配置文件中读取数据
    # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # path_common = curpath + "/Config/common.ini"

    # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    # path_common = root_path + "/app/Kit/Storekeeper/Config/common.ini"

    root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    path_common = root_path + "/app/Kit/Courier/Config/common.ini"

    cf.read(path_common, encoding="UTF-8")
    # # 读取所有section
    # print(cf.sections())  # 返回列表形式    ['mysql_info', 'test_addSection']
    # # 读取section下的option
    # print(cf.options(section="test"))  # 只有key值 ['mysql_host', 'mysql_port', 'mysql_db', 'mysql_user', 'mysql_passwd']
    # # 读取键值对
    # print(cf.items(
    #     section="test"))  # 键值对 [('mysql_host', '120.76.42.189'), ('mysql_port', '3306'), ('mysql_db', 'future'), ('mysql_user', 'futurevistor'), ('mysql_passwd', '123456')]
    # # 读section里option
    # print(cf.get("test", "host"))  # 127.0.0.1
    # # print(cf.getint("test","login_user")) #3306
    # print(cf.get("test", "login_user"))  # 3306

    get_common = cf.get("test", data)
    logging.info("配置文件%s读取成功"%data)
    return get_common



# if __name__ == '__main__':
#     read_common("host")