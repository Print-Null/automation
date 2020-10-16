import logging

from common.readconfig import ReadConfig
from utils.redisbase import RedisBase

#根据redis中存储的环境变量参数，获取.env中的配置参数信息
class Common_data():
    logging.basicConfig(level=logging.INFO)
    #返回运行时host
    def each_parameter(self, data):
        redisObj = RedisBase()
        #获取redis中的环境变量参数
        host_env = redisObj.get("runenv_py")
        logging.info("redis从数据库读取到的参数是：%s"%host_env)
        data = ReadConfig().get_config(host_env, data)
        logging.info("根据Redis参数%s"%host_env + "读取env.ini的数据，读取到的参数是：%s"%data)
        logging.info(data)
        return data


    def write_parameter_to_redis(self,key,value):
        redisObj = RedisBase()
        redisObj.set(key=key, value=value, ex=6000)

    def get_parameter_from_redis(self, key):
        redisObj = RedisBase()
        return redisObj.get(key)

    def append_data(self, k, v):
        redisObj = RedisBase()
        if k :
            k = "Kit_Storekeeper_" + str(k)
        return redisObj.append_(key=k, value=v)



#
# if __name__ == '__main__':
#     co = Common_data()
#     co.each_parameter("host")