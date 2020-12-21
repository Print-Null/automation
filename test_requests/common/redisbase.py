import os
import redis
from common.readconfig import ReadConfig
import logging


class RedisBase(object):
    def __init__(self):
        try:
            confObj = ReadConfig()
            host = confObj.get_config("redis", "REDIS_HOST")
            port = confObj.get_config("redis", "REDIS_PORT")
            bucket = confObj.get_config("redis", "REDIS_BUCKET") if confObj.get_config("redis", "REDIS_BUCKET") else 0
            pwd = confObj.get_config("redis", "REDIS_PWD") if confObj.get_config("redis", "REDIS_PWD") else None
            self.ex = confObj.get_config("redis", "REDIS_EXPIRETIME")
            self.conn = redis.Redis(host = host, port = port, password = pwd, db = bucket)
            self._label = os.path.abspath(os.path.dirname(os.getcwd())).split(os.path.sep)
            self._label.reverse()
        except Exception as e:
            logging.error("Redis connection failed, error message:%s", e)

    # 根据key值获取
    def get(self, key):
        try:
            # if key and key != "runenv_py":
            #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
            res = self.conn.get(key)
            if res:
                return res.decode()
            else:
                return False
        except Exception as e:
            return False

    # 写入了一个键值对
    def set(self, key, value, ex):
        # if key and key != "runenv_py":
        #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
        if ex:
            return self.conn.set(key, value, ex = ex)
        else:
            return self.conn.set(key, value, ex = self.ex)

    def append_(self, key, value):
        return self.conn.append(key=key, value=value)


    # 将一个或多个值 value 插入到列表 key 的表头
    def lpush(self, key, value):
        # if key and key != "runenv_py":
        #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
        return self.conn.lpush(key, value)

    # 获取在存储于列表的key索引的元素
    def lindex(self, key, index):
        # if key and key != "runenv_py":
        #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
        res = self.conn.lindex(key, index)
        if res:
            return res.decode()

    # 返回列表 key 的长度
    def llen(self, key):
        # if key and key != "runenv_py":
        #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
        return self.conn.llen(key)

    # 让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除
    def ltrim(self, key, start, end):
        # if key and key != "runenv_py":
        #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
        return self.conn.ltrim(key, start, end)

    # 删除指定的键
    def delete(self, key):
        try:
            # if key and key != "runenv_py":
            #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
            self.conn.delete(key)
            return True
        except:
            return False

    def exists(self, key):
        # if key and key != "runenv_py":
        #     key = str(self._label[1]) + "_" + str(self._label[0]) + "_" + str(key)
        return self.conn.exists(key)

    # 匹配批量删除  key*
    def delete_keys(self, keys):
        try:
            self.conn.delete(*self.conn.keys(pattern = keys))
            return True
        except:
            return False
