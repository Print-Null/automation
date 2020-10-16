from redis import Redis

r = Redis(host='127.0.0.1', port=6379)
r.set("name", "yxf")
print(r.get("name"))
