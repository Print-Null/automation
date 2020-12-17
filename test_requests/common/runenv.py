import sys
import os
import configparser
import redis

try:
    runenv = sys.argv[1]
    print("获取到的Jenkins参数是：")
    print(runenv)
    if runenv in ['trunk', 'training', 'pro']:
        runenvpy = runenv
    else:
        runenvpy = "trunk"
except:
    runenvpy = "trunk"
cf = configparser.ConfigParser()
configpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "env.ini")
cf.read(configpath, encoding="utf-8")
host = cf.get("redis", "REDIS_HOST")
port = cf.get("redis", "REDIS_PORT")
bucket = cf.get("redis", "REDIS_BUCKET")
expiretime = cf.get("redis", "REDIS_EXPIRETIME")
pwd = cf.get("redis", "REDIS_PWD")
conn = redis.Redis(host=host, port=port, db=bucket, password=pwd, encoding="utf-8")
conn.set("runenv_py", runenvpy, ex=expiretime)
exit("runenv_py read in redis success")
