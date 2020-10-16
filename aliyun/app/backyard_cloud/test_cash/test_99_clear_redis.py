#!/usr/bin/python3
# -*- coding: utf-8 -*-
#@Time   :2020/8/24 14:32
#@Author :lemon_yaoxiaonie
#@Email  :363111505@qq.com
#@File   :test_clear_redis.py
from utils.redisbase import RedisBase
import logging
def clear_redis(key):
    if RedisBase().exists(key):
        logging.info("需要清理redis的{0}数据".format(key))
        RedisBase().delete(key)
    else:
        logging.info("不需要清理redisd{0}数据".format(key))

clear_redis("country_code")
clear_redis("size")
clear_redis("industery")
clear_redis("transportation_type")