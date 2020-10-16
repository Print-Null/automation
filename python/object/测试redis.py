# from redis import Redis
#
# r = Redis(host='192.168.31.52', port=6379)
# r.set("name", "yxf")
# print(r.get("name"))

import redis

r = redis.StrictRedis(host="localhost", db=14, port=6379, decode_responses=True, password="flash123")
r.set("土地", "black")
print(r.get("土地"))
