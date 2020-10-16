import logging
import os

#读取快递员session
from utils.redisbase import RedisBase

logging.basicConfig(level=logging.INFO)
# logging.info("快递员session_id 开始读取文件")
logging.info("获取redis中的数据信息")
def read_courier_session_id(key):
    #读取数据库里的session_id
    # 获取redis中的数据信息
    return RedisBase().get(key)


    # # curpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # # yamlpath = curpath + "/Config/session_courier.yaml"
    #
    # root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__)).split("flash")[0] + "/flash/")
    # yamlpath = root_path + "/app/Kit/Courier/Config/session_courier.yaml"
    #
    # with open(yamlpath, 'r') as f:
    #     session_couier = f.read().split(":")[1].strip()
    #     logging.info(session_couier)
    #     logging.info("快递员session_id 文件读取成功")
    #     return session_couier



#
# if __name__ == '__main__':
#     read_courier_session_id()