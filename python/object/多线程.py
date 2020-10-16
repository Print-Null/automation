import threading
import time


def fun(num):
    print("创建线程%d" % num)
    time.sleep(1)


for i in range(5):
    t = threading.Thread(target=fun, args=(i + 1,))
    t.start()
