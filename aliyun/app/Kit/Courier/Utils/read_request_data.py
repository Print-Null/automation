import configparser
import logging
import os

#读取common文件
from utils.redisbase import RedisBase

logging.basicConfig(level=logging.INFO)
logging.info(" 开始读取common.ini文件")
def read_request_data(key):
    #读取redis中的参数
    return RedisBase().get(key)




    # cf = configparser.ConfigParser()
    # # 2.从配置文件中读取数据
    # # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # # path_common = curpath + "/Config/request_data.ini"
    #
    # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    # path_common = root_path + "/app/Kit/Courier/Config/request_data.ini"
    # # print("a"*888)
    # # print(path_common)
    # # print("a"*888)
    # cf.read(path_common, encoding="UTF-8")
    # get_common = cf.get(sections, option)
    # logging.info("配置文件common.ini%s模块下的%s读取成功,读取到的值是%s"%(sections, option, get_common))
    # return get_common



# if __name__ == '__main__':
#     read_request_data("ticket_pickup","ticket_pickup_id")